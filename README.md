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
|  文本格式名称   |
  | :--------: |
| [h1] 标题文字 [/h1] 
| [b] 粗体文本 [/b] |
| [u] 下划线文本 [/u] |
| [i] 斜体文本 [/i] |
| [strike] 删除文本 [/strike] |
| [spoiler] 隐藏文本 [/spoiler] |
| [noparse] 不解析[b]标签[/b] |
| [hr][/hr]渲染水平分隔线 |
| [url=store.steampowered.com] 网站链接 [/url]网站链接 |
|  :tinder: Steam表情 |
- 无法同步大量内容，受限于Steam反爬和API限制，根据IP、时间等等因素，如果需要同时获取留言内容和对应的用户信息，大约最多可获取1000条，如果只获取留言内容，则可获取5000条甚至更多，但UserID列不会有数据
- 只能从留言板第一页开始向后读取，直到达到指定页数，不支持仅读取指定页数

## TODO
- 同步完成后自动发送同步状态至评论区



## 如何使用

别急，在写了

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

本程序的核心功能的开发者是
```
Author  : AlanStar
Contact : alan233@vip.qq.com
```

感谢以下开发者对本项目作出的贡献：

<a href="https://github.com/ab-Royo/SteamCommentsToDB/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ab-Royo/SteamCommentsToDB" />
</a>