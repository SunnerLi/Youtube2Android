# Simple script written by SunnerLi in 2016/06

# 創建工作資料夾
downloadFolder="temp"
musicFolder="sunnerMusic"
folderName=${downloadFolder}/${musicFolder}
if [ ! -d "$folderName" ]; then
	mkdir -p ${folderName}
fi
musicTXTDir=$(pwd)/musicPath.txt
cd ${folderName}

# 下載所有音樂
while read path
do
	youtube-dl -x --audio-format "mp3" ${path}
	echo "!"
done < ${musicTXTDir}

# 送入手機
cd ../..
adb push ${folderName}/. /storage/emulated/0/Music

# 刪除暫存檔
rm -r ${downloadFolder}
