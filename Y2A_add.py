#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_IO import *
import os

def printRemind(language):
    """
        Print the explaination of this progress with the specific language

        Arg:    language - The language variable
    """
    sentence = ""
    if language == ENGLISH:
        sentence = "Input the URL\ntype -1 while you want to end adding"
    else:
        sentence = "輸入歌曲的youtube網址\n如果你想結束新增請輸入-1"
    print sentence

def addNewSong(songs, language, __file="musicFile1.dat"):
    """
        Add new song to the song JSON object
        The result will be stored into the JSON file at last

        Arg:    songs       - The song JSON object
                language    - The language object
                __file      - The name of Youtube2Android JSON file
    """
    if not __file in os.listdir('.'):
        songs = {"language": CHINESE, "song": []}
    else:
        songs = readFile()

    while True:
        printRemind(language)
        choose = raw_input()
        if choose == "-1":
            break
        else:
            song = {"url": choose, "name": "null", "status": 'X'}
            songs["song"].append(song)
    saveFile(songs)