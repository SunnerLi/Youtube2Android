#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_config import *
from Y2A_table import *
from Y2A_IO import *
import os

def printFileCannotBeFound(language):
    """
        Show the Youtube2Android JSON file cannot be found with specific language

        Arg:    language - The language variable
    """
    sentence = ""
    if language == ENGLISH:
        sentence = "The .dat file cannot be found, please add the song first."
    else:
        sentence = "找不到歌曲檔案，請先新增歌曲"
    print sentence

def printSubQuestionDescription(language):
    """
        Show the description of the sub-question with the specific language

        Arg:    language - The language variable
    """
    sentence = ""
    if language == ENGLISH:
        sentence = """
        Which song you want to see?

        [1]: The whole songs
        [2]: The song with status 'X'

        """
    else:
        sentence = """
        你想看哪些歌曲的資訊呢

        [1]：所有歌曲
        [2]：未下載完成的歌曲

        """
    print sentence

def printInvalidChoose(language):
    """
        Show the user that he/she key-in the invalid symbol with the specific language

        Arg:    language - The language variable
    """
    sentence = ["Invalid choose", "輸入錯誤，請再次確認..."]
    print sentence[language]

def showInformation(songs, language, __file=JSONFileName):
    """
        The function of show information

        Arg:    songs       - The song JSON object
                language    - The language object
                __file      - The name of Youtube2Android JSON file
    """  
    if not __file in os.listdir('.'):
        printFileCannotBeFound(language)
    else:
        songs = readFile()
        printSubQuestionDescription(language)
        choose = raw_input()
        if int(choose) == 1:
            printTable(songs, language)
        elif int(choose) == 2:
            printTableOnlyX(songs, language)
        else:
            printInvalidChoose()