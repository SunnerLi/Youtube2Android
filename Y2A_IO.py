#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_config import *
import os
import json

def readFile(file=JSONFileName):
    """
        Read the Youtube2Android JSON file and return the JSON object
        It would revise the status at last

        Arg:    The JSON file name
        Ret:    The JSON object
    """
    songs = {}
    with open(JSONFileName, 'r') as f:
        songs = json.load(f)
    return reviseStatus(songs)

def reviseStatus(songs, maxLength=20):
    """
        Revised the status of each song on the list
        It would save the revised result at last

        Arg:    songs       - The song JSON object
                maxLength   - The max limit of the music name
        Ret:    The revised JSON object
    """
    # Get the revised direction
    revisedDir = os.listdir(musicFileAddress)
    for i in range(len(revisedDir)):
        revisedDir[i] = revisedDir[i][:min(len(revisedDir[i]), maxLength)]
    
    # Update the status
    if not songs == None:
        for i in range(len(songs["song"])):
            if songs["song"][i]["name"][:min(len(songs["song"][i]["name"]), maxLength)] in revisedDir:
                songs["song"][i]["status"] = 'O'
            else:
                print revisedDir
                print songs["song"][i]["name"][:min(len(songs["song"][i]["name"]), maxLength)]
                songs["song"][i]["status"] = 'X'
    saveFile(songs)
    return songs

def saveFile(songs, file=JSONFileName):
    """
        Store the Youtube2Android JSON object to the specific file

        Arg:    songs   - The song JSON object
                file    - The file name of the Youtube2Android JSON file
    """
    with open(JSONFileName, 'w') as f:
        json.dump(songs, f)

def diff(src1, src2):
    """
        Find the different item between the two list

        Arg:    src1 - The first list you want to traversal
                src2 - The second list you want to traversal
        Ret:    The different item or None(If the two list is the same)
    """
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
    """
        Deprecated function
    """
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