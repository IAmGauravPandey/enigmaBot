import sys, os, zulip
sys.path.insert(0,os.getcwd())

from typing import Any, Dict
from imdbpie import Imdb
import lyricwikia
from weather import Weather

import utils, sps, mindGame, hangman, scrabble, todo, calculator, news, currency, cricketScore, dictionary
from wit import Wit
client = Wit('VMPD5FWPJO6QB7XVP5OKWR4TMHJFKZ75')

class EnigmaBot(object):
    '''
    A docstring documenting this bot.
    '''
    def usage(self):
        return '''Built with Python and Zulip API, Enigma Bot is the most feature rich Zulip chat bot for Programmers and Hackers.'''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        results = []
        query = ""
        print(message["content"])
        if message["content"] == "" or message["content"] == "help":
            results.append(utils.HELP_MESSAGE)

        data = message["content"].split()
        if(data[0] != "Enigma"):
        	data.insert(0,"Enigma")
        	message["content"] = "Enigma " + message["content"]
        if(len(data) >= 2):
            query = data[1]

        addData = ''
        if data.__len__() > 3:
            addData = data[3]

        if query == "man":
            results.append(self.query_man(data[2]))
        elif query == "ssh":
            dataTemp = data[5::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_ssh(data[2],data[3],data[4],dataTemp))
        elif query == "sps":
            results.append(sps.get_sps_response(message, bot_handler))
        elif query == "mind-game":
        	results.append(mindGame.get_mindGame_response(message,bot_handler))
        elif query == "hangman":
        	results.append(hangman.get_response(message,bot_handler))
        elif query == "scrabble":
        	results.append(scrabble.get_response(message,bot_handler))
        elif query == "todo":
        	results.append(todo.get_todo_response(message,bot_handler))
        elif query == "calculator":
            results.append(calculator.get_calculator_response(message,bot_handler))
        elif query == "news":
            results.append(news.get_news_response(message,bot_handler))
        elif query == "dictionary":
            results.append(dictionary.get_dictionary_response(message,bot_handler))
        elif query == "cricket":
            results.append(cricketScore.get_cricketScore_response(message,bot_handler))
        elif query == "help":
            results.append(utils.HELP_MESSAGE)
        else:
            dataTemp = data[1::]
            dataTemp = " ".join(dataTemp)
            print(dataTemp)
            witAnalysis = client.message(dataTemp)
            print(witAnalysis)
            temp = witAnalysis['entities']
            if temp.__len__() == 0:
                results.append('Hey, Sorry, Didn\'t get You. Try "@Enigma help" to get detailed help ')
            else:
                trait = witAnalysis['entities']['intent'][0]['value']
                if   trait == "hello":
                    results.append("Hello there, I am Enigma. Let's Start Hacking !!!! :)")
                elif trait == "bye":
                    results.append("Good Bye. I hope you liked me :)")
                elif trait == "add-todo":
                    results.append('To add a todo make a query as follows "@Enigma todo add <task to add here>"')
                elif trait == "remove-todo":
                    results.append('To remove a todo make a query as follows "@Enigma todo remove <id of task to remove>"')
                elif trait == "ssh":
                    results.append('Want to connect to ssh a remote server ? Make a query as follows "@Enigma ssh <user_name> <server_ip> <password> <command>')
                elif trait == "man":
                    results.append('Need some help over usage of command ? make a query as follows "@Enigma man <command>')
                elif trait == "calculator":
                    results.append('To start a calculator make a query as follows "@Enigma calculator <computation_to_solve>')
                elif trait == "help":
                    results.append('Struck somewhere? Try "@Enigma help" to get detailed help about bot')
                elif trait == "list-todo":
                    results.append('To get list of all todos make a query as follows "@Enigma todo list"')
                elif trait == "scrabble":
                    results.append('Wanna play Scrabble? You\'re just a query away. Type "@Enigma scrabble start" to start game')
                elif trait == "sps":
                    results.append('Wanna play Stone Paper Scissor? You\'re just a query away. Type "@Enigma sps start" to start game')
                elif trait == "hangman":
                    results.append('Can you beat me in Hangman? You\'re just a query away. Type "@Enigma hangman start" to start game')
                elif trait == "memory-game":
                    results.append('Sharpen your memory by playing some memeory games type "@Enigma memory-game" to start game')
                elif trait == "news":
                    results.append('Get latest news from around the globe just type "@Enigma news <keyword>"')
                elif trait == "cricket":
                    results.append('How about some Cricket huh? Type "@Enigma cricket" to get live scores.')


        new_content = ''
        for idx, result in enumerate(results, 1):
            new_content += ((str(idx)) if len(results) > 1 else '') + result + '\n'

        bot_handler.send_reply(message, new_content)

    def query_man(self, command):

        os.system("man " + command + " > man.txt")
        file = open("man.txt","r")
        return file.read()

    def query_ssh(self,user,server,password, command):

        command = "sshpass -p " + password + " ssh " + user + "@" + server + ' "' + command +  '" > output.txt 2>  error.txt'
        os.system(command)
        output = open("output.txt","r")
        error = open("error.txt","r")

        return output.read() + " " + error.read()

handler_class = EnigmaBot
