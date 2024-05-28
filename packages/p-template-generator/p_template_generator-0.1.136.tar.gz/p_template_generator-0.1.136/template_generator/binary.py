import sys
import os
import subprocess
import json
import random
from pathlib import Path
import shutil
import zipfile
import stat
import requests
import hashlib
import logging

def getOssResource(rootDir, url, md5, name):
    localFile = os.path.join(rootDir, name)
    localFileIsRemote = False
    if os.path.exists(localFile):
        with open(localFile, 'rb') as fp:
            file_data = fp.read()
            fp.close()
        file_md5 = hashlib.md5(file_data).hexdigest()
        if file_md5 == md5:
            localFileIsRemote = True

    if localFileIsRemote == False: #download
        if os.path.exists(localFile):
            os.remove(localFile)
        s = requests.session()
        s.keep_alive = False
        print(f"download {url} ")
        file = s.get(url, verify=False)
        with open(localFile, "wb") as c:
            c.write(file.content)
            c.close()
        s.close()
        fname = name[0:name.index(".")]
        fext = name[name.index("."):]
        unzipDir = os.path.join(rootDir, fname)
        if os.path.exists(unzipDir):
            shutil.rmtree(unzipDir)
        print(f"unzip {url} -> {unzipDir}")
        return True
    return False
    
def readDirChecksum(dir):
    f = os.path.join(dir, "checksum.txt")
    txt = ""
    if os.path.exists(f):
        with open(f, "r", encoding="UTF-8") as f1:
            txt = f1.read()
            f1.close()
    return txt
        
def writeDirChecksum(dir, zipFile):
    if os.path.exists(zipFile) == False:
        return
    with open(zipFile, 'rb') as fp:
        fdata = fp.read()
        fp.close()
    fmd5 = hashlib.md5(fdata).hexdigest()

    with open(os.path.join(dir, "checksum.txt"), "w") as f:
        f.write(fmd5)
        f.close()

def checkFileMd5(rootDir):
    data = {
        # "fonts.zip.py" : "b1f190ba1cea49177eccde2eb2a6cb13",
        # "subEffect.zip.py" : "08651251e4351fd8cd5829b2ef65a8b9"
    }
    for key in data:
        fpath = os.path.join(rootDir, key)
        if os.path.exists(fpath):
            with open(fpath, 'rb') as fp:
                fdata = fp.read()
                fp.close()
            fmd5 = hashlib.md5(fdata).hexdigest()
            fname = key[0:key.index(".")]
            fext = key[key.index("."):]
            fdirpath = os.path.join(rootDir, fname)
            if os.path.exists(fdirpath) and fmd5 != readDirChecksum(fdirpath):
                logging.info(f"remove old {fdirpath}")
                shutil.rmtree(fdirpath)
                
def updateBin(rootDir):
    getOssResource(rootDir, "https://m.mecordai.com/res/ffmpeg.zip", "a9e6b05ac70f6416d5629c07793b4fcf", "ffmpeg.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/randomTemplates_20230625.zip", "e0cf7eaed4a90d59fe82f41b02f3d17e", "randomTemplates.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/subEffect.zip", "08651251e4351fd8cd5829b2ef65a8b9", "subEffect.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/fonts.zip", "b1f190ba1cea49177eccde2eb2a6cb13", "fonts.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/effect_text_20240508.zip", "31e34b11d56b3cef33abec94524133a6", "effect_text.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/effect_transition_202405051915.zip", "397561cd057f278efb77b0f6c9d0b377", "effect_transition.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/effect_video.zip", "4d9cc256c96e25c74308b6c2e1de4718", "effect_video.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/effect_blend.zip", "1d49bdf8e56bf8b2a54dfef1f70af83b", "effect_blend.zip.py")
    getOssResource(rootDir, "https://m.mecordai.com/res/effect_sticker.zip", "c060ad3c6891735cbf2798e722c25f24", "effect_sticker.zip.py")
    if sys.platform == "win32":
        getOssResource(rootDir, "https://m.mecordai.com/res/skymedia_win_20240528.zip", "2b182b488ab01bd36f5513405a46936d", "skymedia.zip.py") == True
    elif sys.platform == "linux":
        getOssResource(rootDir, "https://p-template-hk.oss-cn-hongkong.aliyuncs.com/res/skymedia_linux.zip", "6c52e792fb65e16aa1f140c41650a877", "skymedia.zip.py")
    elif sys.platform == "darwin":
        getOssResource(rootDir, "https://m.mecordai.com/res/skymedia_darwin_20240528.zip", "df49823b186515d3f6fc6ef57e090811", "skymedia.zip.py")
    checkFileMd5(rootDir)

    extra_skymedia = False
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            if file.find(".") <= 0:
                continue
            name = file[0:file.index(".")]
            ext = file[file.index("."):]
            if ext == ".zip.py" and os.path.exists(os.path.join(root, name)) == False:
                print(f"unzip {os.path.join(root, name)}")
                with zipfile.ZipFile(os.path.join(root, file), "r") as zipf:
                    zipf.extractall(os.path.join(root, name))
                writeDirChecksum(os.path.join(root, name), os.path.join(root, file))
                if "skymedia" in name:
                    extra_skymedia = True
        if root != files:
            break
    if extra_skymedia:
        platform = ""
        if sys.platform == "win32":
            platform = "win"
        elif sys.platform == "linux":
            platform = "linux"
        elif sys.platform == "darwin":
            platform = "darwin"
        def cp_skymedia_res(platform, s, t):
            src = os.path.join(rootDir, s)
            dst = os.path.join(rootDir, "skymedia",platform,"effects",t)
            shutil.copytree(src, dst)
        effects = os.path.join(rootDir, "skymedia",platform,"effects")
        if os.path.exists(effects):
            shutil.rmtree(effects)
        cp_skymedia_res(platform, "effect_text", "text")
        cp_skymedia_res(platform, "effect_transition", "transition")
        cp_skymedia_res(platform, "effect_video", "video")
        cp_skymedia_res(platform, "effect_sticker", "sticker")
        cp_skymedia_res(platform, "effect_blend", "blend")

def initRes(downloadPath):
    if os.path.exists(downloadPath) == False:
        os.makedirs(downloadPath)
    updateBin(downloadPath)
    
def realBinPath(searchPath):
    binDir = ""
    if len(searchPath) <= 0 or os.path.exists(searchPath) == False:
        binDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
        if os.path.exists(binDir) == False:
            os.makedirs(binDir)
        updateBin(binDir)
    else:
        binDir = searchPath
    return binDir

def ffmpegPath(searchPath):
    return os.path.join(realBinPath(searchPath), "ffmpeg")
def skymediaPath(searchPath):
    return os.path.join(realBinPath(searchPath), "skymedia")
def subEffectPath(searchPath):
    return os.path.join(realBinPath(searchPath), "subEffect")
def randomEffectPath(searchPath):
    return os.path.join(realBinPath(searchPath), "randomTemplates")
def fontPath(searchPath):
    return os.path.join(realBinPath(searchPath), "fonts")
