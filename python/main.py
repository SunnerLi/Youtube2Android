#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_setLanguage import *
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
    while True:
        # Check the english setting
        if "musicFile1.dat" in os.listdir('.'):
             songs = readFile()
        if not songs == None:
            if songs["language"] == "english":
                language = ENGLISH
            else:
                language = CHINESE

        # Ask the question
        print script[language]
        choose = raw_input()
        if choose == "1":
            showInformation(songs, language)
        elif choose == "2":
            addNewSong(songs, language)
        elif choose == "3":
            removeSong(songs, language)
        elif choose == "4":
            downloadSongs(songs, language)
        elif choose == "5":
            setLanguage(songs, language)
        elif choose == "6":
            os.system("adb push " + musicFileAddress + "/. /storage/emulated/0/Music")
        elif choose == "7":
            break
