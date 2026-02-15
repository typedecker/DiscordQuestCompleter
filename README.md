# Discord Quest Completer

Welcome to the README of the Discord Quest Completer project. This program's sole aim is to automate the typically manual work of creating a virtual path to run a dummy executable from, to simulate the completion of a discord quest that involves playing a game.
Specific utilities have been added to ensure an easier workflow for those using the program.

## How to download the program or where to download it from?

The code/files within the repo itself are only for viewing purposes incase someone wants to ensure the safety of the code behind this program. To be able to run the actual program, you must download the .exe file from the latest release of this repository.

## How to use it?

**This only works on windows and I cannot guarantee the working of this program for other Operating Systems. Keep that in mind as you read ahead.**

* In most basic cases, you can just type the name of the game you want to run, mention the number of seconds for which you'd like to "play" that game[leaving the time field empty will make it default to 900 seconds i.e. 15 mins], leave the address field empty and hit the launch button; the program will typically figure out the launch path on it's own using the steam API.

<img width="568" height="513" alt="image" src="https://github.com/user-attachments/assets/94bdaa8e-4811-4f08-82a8-58d6e5292060" />



* In certain cases tho, the launch path found using the steam api is not the correct one, or it may just be pointing to the custom launcher of the game instead, and in such cases discord won't detect the game running from that path, and you'd have to resort to looking for the original path of the game via the r/DiscordQuests subreddit or through the steamdb depot information for the game. Once the address has been found, you can paste the exact address past the common folder part[example: for the path `common/Vindictus/Vindictus_x64.exe` you'd just have to type in `Vindictus/Vindictus_x64.exe`] into the address field, and mention the time you want it to run for, in the time field -- the name field in this case can be left entirely empty; and it should be able to simulate the game being ran on your system through that.

<img width="600" height="474" alt="image" src="https://github.com/user-attachments/assets/a18e53eb-05be-42dd-801f-9501c4a82f16" />



* For Non steam games, it is almost always certainly not going to be able to fetch the game/program itself from just the name of it, and you'd have to mention the address in the address field before launch.

* Upon pressing the launch button, a new window will popup, with a progress bar, and a progress and time label to indicate how long the window must be kept up for. This window can be closed at any moment, if you'd like to halt the execution of the program. The code has been written such that it recovers from the sudden closing of the simulated game window.

<img width="601" height="471" alt="image" src="https://github.com/user-attachments/assets/ab2909e8-a72f-46e5-8d66-175d8439b804" />



* Note that mentioning the time is optional and it'll default to 900 seconds i.e. 15 mins, if no time is mentioned in the time field. The option is available in case you need to run a game for a shorter or longer duration than the default of 15 minutes.

* For games that you already own, you won't lose the original .exe, as it'll temporarily rename the original exe whilst running itself, and then put the original .exe back in place when its done. Also any and all directories manually created during the running of this program are deleted after the "simulated" game has stopped running.

## Feedback & Suggestions

If anyone has any ideas on things that could be added to this project, or if you'd like to suggest new features, feel free to do so! I'll also try to help out with any issues being faced via the subreddit post or on here <3

Furthermore, if anyone has an idea on how to fetch the depot information without having to use a steam api key or having to login non-anonymously using code -- then let me know and we can add that to the project to make it robust and have it work in every single case <3. Also for anyone looking into this -- I've already looked through the python steam module docs and I am aware of the cdn client being used for depot info, but my previous attempts at fetching depot info that way, have failed and it always returns an empty list.

---

## Disclaimer & Limitation of Liability

**This tool is provided for educational and research purposes only.**

By using this software, you acknowledge and agree to the following:

* **No Affiliation:** This project is not affiliated with, endorsed by, or supported by Discord, any game developers, or their respective parent companies.
* **Risk of Use:** Use of automation tools, "quest completers," or software that simulates user behavior may violate **Discord's Terms of Service (ToS)**. Use of this program may result in account warnings, temporary suspensions, or permanent bans.
* **No Warranty:** This software is provided "as is," without warranty of any kind, express or implied. The author(s) make no guarantees regarding the safety, functionality, or continued compatibility of this tool.
* **Limitation of Liability:** In no event shall the author(s) or copyright holders be held liable for any claims, damages, account losses, or other consequences arising from the use, inability to use, or the "misuse" of this software.
* **User Responsibility:** You are solely responsible for your own actions and any consequences that arise from running this executable. 

**If you do not agree to these terms, do not download, install, or run this software.**
