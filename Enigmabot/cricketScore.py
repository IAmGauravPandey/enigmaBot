import sys
import os
sys.path.insert(0, os.getcwd())

import requests
import json
from typing import Any, Dict, List

def get_cricketScore_response(message: Dict[str, str], bot_handler: Any) -> str:
    content = message['content']
    words = content.lower().split()
    matches = requests.get(
        'http://cricapi.com/api/matches?apikey=rRjw4YvDDjcXtIj5GAE5wV25fAl1').json()
    res = ""
    i = 0
    for match in matches['matches']:
        unique_id = match['unique_id']
        score = requests.get(
            'http://cricapi.com/api/cricketScore?apikey=rRjw4YvDDjcXtIj5GAE5wV25fAl1&unique_id=' + str(unique_id)).json()
        if 'score' in score:
            res = res + match['date'][0:10:] + "\n" + score['score'] + "\n\n"
            i += 1
        if i == 5:
            break
    return res
