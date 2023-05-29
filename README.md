<!--
 * @Author: abRoy abroyo@outlook.com
 * @Date: 2023-05-27 21:51:10
 * @FilePath: \SteamCommentsToDB\README.md
 * @Description: 
 * 
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
-->
# SteamCommentsToDB

<div align="center">


<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
_✨获取Steam个人资料留言板并存储至数据库_
<!-- prettier-ignore-end -->

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/nonebot/nonebot2/master/LICENSE">
    <img src="https://img.shields.io/github/license/nonebot/nonebot2" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="python">
  <img src="https://img.shields.io/badge/SQLite-3-ff69b4" alt="SQLite">
</p>


## 简介

SteamCommentsToDB 可以获取Steam个人资料留言板的内容和留言者的个人信息并存储至SQLite数据库，便于记录和统计分析。


## 存在的问题
- 使用以下文本格式的内容无法被程序识别，在导入到数据库后会丢失内容（仅下表列出的格式部分，其余正常）

| 文本格式名称                                   |
|:----------------------------------------:|
| [h1] 标题文字 [/h1]                          |
| [b] 粗体文本 [/b]                            |
| [u] 下划线文本 [/u]                           |
| [i] 斜体文本 [/i]                            |
| [strike] 删除文本 [/strike]                  |
| [spoiler] 隐藏文本 [/spoiler]                |
| [url=store.steampowered.com] 网站链接 [/url] |
| :tinder: Steam表情                         |

- 无法同步大量内容，受限于Steam反爬和API限制，根据IP、时间等等因素，如果需要同时获取留言内容和对应的用户信息，大约最多可获取1000条，如果只获取留言内容，则可获取5000条甚至更多，但UserID列不会有数据
- 只能从留言板第一页开始向后读取，直到达到指定页数，不支持仅读取指定页数

## TODO
- [ ] 同步完成后自动发送同步状态至评论区



## 如何使用
首先你需要一个大于等于3.8版本的Python环境，然后按照以下步骤进行操作

>如何安装Python
>https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624


### 1.获取本项目
如果你有Git，在命令行中输入以下命令
```
git clone https://github.com/ab-Royo/SteamCommentsToDB.git
```

如果你没有Git，那么你可以点击本页面右上角的**Code**按钮，然后选择**Download ZIP**，下载完成后解压到你想要的位置

### 2.安装依赖
进入你解压出来的文件夹中
#### Windows10:
点击文件资源管理器左上角**文件**，选择**打开Windows PowerShell**
在命令行中输入以下命令
```
pip install -r requirements.txt
```
#### Windows11:
在文件资源管理器窗口内空白处单击鼠标右键，选中**在终端中打开**
在命令行中输入以下命令
```
pip install -r requirements.txt
```


### 3.配置要获取的留言板
首先打开你的个人资料页，然后单击鼠标右键，选择 **复制网页URL**
如果你设定了**自定义链接**,那么你的链接应该形如：
> https://steamcommunity.com/id/**xxxx**/

如果你没有设定自定义链接，那你就是默认的**数字链接**，那么你的链接应该形如:
> https://steamcommunity.com/profiles/**xxxx**/

将链接内的 **xxxx** 的内容替换掉 `\SteamCommentsToDB\config\info.json` 中的 **userID** 字段的引号内的 **xxxx**

### 4.配置代理
如果你的网络不能直连Steam（即无法打开 https://steamcommunity.com ），那么你需要配置代理，否则请跳过这一步

将 `\SteamCommentsToDB\config\settings.json` 中的 **"Enable": false** 字段中的`false`改为`true`，并在 **"ProxyURL":** 字段的引号内填入你的代理地址，如果你使用ClashforWindows，那么默认的代理地址就是：
>127.0.0.1:7890


