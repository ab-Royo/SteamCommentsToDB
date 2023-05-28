# -*- coding: utf-8 -*-
"""
@File    : utils.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""
import json

import requests

import LogMarker

import re

'''
    功能简述: utils 为通用小工具库, 内部存放一些通用方法, 主要负责读取配置文件, 生成快速方法并精确返回需要的数据
    使用 class 对功能大类进行分离, 可单独引用, 将不必要的一些变量进行私有化处理
'''

class UserInfo:
    @staticmethod
    # TODO: 静态方法, 读取 "./config/info.json" 中的 userID 并返回
    def userID():
        with open("./config/info.json", encoding="utf-8", mode="r") as __doc:
            __info = __doc.read()
            __info = json.loads(__info)
            __userInfo = __info["userID"]
            if __userInfo == "":
                print(LogMarker.error() + "info.json 文件中 userID 属性为空!")
                pass
            else:
                return __userInfo

# TODO: 读取 "./config/settings.json" 下的配置
class Settings:
    @staticmethod
    def ProxyStatus():
        # Light: (注) 返回的数据类型为 bool
        with open("./config/settings.json", encoding="utf-8", mode="r") as __settings:
            __settings = __settings.read()
            __settings = json.loads(__settings)
            __ProxyStatus = __settings["Proxy"]["Enable"]
            if __ProxyStatus == "":
                print(LogMarker.error() + "settings.json 文件中 Enable 属性为空!")
                pass
            else:
                return __ProxyStatus

    @staticmethod
    def ProxyMode():
        with open("./config/settings.json", encoding="utf-8", mode="r") as __settings:
            __settings = __settings.read()
            __settings = json.loads(__settings)
            __ProxyMode = __settings["Proxy"]["ProxyMode"]
            if __ProxyMode == "":
                print(LogMarker.error() + "settings.json 文件中 ProxyMode 属性为空!")
                pass
            else:
                return __ProxyMode

    @staticmethod
    def ProxyURL():
        with open("./config/settings.json", encoding="utf-8", mode="r") as __settings:
            __settings = __settings.read()
            __settings = json.loads(__settings)
            __ProxyURL = __settings["Proxy"]["ProxyURL"]
            if __ProxyURL == "":
                print(LogMarker.error() + "settings.json 文件中 ProxyURL 属性为空!")
            else:
                return __ProxyURL

# steam ID 转换
class SteamTools:
    @staticmethod
    def IDTransformer(URL):
        # 代理状态
        Enable = Settings.ProxyStatus()
        ProxyMode = Settings.ProxyMode()
        ProxyURL = Settings.ProxyURL()

        # 将 URL 统一转换
        url = str(URL).replace("https://steamcommunity.com/id/", "").replace("https://steamcommunity.com/profiles/", "")

        if Enable:
            __transURL = 'https://avi12.com/api/steam-id-finder?id={}'.format(url)
            __Headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                }
            __Proxy = proxy = {ProxyMode: ProxyURL}   # 拼接 proxy
            __data = requests.get(__transURL, headers=__Headers, proxies=proxy)
            __data = __data.text
            __userInfo = json.loads(__data)
            __SteamID = __userInfo["steamid"]

        # TODO: 建议处于全局代理模式或处于国际网络(全局)环境下使用
        else:
            __transURL = 'https://avi12.com/api/steam-id-finder?id={}'.format(url)
            __Headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                }
            __data = requests.get(__transURL, headers=__Headers)
            __data = __data.text
            __userInfo = json.loads(__data)
            __SteamID = __userInfo["steamid"]
        return __SteamID



if __name__ == "__main__":
    # info
    print("SteamID: " + UserInfo.userID())
    # settings
    print("ProxyStatus: " + str(Settings.ProxyStatus()))
    print("ProxyMode: " + str(Settings.ProxyMode()))
    print("ProxyURL: " + str(Settings.ProxyURL()))
