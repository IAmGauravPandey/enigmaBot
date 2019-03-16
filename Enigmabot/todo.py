import sys
import os
sys.path.insert(0, os.getcwd())

import copy
import importlib
import random
from math import log10, floor

import re
from converter import utils
from typing import Any, Dict, List


def get_todo_response(message: Dict[str, str], bot_handler: Any) -> str:
    content = message["content"]
    words = content.split()
    if words[2] == "start":
        bot_handler.storage.put("list", "")
        return "todo initialized"
    if words[2] == "list":
        res = bot_handler.storage.get("list")
        val = ""
        values = res.split("~")
        i = 1
        for temp in values:
            val = val + str(i) + ". " + temp + "\n"
            i += 1
        return val
    elif words[2] == "add":
        res = bot_handler.storage.get("list")
        res = res + " ".join(words[3::]) + "~"
        bot_handler.storage.put("list", res)
        return "Added to list."
    elif words[2] == "remove":
        index = int(words[3])
        res = bot_handler.storage.get("list")
        val = ""
        values = res.split("~")
        i = 1
        for temp in values:
            if i != index:
                val = val + temp + "~"
            i += 1
        bot_handler.storage.put("list", val)
        return "Removed from list."
