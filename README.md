<h1 align="center"> Enigma - Bot </h1> <br>
<p align="center">
<img src = "https://github.com/gauravpandey1998/enigmaBot/blob/master/enigma.jpg" height="400px"/>
</p>
Hey Hackers, I'm Enigma, the most feature-rich Zulip Chat Bot built for solving your queries. I was developed by the Team Enigma Rebooted in the HackFest 2k19, the offcial Fest of Department of Computer Science and Engineering, IIT(ISM) Dhanbad.I'm famous for solving various programming queries and, am really good in mind games like Hangman,Memory game and Scrabble.
So? Up for a challenge? Follow the upcoming steps and Voila!

## Features:
   * Chatting
   * Description of a Linux Command
   * SSH a remote user
   * Hacker news on keyword
   * Dictionary based search
   * Mind Games:
     * Hangman
     * scrabble
     * Stone Paper Scissor
     * Mind Game
   * Calculator
   * Live Sports Score
   
## How to Deploy:
   * Create a Zulip Realm
   
   * Goto to settings and create a new generic bot named 'Enigma'. (Settings can be found in dropdown of gear icon present in top right corner of zulip realm)
   
   * Download the zuliprc file for your bot and place it in your home directory as '.zuliprc'.
   
   * Install all the requirements using ``` pip install -r requirements.txt ```
   
   * In ```bot.py``` , change site in ```self.client = zulip.Client [site]("https://chunkzz.zulipchat.com/api/")``` to url of your created zulip realm.Do the same for ```BOT_MAIL variable```
   
   * Run ```bot.py``` using the lastest version of Python. ``` python bot.py ```
   
   * Head over to your created zulip realm and start using the bot.
   
## Screenshots:
