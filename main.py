# -*- coding: utf-8 -*-
"""
@File    : main.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""
import time

from lxml import html

import requests
import sqlite3 as sqlite
import LogMarker
import SteamDB
from utils import UserInfo, Settings, SteamTools
# 调用 SteamDB 下属方法检测数据库存在, 初始化
SteamDB.initDB()

# 读配置文件中的 userID
aimID = UserInfo.userID()
page = 1    # 初始化为第一页

# 构造请求
Enable = Settings.ProxyStatus()
ProxyMode = Settings.ProxyMode()
ProxyURL = Settings.ProxyURL()
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# 如果启用了代理模式, 单次输出一个提醒
if Enable:
    print(LogMarker.message() + "代理模式已启用, 代理地址为: {}://{}".format(ProxyMode, ProxyURL))
# 否则就 pass
else:
    pass

page = int(input(LogMarker.message() + "请输入需要同步的页数: "))

# 如果启用了代理模式
if Enable:
    proxy = {ProxyMode: ProxyURL}   # 拼接 proxy
    userID = []     # 定义一个 userID 列表
    for i in range(1, page + 1):
        print(LogMarker.message() + "===== 正在同步第 {} 页 =====".format(i))
        communityURL = "https://steamcommunity.com/id/{}/allcomments?ctp={}".format(aimID, i)
        req = requests.get(communityURL,headers=Headers, proxies=proxy)
        # 解析返回数据并创建选择器
        communityData = req.text
        selector = html.fromstring(communityData)

        # Light: 解析数据
        ContentID = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/@id')
        nickName = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[2]/div[1]/a/bdi/text()')
        userAvatar = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[1]/a/img/@src')
        # Content = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[2]/div[@class="commentthread_comment_text"]')
        Content = selector.xpath('//*[@class="commentthread_comment_content"]/div[@class="commentthread_comment_text"]')
        sendTime = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[2]/div[1]/span/@data-timestamp')

        # TODO: 将不定长的 Content 内部元素进行整合, 重新生成列表
        finalStr = ""
        voidContentList = []
        # 进入双循环, 外部循环先打开每个 Content 中的元素, 准备进行拼接
        for listElementCount in range(len(ContentID)):
            # print("当前listElementCount为{}".format(listElementCount))
            ContentDataList = Content[listElementCount].xpath('text()')
            # print("此时 ContentDataList 长度为: {}".format(len(ContentDataList)))
            # 元素整合
            for element in range(len(ContentDataList)):
                finalStr += ContentDataList[element]
                finalStr = finalStr.replace("\t", "").replace("\n", "").replace("\r", "").replace("\u2000", "").replace("\u3000", "")
                # print(finalStr)
                # 将整合后的元素划归到新的数组中
            voidContentList.append(finalStr)
            finalStr = ""
        # 将 Content 刷新成 voidContentList 列表
        Content = voidContentList
        # print(Content)
        # for num in range(5):
        #     print(Content[num])
        # print(len(Content))
        # break

        # TODO: 将特殊换行符从 Content 中去除
        # ContentList = []
        # for content in Content:
        #     newContent = str(content).replace("\t", "").replace("\n", "").replace("\r", "").replace("\u2000", "").replace("\u3000", "")    # 将换行符去除
        #     ContentList.append(newContent)
        #     # print(newContent)
        #     # print(ContentList)
        # Content = ContentList   # 将源 Content 刷新

        # TODO: 通过 userSpaceURL 提取 64位 ID
        userID.clear()  #清空列表
        userSpaceURL = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[1]/a/@href')
        for url in userSpaceURL:
            print(LogMarker.message() + "转换中: {}".format(url.replace("https://steamcommunity.com/id/", "").replace("https://steamcommunity.com/profiles/", "")))
            userIDData = SteamTools.IDTransformer(url)  # 通过接口逐一转换
            userID.append(userIDData)  
        print(LogMarker.message() + "第 {} 页同步完成".format(i))



        '''
        最终将有 6 个字段
        ContentID
        userID
        nickName
        userAvatar
        Content
        sendTime
        '''
        # 数据库同步
        for j in range(len(ContentID)):
            steamDB = sqlite.connect("steamDB.db")
            steamDB_cursor = steamDB.cursor()
            query = "SELECT * FROM 'main'.'msg' WHERE ContentID = '{}'".format(ContentID[j])
            steamDB_cursor.execute(query)
            results = steamDB_cursor.fetchall()
            # 如果已存在 ContentID
            if len(results) > 0:
                print(LogMarker.warning() + "ID: {} 重复, 已跳过".format(ContentID[j]))
                pass
            # 不存在
            else:
                steamDB_cursor.execute(
                    '''INSERT INTO "main"."msg" ("ContentID", "userID", "nickName", "userAvatar", "Content", "sendTime") VALUES (?, ?, ?, ?, ?, ?);''',
                    (ContentID[j], userID[j], nickName[j], userAvatar[j], Content[j], time.strftime('%Y{Y}%m{m}%d{d} %H:%M:%S', time.localtime(int(sendTime[j]))).format(Y='年', m='月', d='日'))
                )
                steamDB.commit()
                steamDB.close()
                print(LogMarker.message() + "ID: {} 已写入!".format(ContentID[j]))
# 没有启用代理
else:
    userID = []     # 定义一个 userID 列表
    for i in range(1, page + 1):
        print(LogMarker.message() + "===== 正在同步第 {} 页 =====".format(i))
        communityURL = "https://steamcommunity.com/id/{}/allcomments?ctp={}".format(aimID, i)
        req = requests.get(communityURL,headers=Headers)
        # 解析返回数据并创建选择器
        communityData = req.text
        selector = html.fromstring(communityData)

        # Light: 解析数据
        ContentID = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/@id')
        nickName = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[2]/div[1]/a/bdi/text()')
        userAvatar = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[1]/a/img/@src')
        # Content = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[2]/div[@class="commentthread_comment_text"]')
        Content = selector.xpath('//*[@class="commentthread_comment_content"]/div[@class="commentthread_comment_text"]')
        sendTime = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[2]/div[1]/span/@data-timestamp')

        # TODO: 将不定长的 Content 内部元素进行整合, 重新生成列表
        finalStr = ""
        voidContentList = []
        # 进入双循环, 外部循环先打开每个 Content 中的元素, 准备进行拼接
        for listElementCount in range(len(ContentID)):
            # print("当前listElementCount为{}".format(listElementCount))
            ContentDataList = Content[listElementCount].xpath('text()')
            # print("此时 ContentDataList 长度为: {}".format(len(ContentDataList)))
            # 元素整合
            for element in range(len(ContentDataList)):
                finalStr += ContentDataList[element]
                finalStr = finalStr.replace("\t", "").replace("\n", "").replace("\r", "").replace("\u2000", "").replace("\u3000", "")
                # print(finalStr)
                # 将整合后的元素划归到新的数组中
            voidContentList.append(finalStr)
            finalStr = ""
        # 将 Content 刷新成 voidContentList 列表
        Content = voidContentList
        # print(Content)
        # for num in range(5):
        #     print(Content[num])
        # print(len(Content))
        # break

        # TODO: 将特殊换行符从 Content 中去除
        # ContentList = []
        # for content in Content:
        #     newContent = str(content).replace("\t", "").replace("\n", "").replace("\r", "").replace("\u2000", "").replace("\u3000", "")    # 将换行符去除
        #     ContentList.append(newContent)
        #     # print(newContent)
        #     # print(ContentList)
        # Content = ContentList   # 将源 Content 刷新

        # TODO: 通过 userSpaceURL 提取 64位 ID
        userID.clear()  #清空列表
        userSpaceURL = selector.xpath('//*[@class="commentthread_comment responsive_body_text   "]/div[1]/a/@href')
        for url in userSpaceURL:
            print(LogMarker.message() + "转换中: {}".format(url.replace("https://steamcommunity.com/id/", "").replace("https://steamcommunity.com/profiles/", "")))
            userIDData = SteamTools.IDTransformer(url)  # 通过接口逐一转换
            userID.append(userIDData)  
        print(LogMarker.message() + "第 {} 页同步完成".format(i))


        '''
        最终将有 6 个字段
        ContentID
        userID
        nickName
        userAvatar
        Content
        sendTime
        '''
        # 数据库同步
        for j in range(len(ContentID)):
            steamDB = sqlite.connect("steamDB.db")
            steamDB_cursor = steamDB.cursor()
            query = "SELECT * FROM 'main'.'msg' WHERE ContentID = '{}'".format(ContentID[j])
            steamDB_cursor.execute(query)
            results = steamDB_cursor.fetchall()
            # 如果已存在 ContentID
            if len(results) > 0:
                print(LogMarker.warning() + "ID: {} 重复, 已跳过".format(ContentID[j]))
                pass
            # 不存在
            else:
                steamDB_cursor.execute(
                    '''INSERT INTO "main"."msg" ("ContentID", "userID", "nickName", "userAvatar", "Content", "sendTime") VALUES (?, ?, ?, ?, ?, ?);''',
                    (ContentID[j], userID[j], nickName[j], userAvatar[j], Content[j], time.strftime('%Y{Y}%m{m}%d{d} %H:%M:%S', time.localtime(int(sendTime[j]))).format(Y='年', m='月', d='日'))
                )
                steamDB.commit()
                steamDB.close()
                print(LogMarker.message() + "ID: {} 已写入!".format(ContentID[j]))

# print(userAvatar)  # len = 50
# print(nickName)
# print(sendTime)
# print(Content)
# print(ContentID)
# print(userSpaceURL)
# print(userID)
