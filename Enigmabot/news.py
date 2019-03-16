import sys, os
sys.path.insert(0,os.getcwd())

import requests
import json
from typing import Any,Dict,List

def get_news_response(message: Dict[str, str], bot_handler: Any) -> str:
	content = message['content']
	words = content.lower().split()
	articles = requests.get('https://newsapi.org/v2/everything?q=' + words[2] + '&apiKey=142ba11e03d74ba38f859c785eee017f').json()
	res = "" 
	i = 1
	for article in articles['articles'] :
		res = res + article['title'] + "\n" + article['url'] + "\n\n"
		i += 1
		if i == 5 :
			break  
	return res