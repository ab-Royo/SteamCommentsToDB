# -*- coding: utf-8 -*-
"""
@File    : SteamDB.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""
import os.path
import sqlite3 as sqlite

import LogMarker

# 初始化数据库
def initDB():
    __DBExist = os.path.exists("./steamDB.db")
    # 如果文件存在
    if __DBExist == 1:
        print(LogMarker.message() + "数据库已存在!")
    else:
        # 创建数据库文件并初始化
        __steamDB = sqlite.connect("steamDB.db")
        print(LogMarker.message() + "数据库创建成功!")
        # 创建游标 (cursor)
        __cursor = __steamDB.cursor()
        """
        ContentID 评论ID pk
        userID 用户ID
        nickName 用户名
        Content 内容
        sendTime 发送时间
        """
        __cursor.execute('''CREATE TABLE msg
        (ContentID varchar(30) primary key,
        userID char(64) not null,
        nickName char(100),
        userAvatar char(200),
        Content char(1000),
        sendTime char(20));''')
        # 提交并关闭流
        __steamDB.commit()
        __steamDB.close()


if __name__ == "__main__":
    initDB()