### 5.运行本项目
#### Windows10:
在 `SteamCommentsToDB` 文件夹内，点击文件资源管理器左上角**文件**，选择**打开Windows PowerShell**，在弹出的窗口中输入以下命令
```
python main.py
```
#### Windows11:
在 `SteamCommentsToDB` 文件夹内，在文件资源管理器窗口内空白处单击鼠标右键，选中**在终端中打开**，在弹出的窗口中输入以下命令
```
python main.py
```

随后根据程序提示操作即可:
1. 输入URL格式：参考*3.配置要获取的留言板*，你的个人资料页是自定义链接，那么输入1，如果是数字链接，那么输入2，然后按回车键确认；
2. 输入需要同步的页数：每一页有50条留言，你可以在个人资料留言板位置点击**查看所有 xxx 条留言**，此处的页数为你最多获取的页数，例如你想获取前10页的留言，那么你就输入10，然后按回车键确认；
3. 请输入同步模式：如果你想在获取留言的同时获取留言发送者的userID，那么输入1或2（此处Steam获取和API获取为两种不同的方式，请根据网络情况自行选择），如果你只想获取留言内容，那么输入2，然后按回车键确认；
>需要说明的是，如果你希望进行一些留言板的统计分析，那么你需要获取留言发送者的userID！否则你只能获取留言者的昵称(nickName)，而昵称是可以修改的，程序只能获取运行时的留言发送者的昵称，如果TA修改了昵称，程序不会修改数据库里已写入的昵称。


### 6.查阅数据库
首先你需要一个SQLite数据库查看工具，例如 [DB Browser for SQLite (免费)](https://sqlitebrowser.org/dl/)，DataGrip等等

打开你的数据库查看工具，选择 **打开数据库**，选择 `SteamCommentsToDB`文件夹的`steamDB.db`文件，即可查看你的留言板内容

#### msg表结构
| 列名         | 数据类型        | 描述               |
|------------|-------------|------------------|
| ContentID  | varchar(30) | Steam每一条评论的唯一ID  |
| userID     | char(64)    | 评论发送者的64位SteamID |
| nickName   | char(100)   | 评论发送者的昵称         |
| userAvatar | char(200)   | 评论发送者的头像         |
| Content    | char(1000)  | 评论内容             |
| UnixTime   | char(100)   | 评论发送的Unix时间      |
| sendTime   | char(20)    | 评论发送的北京时间        |

#### 一些SQL常用指令
```sql
SELECT * FROM msg WHERE userID = '76561198000000000' --查询某个用户的所有留言
SELECT * FROM msg WHERE ContentID = '123456789' --查询某条留言
SELECT * FROM msg WHERE Content LIKE '%xxx%' --查询留言内容中包含xxx的所有留言
```
## 常见问题

1. 程序运行时出现以下提示
```
connectionpool.py:852: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn((
```
为了优化查询效率关闭了SSL验证。

如果你想开启SSL验证，可以在 `\SteamCommentsToDB\main.py` 中将 **req = requests.get(communityURL,headers=Headers, proxies=proxy, verify=False)** 字段中的`false`改为`true`，但是这会导致查询速度变慢、稳定性变差。


2. 程序运行时出现以下提示
```
Traceback (most recent call last):
  File "G:\...\main.py", line 123, in <module>
    userIDData = SteamID.XpathSteamID(url)  # 通过接口逐一转换
  File "G:\...\utils.py", line 131, in XpathSteamID
    __SteamID = re.findall('"steamid":"(.*?)"', xml.text, re.S)[0]
IndexError: list index out of range
```
说明你的网络状况不佳，请更换网络环境或开启代理后重试。

### 开发者

**初版代码由AlanStar编写**

>Contact : alan233@vip.qq.com
>License : MIT

**感谢以下开发者对本项目作出的贡献：**

<a href="https://github.com/ab-Royo/SteamCommentsToDB/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ab-Royo/SteamCommentsToDB" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

如果有任何问题或建议，欢迎ISSUE或PR。