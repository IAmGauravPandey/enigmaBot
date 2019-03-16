import sys, os
sys.path.insert(0,os.getcwd())

import copy
import importlib
import random
from math import log10, floor

import re
from converter import utils

from typing import Any, Dict, List

def get_sps_response(message: Dict[str, str], bot_handler: Any) -> str:
	content = message['content']
	words = content.lower().split()
	if words[2] == "start" :
		score = "0" 
		bot_handler.storage.put("score" , score)
		return "Game Starts. Enter Stone/Paper/Scissors. Score : " + score
	else :
		score = bot_handler.storage.get("score") 
		letter = words[2]
		# return letter
		temp = random.randint(1, 3)
		# 1 - Stone , 2 - Paper , 3 - Scissor 
		temp1 = int(score)
		if letter == "stone" :
			if temp == 2 :
				temp1 -= 5 
			elif temp == 3 :
				temp1 += 10 
		elif letter == "paper" :
			if temp == 3 :
				temp1 -= 5 
			elif temp == 1 :
				temp1 += 10
		elif letter == "scissors" :
			if temp == 1 :
				temp1 -= 5 
			elif temp == 2 :
				temp1 += 10
		if temp1 < 0 :
			temp1 = 0 	
		score = str(temp1)
		val = ""
		if temp == 1 :
			val = "Stone" 
		elif temp == 2 :
			val = "Paper" 
		else :
			val = "Scissors" 	
		bot_handler.storage.put("score" , score)
		return "Bot chose " + val + ".... New Score : " + str(temp1)
