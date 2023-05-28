# -*- coding: utf-8 -*-
"""
@File    : LogMarker.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""

# 生成 Log 消息前置标识(带颜色)
def message():
    return "\033[92m[message] \033[0m"

def warning():
    return "\033[93m[warning] \033[0m"

def error():
    return "\033[31m[error] \033[0m"


# 调试, 分别输出三种不同颜色的消息
if __name__ == "__main__":
    print(message() + "这是一条普通消息")
    print(warning() + "这是一条警告消息")
    print(error() + "这是一条错误消息")
