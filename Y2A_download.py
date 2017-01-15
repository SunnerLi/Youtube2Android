#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_table import *
from Y2A_IO import *
import os

def printFileCannotBeFound(language):
    """
        Show the Youtube2Android JSON file cannot be found with specific language

        Arg:    language - The language variable
    """
    sentence = ["The .dat file cannot be found, please add the song first.", "找不到歌曲檔案，請先新增歌曲"]
    print sentence[language]

def showNoDownloadSong(songs, language):
    """
        Show the songs which didn't download

        Arg:    songs       - The song JSON object
                language    - The language variable
    """
    sentence = ["The following song didn't download correctly\nPlease check the list or remove them", "下面這些歌曲未成功下載，請確認未下載的歌曲以方便移除他們！"]
    print sentence[language]
    printTableOnlyX(songs, language)

def downloadSongs(songs, language, __file=JSONFileName):
    """
        Download the songs whose status are 'X'
        If there's song didn't download, it will remind at last

        Arg:    songs       - The song JSON object
                language    - The language variable
                __file      - The name of Youtube2Android JSON file
    """
    if not __file in os.listdir('.'):
        printFileCannotBeFound(language)
    else:
        songs = readFile()
        for i in range(len(songs["song"])):
            if songs["song"][i]["status"] == 'X':
                # Download the music and construct the directory list
                originDir = os.listdir(musicFileAddress)
                command = 'youtube-dl -x --audio-format "mp3" ' + songs["song"][i]['url']
                os.system(command)
                afterDir = os.listdir(musicFileAddress)
            
                # Revised the json
                fileName = diff(afterDir, originDir)
                if not fileName == None:
                    songs["song"][i]['name'] = removeHashCodeAndShrink(fileName)[:55]
                    songs["song"][i]['status'] = "O"

        # Show the songs which didn't download
        isSongNoDownload = False
        for song in songs["song"]:
            if song["status"] == 'X':
                isSongNoDownload = True
        if isSongNoDownload == True:
            showNoDownloadSong(songs, language)
        saveFile(songs)

def removeHashCodeAndShrink(__string, maxLength=40):
    """
        Remove the hash code generated by youtube-dl and shrink the size of the name

        Arg:    __string    - The name you want to progress
                maxLength   - The max limit of the name
    """
    for i in range(len(__string)-1, 0, -1):
        if __string[i] == '-':
            __string = (__string[:i])[:maxLength] + __string[-4:]
            return str(__string).decode('string_escape')