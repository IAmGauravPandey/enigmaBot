from PyDictionary import PyDictionary
from typing import Any, Dict, List

def get_dictionary_response(message: Dict[str, str], bot_handler: Any) -> str:
	content = message['content']
	words = content.lower().split()
	dictionary=PyDictionary()
	res = dictionary.meaning(words[2])
	if res != None:
		res = res['Noun']
		ans = ""
		for i in res:
			ans = ans + i + "\n\n"
		return ans
	return "Unable to find meaning :("