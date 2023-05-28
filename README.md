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

### 1.安装依赖
在命令行中输入以下命令
```
pip install -r requirements.txt
```

### 2.获取本项目
在命令行中输入以下命令
```
git clone https://github.com/ab-Royo/SteamCommentsToDB.git
```

### 3.配置要获取的留言板
首先打开你的个人资料页，然后单击鼠标右键，选择 **复制网页URL**
如果你设定了**自定义链接**,那么你的链接应该形如：
> https://steamcommunity.com/id/**xxxx**/

如果你没有设定自定义链接，那你就是默认的**数字链接**，那么你的链接应该形如:
> https://steamcommunity.com/profiles/**xxxx**/

将 **xxxx** 的内容替换掉 `\SteamCommentsToDB\config\info.json` 中的 **userID** 字段的引号内的 **xxxx**

### 4.运行本项目
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

随后根据程序提示操作即可

### 5.查阅数据库
首先你需要一个SQLite数据库查看工具，例如 [DB Browser for SQLite (免费)](https://sqlitebrowser.org/dl/)，DataGrip等等

打开你的数据库查看工具，选择 **打开数据库**，选择 `SteamCommentsToDB`文件夹的`steamDB.db`文件，即可查看你的留言板内容

msg表结构
| 列名         | 数据类型        | 描述               |
|------------|-------------|------------------|
| ContentID  | varchar(30) | Steam每一条评论的唯一ID  |
| userID     | char(64)    | 评论发送者的64位SteamID |
| nickName   | char(100)   | 评论发送者的昵称         |
| userAvatar | char(200)   | 评论发送者的头像         |
| Content    | char(1000)  | 评论内容             |
| UnixTime   | char(100)   | 评论发送的Unix时间      |
| sendTime   | char(20)    | 评论发送的北京时间        |






## 常见问题

别急，在写了

## 许可证

SteamCommentsToDB 采用 MIT 许可证进行开源

```text
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```


### 开发者

初版代码由AlanStar编写

Contact : alan233@vip.qq.com

License : MIT

感谢以下开发者对本项目作出的贡献：

<a href="https://github.com/ab-Royo/SteamCommentsToDB/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ab-Royo/SteamCommentsToDB" />
</a>
