# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 00:03:27 2026

@author: ketch
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder

import sys, time, datetime

progress_bar_kv = \
'''
<-MyProgressBar@ProgressBar>:
    thickness: 24
    color: [1, 0, 0, 1]
    
    canvas:
        Color:
            rgb: 0.5, 0.5, 0.5, 1
        RoundedRectangle:
            pos: self.x, self.center_y - self.thickness/2
            size: self.width, self.thickness
            radius: [self.thickness/4]
        Color:
            rgba: self.color
        RoundedRectangle:
            pos: self.x, self.center_y - self.thickness/2
            size: self.width * (self.value / float(self.max)) if self.max else 0, self.thickness
            radius: [self.thickness/4]

AnchorLayout:
    anchor_x: 'center'
    anchor_y: 'center'
    
    BoxLayout:
        orientation: 'vertical'
        size_hint: 0.7, 0.35
        spacing: '5dp'
        
        Label:
            id: progress_label
            size_hint: 1, 0.01
            text: '0%'
        
        Label:
            id: time_label
            size_hint: 1, 0.01
            text: '(1 sec left)'
        
        MyProgressBar:
            id: progress_bar
            size_hint: 1, 0.01
            thickness: 10
            color: [0, 1, 0, 1]
            max: 1000
            value: 50
'''

def get_timedelta_str(dto) :
    hours, remainder = divmod(dto.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return (f'{hours} hours ' if hours > 0 else '') + (f'{minutes} mins ' if minutes > 0 else '') + (f'{round(seconds, 2)} secs' if seconds > 0 else '')

class dqcApp(App) :
    def on_start(self) :
        self.wait_time = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
        # Window.set_title(sys.argv[0])
        return
    
    def build(self) :
        self.wait_time = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
        self.layout = Builder.load_string(progress_bar_kv)
        self.progress_label = self.layout.ids['progress_label']
        self.time_label = self.layout.ids['time_label']
        self.progress_bar = self.layout.ids['progress_bar']
        self.progress_bar.max = self.wait_time
        
        self.start_time = time.time()
        
        Clock.schedule_interval(self.update_loading_bar, 0.5)
        Clock.schedule_once(lambda dt: Window.close(), (self.wait_time / 1000) + 1)
        return self.layout
    
    def update_loading_bar(self, dt) :
        progress_ms = (time.time() - self.start_time) * 1000
        progress_percentage = p if (p := round((progress_ms / self.wait_time) * 100, 2)) <= 100 else 100
        self.progress_bar.value = progress_ms
        self.progress_label.text = f'{progress_percentage}%'
        self.time_label.text = f'({get_timedelta_str(datetime.timedelta(milliseconds = (self.wait_time - progress_ms)))} left)'
        return

if __name__ == '__main__' :
    app = dqcApp()
    app.run()