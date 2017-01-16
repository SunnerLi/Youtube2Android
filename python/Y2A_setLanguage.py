#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_IO import *

def setLanguage(songs, language):
    """
        Set the language about this program

        Arg:    songs       - The song JSON object
                language    - The language variable
    """
    # Print the question
    sentence = ""
    if language == ENGLISH:
        sentence = """
            Which language do you want to set?

            [1]: English
            [2]: Chinese
        """
    else:
        sentence = """
            你想要設定成哪一種語言？

            [1]：英文
            [2]：中文
        """
    print sentence

    # Get the choice of the user
    choose = raw_input()
    if choose == '1':
        songs["language"] = "english"
    elif choose == '2':
        songs["language"] = "chinese"
    else:
        if language == ENGLISH:
            print "Invalid language index"
        else:
            print "你輸入了一個錯的語言代碼..."
    saveFile(songs)