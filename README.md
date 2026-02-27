# Discord Quest Completer

Welcome to the README of the Discord Quest Completer project. This program's sole aim is to automate the typically manual work of creating a virtual path to run a dummy executable from, to simulate the completion of a discord quest that involves playing a game.
Specific utilities have been added to ensure an easier workflow for those using the program.

## How to download the program or where to download it from?

The code/files within the repo itself are only for viewing purposes incase someone wants to ensure the safety of the code behind this program. To be able to run the actual program, you must download the .exe file from the latest release of this repository.

Also, make sure you have steam installed on your system. This program may work without it, but theres no guarantee of it.

## How to use it?

**This only works on windows and I cannot guarantee the working of this program for other Operating Systems. Keep that in mind as you read ahead.**

* In most basic cases, you can just type the name of the game you want to run, mention the number of seconds for which you'd like to "play" that game[leaving the time field empty will make it default to 900 seconds i.e. 15 mins], leave the address field empty and hit the launch button; the program will typically figure out the launch path on it's own using the steam API.

<img width="568" height="513" alt="image" src="https://github.com/user-attachments/assets/94bdaa8e-4811-4f08-82a8-58d6e5292060" />



* In certain cases tho, the launch path found using the steam api is not the correct one, or it may just be pointing to the custom launcher of the game instead, and in such cases discord won't detect the game running from that path, and you'd have to resort to looking for the original path of the game via the r/DiscordQuests subreddit or through the steamdb depot information for the game. Once the address has been found, you can paste the exact address into the address field, and mention the time you want it to run for, in the time field -- the name field in this case can be left entirely empty; and it should be able to simulate the game being ran on your system through that.

<img width="600" height="474" alt="image" src="https://github.com/user-attachments/assets/a18e53eb-05be-42dd-801f-9501c4a82f16" />



* For Non steam games, it is almost always certainly not going to be able to fetch the game/program itself from just the name of it, and you'd have to mention the address in the address field before launch.

* __**[FIX for Marathon & Toxic Commando-like games]**__ Recently it has been observed, that some games do not get detected by discord even if they are being run from the right path. The best guess on why this happens, is that discord checks if the folders for that game were created by steam or not. So if none of the above methods work, and the quest percentage isn't going up for you -- Try to hit the download button for that game on steam, and pause the download at 1-2% then use the discord quest completer the way you originally used to. Also, make sure discord_quest_completer is not running any dummy game windows when you hit the download button. If by any chance, the dummy game window was left open during download -- close the window now, and unpause the steam download for an extra percent, and then pause it again, after that the procedure is the same as usual. I'll try to post the address for the different games in the subreddit r/DiscordQuests. Unfortunately, for some games like the ones mentioned in this section, you do need steam to download them, but I'll try to find a fix that doesn't even require steam anymore, and will add it to my next few releases if possible.

* Upon pressing the launch button, a new window will popup, with a progress bar, and a progress and time label to indicate how long the window must be kept up for. This window can be closed at any moment, if you'd like to halt the execution of the program. The code has been written such that it recovers from the sudden closing of the simulated game window.

<img width="601" height="471" alt="image" src="https://github.com/user-attachments/assets/ab2909e8-a72f-46e5-8d66-175d8439b804" />



* Note that mentioning the time is optional and it'll default to 990 seconds i.e. 16.5 mins, if no time is mentioned in the time field. The option is available in case you need to run a game for a shorter or longer duration than the default of 16.5 minutes. You can also mention time using mathematical operations, such as `10 * 60` for 10 mins, or `(3 * 60) + 20` for 3 minutes and 20 seconds, and the time field should be able to make sense of it, on it's own.

* For games that you already own, you won't lose the original .exe, as it'll temporarily rename the original exe whilst running itself, and then put the original .exe back in place when its done. Also any and all directories manually created during the running of this program are deleted after the "simulated" game has stopped running.


## Commonly Faced Issue & it's solution

**[FIXED in v3.5]** (This issue should no longer happen in v3.5+ but you can reach out to me on reddit if this still happens) If you run into an error wherein it says that the path is invalid or something, just go to `C:/Program Files(x86)/Steam/steamapps/common/` and look for the folder mentioned in the error and delete it entirely, and close out of the program as well. Now restart the program and try again, the error should be gone.

## Feedback & Suggestions

If anyone has any ideas on things that could be added to this project, or if you'd like to suggest new features, feel free to do so! I'll also try to help out with any issues being faced via the subreddit post or on here <3

Furthermore, if anyone has an idea on how to fetch the depot information without having to use a steam api key or having to login non-anonymously using code -- then let me know and we can add that to the project to make it robust and have it work in every single case <3. Also for anyone looking into this -- I've already looked through the python steam module docs and I am aware of the cdn client being used for depot info, but my previous attempts at fetching depot info that way, have failed and it always returns an empty list.

## Future Plans

I am open to any and all suggestions and improvements ofcourse, but this section will highlight some of the personally desired features I'd like to add to this program:
1. Adding clickable/selectable options by default for commonly appearing quest games like Where Winds Meet.
2. Possibly finding a fix to the issue of not being able to locate the right path all the time -- by somehow figuring out a way of fetching the depot information or using some other workaround to fetch the original path.
3. Might add the option for the program to auto detect the addition of new quests and notify the user if they turn the option on, of the availability of the new quest. The user can then click on the notification to auto-launch the game without even having to type the game in manually.
4. Perhaps utilizing the reddit api and r/DiscordQuests to fetch the missing info regarding quests. [somewhat implemented]
5. Find a .png via steam CDN or elsewhere, for the game that is being simulated, and make the dummy .exe run with that icon.

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
