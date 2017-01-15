#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_download import *
from Y2A_showInfo import *
from Y2A_remove import *
from Y2A_add import *
from Y2A_IO import *

import os
import json
import sys

# Set up the utf-8 coding function
reload(sys)  
sys.setdefaultencoding('utf8')

# The songs JSON object
songs = {
    "language": "chinese",
    "song":
        [
        ]
    }

# Language variable
language = -1

if __name__ == "__main__":
    # Check the english setting
    if "musicFile1.dat" in os.listdir('.'):
         readFile()
    if not songs == None:
        if songs["language"] == "english":
            language = ENGLISH
        else:
            language = CHINESE

    # Working
    while True:
        print script[language]
        choose = raw_input()
        if int(choose) == 1:
            showInformation(songs, language)
        elif int(choose) == 2:
            addNewSong(songs, language)
        elif int(choose) == 3:
            removeSong(songs, language)
        elif int(choose) == 4:
            downloadSongs(songs, language)
        elif int(choose) == 5:
            break
