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
                "status": "X"
            },
"""

songs = {
    "language": "chinese",
    "song":
        [
            {
                "name": "song name 1",
                "url": "https://www.youtube.com/watch?v=EYl714wFeJM",
                "status": "not finish"
            },
            {
                "name": "song name 2",
                "url": "https://www.youtube.com/watch?v=3UuaQ-7hNiQ",
                "status": "X"
            }
        ]
    }

language = -1
ENGLISH = 0
CHINESE = 1

def readFile(file="musicFile1.dat"):
    global songs
    with open("musicFile1.dat", 'r') as f:
        songs = json.load(f)
    reviseStatus()

def reviseStatus(maxLength=20):
    global songs

    # Get the revised direction
    revisedDir = os.listdir('.')
    for i in range(len(revisedDir)):
        revisedDir[i] = revisedDir[i][:min(len(revisedDir[i]), maxLength)]
    
    # Update the status
    if not songs == None:
        for i in range(len(songs["song"])):
            if songs["song"][i]["name"][:min(len(songs["song"][i]["name"]), maxLength)] in revisedDir:
                songs["song"][i]["status"] = 'O'
            else:
                songs["song"][i]["status"] = 'X'
    saveFile()

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

<<<<<<< HEAD
def removeHashCodeAndShrink(__string, maxLength=40):
    for i in range(len(__string)-1, 0, -1):
        if __string[i] == '-':
            __string = (__string[:i])[:maxLength] + __string[-4:]
=======
def removeHashCode(__string):
    for i in range(len(__string)-1, 0, -1):
        if __string[i] == '-':
            __string = __string[:i] + __string[-4:]
>>>>>>> 2529bb6b3b2f918c1d5ad8baf9a216ee46445244
            return str(__string).decode('string_escape')

def printTable():
    global songs
<<<<<<< HEAD
    global language

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

def printTableOnlyX():
    global songs
    global language

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
    
    

def printMainDescription():
    global language
    script = ""
    if language == ENGLISH:
        script = """
        =================================
        The Youtube2Android python script
        =================================

        Please type the index of operator you want:
        [1]: show the information of songs
        [2]: add the new song
        [3]: remove the song
        [4]: download the songs
        [5]: exit

        """
    else:
        script = """
        =================================
            Youtube2Android python 腳本
        =================================

        請輸入你想要的操作代碼：
        [1]： 秀出資訊
        [2]： 新增歌曲
        [3]： 移除歌曲
        [4]： 下載歌曲
        [5]： 退出

        """
    print script



def showInformation(__file="musicFile1.dat"):
    """
        The function of show information
    """
    # Define the function first
    def printFileCannotBeFound():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "The .dat file cannot be found, please add the song first."
        else:
            sentence = "找不到歌曲檔案，請先新增歌曲"
        print sentence

    def printSubQuestionDescription():
        global language
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

    def printInvalidChoose():
        sentence = ""
        if language == ENGLISH:
            sentence = "Invalid choose"
        else:
            sentence = "輸入錯誤，請再次確認..."
        print sentence

    # Define the process next
    if not __file in os.listdir('.'):
        printFileCannotBeFound()
    else:
        readFile()
        printSubQuestionDescription()
        choose = raw_input()
        if int(choose) == 1:
            printTable()
        elif int(choose) == 2:
            printTableOnlyX()
        else:
            printInvalidChoose()

def addNewSong(__file="musicFile1.dat"):
    global songs

    # Define the function first
    def printRemind():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "Input the URL\ntype -1 while you want to end adding"
        else:
            sentence = "輸入歌曲的youtube網址\n如果你想結束新增請輸入-1"
        print sentence

    # Define the process next
    if not __file in os.listdir('.'):
        songs = {"language": CHINESE, "song": []}
    else:
        readFile()

    while True:
        printRemind()
        choose = raw_input()
        if choose == "-1":
            break
        else:
            song = {"url": choose, "name": "null", "status": 'X'}
            songs["song"].append(song)
    saveFile()

def removeSong(__file="musicFile1.dat"):
    global songs

    # Define the function first
    def printFileCannotBeFound():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "The .dat file cannot be found, nothing to remove"
        else:
            sentence = "找不到歌曲檔案，沒有歌曲可以移除"
        print sentence

    def printRemind():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "Input the URL\ntype -1 while you want to end removing"
        else:
            sentence = "輸入歌曲的youtube網址\n如果你想結束移除請輸入-1"
        print sentence

    def printSongNoFound():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "The song no found, please check if the song exist in the list"
        else:
            sentence = "找不到此歌曲，請確認歌曲是否在清單中..."
        print sentence

    # Define the process next
    if not __file in os.listdir('.'):
        printFileCannotBeFound()
    else:
        readFile()
        while True:
            printRemind()
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
                    printSongNoFound()
        saveFile()

def downloadSongs(__file="musicFile1.dat"):
    global language

    # Define the function first
    def printFileCannotBeFound():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "The .dat file cannot be found, please add the song first."
        else:
            sentence = "找不到歌曲檔案，請先新增歌曲"
        print sentence

    def showNoDownloadSong():
        global language
        sentence = ""
        if language == ENGLISH:
            sentence = "The following song didn't download correctly\nPlease check the list or remove them"
        else:
            sentence = "下面這些歌曲未成功下載，請確認未下載的歌曲以方便移除他們！"
        print sentence
        printTableOnlyX()


    # Define the process next
    if not __file in os.listdir('.'):
        printFileCannotBeFound()
    else:
        readFile()
        for i in range(len(songs["song"])):
            if songs["song"][i]["status"] == 'X':
                # Download the music and construct the directory list
                originDir = os.listdir('.')
                command = 'youtube-dl -x --audio-format "mp3" ' + songs["song"][i]['url']
                os.system(command)
                afterDir = os.listdir('.')
            
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
            showNoDownloadSong()
        saveFile()

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
        printMainDescription()
        choose = raw_input()
        if int(choose) == 1:
            showInformation()
        elif int(choose) == 2:
            addNewSong()
        elif int(choose) == 3:
            removeSong()
        elif int(choose) == 4:
            downloadSongs()
        elif int(choose) == 5:
            break


