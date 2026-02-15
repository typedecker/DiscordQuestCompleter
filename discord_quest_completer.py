# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 18:10:20 2026

@author: ketch
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder

from kivy.uix.label import Label
from kivy.uix.popup import Popup

from pathlib import Path
from steam.client import SteamClient
import shutil, os, subprocess, threading, requests, sys

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath('.'), relative)


common_folder_addr = r'C:\Program Files (x86)\Steam\steamapps\common'

app_kv = \
'''
AnchorLayout:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: 1, 1
    
    BoxLayout:
        orientation: 'vertical'
        size_hint: 0.5, 0.4
        spacing: '10dp'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, None
            
            Label:
                text: 'Game Name: '
                size_hint: 0.2, 0.5
            TextInput:
                id: name_input
                size_hint: 0.7, 0.5
                multiline: False
                font_size: '18sp'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, None
            
            Label:
                text: 'Address: '
                size_hint: 0.2, 0.5
            TextInput:
                id: addr_input
                size_hint: 0.7, 0.5
                multiline: False
                font_size: '18sp'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, None
            
            Label:
                text: 'Time(in secs): '
                size_hint: 0.2, 0.5
            TextInput:
                id: time_input
                size_hint: 0.7, 0.5
                multiline: False
                font_size: '18sp'
        
        AnchorLayout:
            size_hint: 1, None
            anchor_x: 'center'
            anchor_y: 'top'
            
            Button:
                id: launch_btn
                text: 'Launch'
                size_hint: None, 0.5
'''

def mkdir_track(path):
    p = Path(path)
    created = []

    for parent in reversed(p.parents) :
        if not parent.exists() :
            created.append(parent)

    if not p.exists() :
        created.append(p)

    p.mkdir(parents = True, exist_ok = True)

    return created

def get_game_path_by_name(game_query):
    # --- STEP 1: Find the AppID using the Store API ---
    search_url = f'https://store.steampowered.com/api/storesearch/?term={game_query}&l=english&cc=US'
    search_resp = requests.get(search_url).json()
    
    if not search_resp.get('items') :
        return

    # Grab the top result
    game_data = search_resp['items'][0]
    app_id = game_data['id']
    official_name = game_data['name']

    # --- STEP 2: Connect to Steam for internal metadata ---
    client = SteamClient()
    
    try:
        client.anonymous_login()
        product_info = client.get_product_info(apps = [app_id])
        
        if not product_info or 'apps' not in product_info:
            return

        app_config = product_info['apps'][app_id].get('config', {})
        
        # Get the folder name
        install_dir = app_config.get('installdir', official_name)
        
        # Get the executable relative path
        launch_data = app_config.get('launch', {})
        exe_rel_path = 'unknown.exe'
        
        if launch_data:
            # We take the first available launch option
            first_launch = list(launch_data.values())[0]
            exe_rel_path = first_launch.get('executable', '')

        # --- STEP 3: Construct Path ---
        # Note: We use the relative path provided by Steam (e.g., bin/game.exe)
        full_path = os.path.join(common_folder_addr, install_dir, exe_rel_path)
        
        return {
            'official_name': official_name,
            'app_id': app_id,
            'install_dir': install_dir,
            'exe_rel_path': exe_rel_path,
            'full_path': full_path
        }
    finally :
        client.disconnect()
    return

class DiscordGameQuestCompletionApp(App) :
    
    def on_start(self) :
        Window.set_title('Discord Quest Completer')
        # Window.set_icon(resource_path('icon.png')) # uncomment when compiling to .exe
        self.game_threads = []
        return
    
    def build(self) :
        self.layout = Builder.load_string(app_kv)
        self.layout.ids['launch_btn'].bind(on_press = self.launch)
        return self.layout
    
    def _launch_app(self, command, created_dirs, found_addr) :
        subprocess.run(command)
        if len(created_dirs) != 0 :
            shutil.rmtree(created_dirs[0])
        else :
            # if this was a preinstalled game, this portion of the code deletes the fake .exe and renames the backed up original exe into the correct .exe name for the game.
            dir_addr = os.path.dirname(found_addr)
            os.remove(found_addr)
            os.rename(os.path.join(dir_addr, 'old_game_file.exe'), found_addr)
        return
    
    def launch(self, e = None) :
        search_popup = Popup(
            title = 'Searching...',
            content = Label(text = 'Searching for the game in the steam database...'),
            auto_dismiss = False
        )
        # search_popup.open()
        
        exe_info = {
            'name': self.layout.ids['name_input'].text,
            'addr': self.layout.ids['addr_input'].text,
            'time': self.layout.ids['time_input'].text
        }
        
        if exe_info['addr'] == '' :
            found_result = get_game_path_by_name(exe_info['name'])
            # search_popup.dismiss()
            if found_result == None :
                search_failed_popup = Popup(
                    title = 'Search Failed',
                    content = Label(
                        text = f'The game -- {exe_info["name"]}, that you were searching for, could not be found in the steam DB. Click outside this dialog box to close it.',
                        text_size = (350, 120),
                    ),
                    size = (400, 300),
                    size_hint = (None, None)
                )
                search_failed_popup.open()
                return
            found_addr = found_result['full_path']
        else :
            found_addr = os.path.join(common_folder_addr, exe_info['addr'])
        dir_addr = os.path.dirname(found_addr)
        
        created_dirs = mkdir_track(dir_addr)
        if len(created_dirs) == 0: os.rename(found_addr, os.path.join(dir_addr, 'old_game_file.exe')) # rename the currently existing exe to something else temporarily.
        
        # shutil.copy(resource_path('dqc.exe'), found_addr) # uncomment when compiling to .exe
        shutil.copy('dqc.exe', found_addr) # found_addr = new_exe_addr # comment when compiling to .exe
        command = f'"{found_addr}" {int(exe_info["time"]) * 1000}'
        
        t = threading.Thread(target = self._launch_app, args = (command, created_dirs, found_addr))
        t.start()
        
        self.game_threads = [thread for thread in self.game_threads if thread.is_alive]
        self.game_threads.append(t)
        return
    
    def on_stop(self) :
        print('Joining all threads back to main thread...')
        for thread in self.game_threads :
            thread.join()
        return
    
    pass


if __name__ == '__main__' :
    app = DiscordGameQuestCompletionApp()
    app.run()