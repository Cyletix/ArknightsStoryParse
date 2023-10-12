# 明日方舟剧情解析

# 说明

此项目用于从解包数据生成Arknights剧情和人物关联的markdown文件, 构建Obsidian仓库, 使用Obsidian打开此仓库可以展示人物和剧情之间的联系, 以便方舟文学家考古, 此项目首先在无精二群公开, 现分享到GitHub

Fork自[arknightPlotReader](https://github.com/BRSblackshoot/arknightPlotReader), 可以看看作者的README, 解析思路不做过多赘述

数据依赖解包仓库ArknightsGameDate
github链接：[https://github.com/Kengxxiao/ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData "https://github.com/Kengxxiao/ArknightsGameData")

---
# 目录
## Appendix
放置图片等附件杂项, 不重要

## ArknightsGameData
游戏的解包原数据, 这是引入别人的项目作为子模块, 本人不负责此内容的更新, 需要定期从此项目拉取更新, 由于是别人的项目作为子模块, 所以不要对ArknightsGameData中的文件进行任何改动, 否则同步时会出问题, 如果进行了改动也要在git工具中放弃更改. 如果修改过于复杂不知如何处理就都删掉, 重新引入子模块, 或许会遇到一些困难, 但能够根除问题

## Character
此文件夹下存放干员的markdown文件, 这些文件通过`character_data_to_md.py` 脚本解析生成, 在初次生成后再次执行脚本不会对现有的md文件更改或重新生成, 后续


---
# 使用方法

如果你想在这个基础上进行一些开发,则可以参考以下流程介绍每个功能的实现

## 1.准备数据

从ArknightsGameDate项目获取数据,作为子模块放到根目录下即可.
这里有两种引入方法(确保你已经安装了git):

1. 直接克隆新的数据, 在此目录运行命令 `git clone https://github.com/Kengxxiao/ArknightsGameData.git`
2. 使用子模块引入数据, 参照下面的说明

在本项目中我已经更改为使用子模块并引入过子模块ArknightsGameData了

## 2.处理数据

如果没有需要的数据则运行 `解包剧情阅读器.py`, `character_data_to_md.py` 这两个文件, 分别解析剧情和干员的markdown文件

1. 解包剧情阅读器.py 用于解析剧情
2. character_data_to_md.py 用于解析干员

## 3.数据预览

1. 下载Obsidian, 使用Obsidian打开此文件夹, 并打开关系图谱
2. 在关系图谱筛选条件里添加 `path:(ArknightsGameData/zh_CN OR ArknightsOperator)`, 主要是排除其他文件夹内容

## 以下是设置子模块的步骤：

1. **在主项目仓库中添加子模块：**
   在主项目的根目录下，使用以下命令添加子模块：
   bashCopy code
   `git submodule add <URL to submodule> <path>`
   其中，`<URL to submodule>` 是子项目的远程仓库 URL，`<path>` 是将子项目放置在主项目中的路径。
2. **初始化和更新子模块：**
   在主项目中添加子模块后，需要进行初始化和更新操作：
   bashCopy code
   `git submodule init git submodule update`
   这将拉取子模块的内容到你的主项目中。
3. **拉取子模块的更新：**
   当子模块的远程仓库有更新时，你可以通过以下命令来拉取子模块的更新：
   bashCopy code
   `git submodule update --remote`
   这会将子模块更新到最新的远程内容。
   


---

# 更新数据

由Arknights版本更新造成的数据变动, 依赖于ArknightsGameDate的解包项目的更新, 当项目有更新后, 使用git命令拉取更新, 再运行一次处理数据的脚本即可. 

如果你有vscode等自带git工具的编辑器, 可以使用工具进行更新最新的ArknightsGameData项目的内容, 没有的话也可以通过命令行使用git命令执行, 这个自己学习下.

## Obsidian的数据处理技巧

1. 有些干员会有别名, 比如异客-"沙卒", 陈-陈晖洁, 这种情况下如果想要将两个人的md合并, 则需要指定一个主要md, 将别名外加上双中括号添加到头文件的yaml字段中(也就是图中的Properties), 字段名固定为aliases, 这是一个特殊的指定类型. 添加别名后, 图谱中的别名的md会指向此主md, 此时可以删除别名md文件, md中的源码如下, 在Properties的界面操作也可以

```yaml
aliases:
  - "[[克洛丝]]"
```

2. 有些不是干员的剧情人物并不会被character_data_to_md.py脚本创建, 在我想出来解决办法之前需要手动创建, 从关系图谱或者某个剧情或者干员的md文件中点击灰色的超链接直接创建, 此时md内容是空的, 根据需要添加信息, 剧情说明, properties等等
3. 手动添加潜在的链接. 打开一篇剧情, 在出链页面会检测当前笔记中的潜在的链接, 点击手动添加
4. 对于未创建的人物与剧情的链接, 还可以选择在人物的md界面查看反向链接, 点击提到当前文件名, 可以查看这个人物出现在哪些剧情中

不懂的地方参考markdown语法, Obsidian官方文档及插件文档

## 使用Note Linker插件自动化创建

 如果有个干员的md文件已经创建, 但是有些对话中出现的, 想要在对话内容中展示的话, 可以运行Note Linker插件处理潜在链接, 这一步耗时极长, 需要耐心等待, 如果我在项目中运行过一次了, 克隆下来的内容就不需要再处理, 仅处理每次更新的新剧情即可. 如果Note Linker实在是卡得动不了, 可以选择手动添加潜在的链接.

# 效果展示

在Obsidian里有点卡, 暂时先不展示了
想展示在最前面加上叹号
[1692981693734](1692981693734.png)
[1692981722019](1692981722019.png)
[1692981731459](1692981731459.png)
[1692981733714](1692981733714.png)


---
# 接下来可能进行的工作

## 多人对话处理

形如 \[name="拜颂&能天使"\] 开头的对话内容会修改为 \[\[拜颂&能天使\]\]
需要优化代码, 将其正确修改为\[\[拜颂\]\]&\[\[能天使\]\]

## 别名处理

假如以临光为主, 玛丽亚作为别名, 则需要想办法把剧情story中的玛丽亚改为别名形式, 如下:
\[玛丽亚\] ----> \[临光|玛丽亚\]
目前仅使用markdown中的aliases属性来关联两者

## 干员档案数据

暂时不知道怎么做, 如果不能从ArknightsGameData获取, 则只能写爬虫从PRTS获取了
