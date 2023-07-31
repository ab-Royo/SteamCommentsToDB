# -*- coding: utf-8 -*-
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
        print(LogMarker.message() + "开始创建数据库!")
        # 创建游标 (cursor)
        __cursor = __steamDB.cursor()
        """
        ContentID 评论ID pk
        userID 用户ID
        nickName 用户名
        Content 内容
        UnixTime 时间戳
        sendTime 发送时间
        """
        __cursor.execute('''CREATE TABLE msg
        (ContentID varchar(30) primary key,
        userID char(64) not null,
        nickName char(100),
        userAvatar char(200),
        Content char(1000),
        UnixTime char(100),
        sendTime char(20));''')

        """
        userID 用户ID pk
        nickname 对用户的昵称
        profileName 用户的个人资料昵称
        recently 是否满足条件
        """
        __cursor.execute('''CREATE TABLE friends
        (userID char(64) primary key,
        nickName char(100),
        profileName char(100),
        recently char(10));''')

        # 提交并关闭流
        __steamDB.commit()
        __steamDB.close()
        print(LogMarker.message() + "数据库初始化成功!")


if __name__ == "__main__":
    initDB()
