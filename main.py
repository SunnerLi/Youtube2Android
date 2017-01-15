#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

"""
{
                "name": "song name 1",
                "url": "https://www.youtube.com/watch?v=EYl714wFeJM",
                "status": "not finish"
            },
"""

songs = {"song":
        [
            {
                "name": "song name 1",
                "url": "https://www.youtube.com/watch?v=EYl714wFeJM",
                "status": "not finish"
            },
            {
                "name": "song name 2",
                "url": "https://www.youtube.com/watch?v=3UuaQ-7hNiQ",
                "status": "not finish"
            }
        ]
    }

def readFile(file="musicFile1.dat"):
    with open("musicFile1.dat", 'r') as f:
        songs = json.load(f)
    return songs

def saveFile(file="musicFile1.dat"):
    global songs
    with open("musicFile1.dat", 'w') as f:
        json.dump(songs, f)

def diff(src1, src2):
    if len(src1) == len(src2):
        return None
    for item1 in src1:
        isExist = False
        for item2 in src2:
            if item1 == item2:
                isExist = True
        if isExist == False:
            return item1

def download():
    global songs
    for i in range(len(songs["song"])):
        # Download the music and construct the directory list
        originDir = os.listdir('.')
        command = 'youtube-dl -x --audio-format "mp3" ' + songs["song"][i]['url']
        os.system(command)
        afterDir = os.listdir('.')

        # Revised the json
        fileName = diff(afterDir, originDir)
        if not fileName == None:
            songs["song"][i]['name'] = removeHashCode(fileName)
            songs["song"][i]['status'] = "Done"

def removeHashCode(__string):
    for i in range(len(__string)-1, 0, -1):
        if __string[i] == '-':
            __string = __string[:i] + __string[-4:]
            return str(__string).decode('string_escape')

def printTable():
    global songs

    attributes = "Song Name".ljust(50) + " | URL".ljust(60) + " | Status\t\t"
    print attributes
    print "-" * 51 + "+" + "-" * 57 + "+" + "-" * 20
    rows = ""
    for i in range(len(songs["song"])):
        rows = rows + songs["song"][i]["name"].ljust(50) + " | " \
                    + songs["song"][i]["url"].ljust(57) + " | "  \
                    + songs["song"][i]["status"] + "\n"
    print rows 
        
#readFile()
download()
printTable()