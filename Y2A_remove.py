#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_config import *
from Y2A_IO import *
import os

def printFileCannotBeFound(language):
    """
        Show the Youtube2Android JSON file cannot be found with specific language

        Arg:    language - The language variable
    """
    sentence = ["The .dat file cannot be found, nothing to remove", "找不到歌曲檔案，沒有歌曲可以移除"]
    print sentence[language]

def printRemind(language):
    """
        Print the explaination of this progress with the specific language

        Arg:    language - The language variable
    """
    sentence = ["Input the URL\ntype -1 while you want to end removing", "輸入歌曲的youtube網址\n如果你想結束移除請輸入-1"]
    print sentence[language]

def printSongNoFound(language):
    """
        Tell the user the specific song cannot found with the specific language

        Arg:    language - The language variable
    """
    sentence = ["The song no found, please check if the song exist in the list", "找不到此歌曲，請確認歌曲是否在清單中..."]
    print sentence[language]

def removeSong(songs, language, __file="musicFile1.dat"):
    """
        Remove the specific song toward the song JSON object
        The removed result will be stored into the Youtube2Android JSON file

        Arg:    songs       - The song JSON object
                language    - The language object
                __file      - The name of Youtube2Android JSON file
    """
    if not __file in os.listdir('.'):
        printFileCannotBeFound(language)
    else:
        songs = readFile()
        while True:
            printRemind(language)
            choose = raw_input()
            if choose == "-1":
                break
            else:
                isFound = False
                for i in range(len(songs["song"])):
                    if songs["song"][i]["name"] == choose or songs["song"][i]["url"] == choose:
                        songs["song"].remove(songs["song"][i])
                        isFound = True
                        break
                if isFound == True:
                    break
                else:
                    printSongNoFound(language)
        saveFile(songs)