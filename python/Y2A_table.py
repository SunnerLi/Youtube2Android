#!/usr/bin/python
# -*- coding: utf-8 -*-

from Y2A_config import *

def printTable(songs, language):
    """
        Print the song table according to the source JSON object and language variable

        Arg:    songs       - The song JSON object
                language    - The language variable 
    """

    attributes = ""
    if language == ENGLISH:
        print "Song Name".ljust(55) + " | URL".ljust(60) + " | Status\t\t"
        print "-" * 56 + "+" + "-" * 57 + "+" + "-" * 20
        rows = ""
        for i in range(len(songs["song"])):
            rows = rows + songs["song"][i]["name"].ljust(55) + " | " \
                        + songs["song"][i]["url"].ljust(57) + " | "  \
                        + songs["song"][i]["status"] + "\n"
        print rows 
    else:
        print "歌曲名稱".ljust(55) + " | URL".ljust(60) + " | 狀態\t\t"
        print "-" * 52 + "+" + "-" * 59 + "+" + "-" * 20
        rows = ""
        for i in range(len(songs["song"])):
            rows = rows + songs["song"][i]["name"].ljust(51) + " | " \
                        + songs["song"][i]["url"].ljust(57) + " | "  \
                        + songs["song"][i]["status"] + "\n"
        print rows 

def printTableOnlyX(songs, language):
    """
        Print the song table according to the source JSON object and language variable
        The table will only show the songs which didn't download

        Arg:    songs       - The song JSON object
                language    - The language variable 
    """

    attributes = ""
    if language == ENGLISH:
        print "Song Name".ljust(50) + " | URL".ljust(60) + " | Status\t\t"
        print "-" * 51 + "+" + "-" * 57 + "+" + "-" * 20
        rows = ""
        for i in range(len(songs["song"])):
            if songs["song"][i]["status"] == 'X':
                rows = rows + songs["song"][i]["name"].ljust(50) + " | " \
                            + songs["song"][i]["url"].ljust(57) + " | "  \
                            + songs["song"][i]["status"] + "\n"
        print rows 
    else:
        print "歌曲名稱".ljust(50) + " | URL".ljust(60) + " | 狀態\t\t"
        print "-" * 47 + "+" + "-" * 59 + "+" + "-" * 20
        rows = ""
        for i in range(len(songs["song"])):
            if songs["song"][i]["status"] == 'X':
                rows = rows + songs["song"][i]["name"].ljust(46) + " | " \
                            + songs["song"][i]["url"].ljust(57) + " | "  \
                            + songs["song"][i]["status"] + "\n"
        print rows 