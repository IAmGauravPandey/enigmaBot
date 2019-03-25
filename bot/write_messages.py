#!/usr/bin/env python3

import zulip
import sys
import pathlib

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="~/zuliprc")

# Print every message the current user would receive
# This is a blocking call that will run forever
#f= open("messages.txt","w")
client.call_on_each_message(lambda msg: pathlib.Path('messages.txt').write_text(msg['content']))
