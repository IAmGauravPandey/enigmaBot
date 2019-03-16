import sys, os
sys.path.insert(0,os.getcwd())

import copy
import importlib
import random
from math import log10, floor

import re
from converter import utils

from typing import Any, Dict, List


def get_calculator_response(message: Dict[str, str], bot_handler: Any) -> str:
	content = message['content']
	words = content.lower().split()
	if words[3] == "+" :
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp + temp1 
		return str( temp ) 
	elif words[3] == "-" :
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp - temp1 
		return str( temp )
	elif words[3] == "*" :
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp * temp1 
		return str( temp )
	elif words[3] == "/" :
		if words[4] == "0":
			return "Division by zero."
		temp = float(words[2]) 
		temp1 = float(words[4])
		temp = temp / temp1 
		return str( temp )
	else :
		return "Under Construction"