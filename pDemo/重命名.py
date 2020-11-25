# coding=utf-8
# -*- coding: utf-8 -*-
import os
import sys

#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'


def updateName(rootDir,sou, des):
    if rootDir.endswith("\\"):
        rootDir= rootDir[0:-1]
    files = os.listdir(rootDir)
    local = os.path.basename(sys.argv[0])
    for i in files:
        if i == local:
            continue
        filePath = os.path.join(rootDir, i+"\\")
        if os.path.isdir(filePath):
            updateName(filePath,sou, des)
            if filePath.find(sou) >= 0:
                newFilePath = rootDir+'\\'+i.replace(sou, des)
                os.rename(filePath, newFilePath)
            continue

        ext = os.path.splitext(i)[-1]
        arr = ['.cs','.json','.txt','.tt','.sln','.csproj','.props','.targets','.yml','.bat','.sh','.md']
        if ext not in arr:
            continue
        filePath = rootDir+'\\'+i
        file_data = ""
        with open(filePath, 'r', encoding='utf-8', errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                if sou in line:
                    line = line.replace(sou, des)
                file_data += line
        with open(filePath, 'w', encoding='utf-8', errors="ignore") as f:
            f.write(file_data)
        if filePath.find(sou) >= 0:
            newFilePath = rootDir+'\\'+i.replace(sou, des)
            os.rename(filePath, newFilePath)

if __name__ == "__main__":
    updateName( os.getcwd(),"Blog.Core", "Hw.Core")
