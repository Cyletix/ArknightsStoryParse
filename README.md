# 明日方舟剧情解析

# 说明

此项目用于从解包数据生成Arknights剧情和人物关联的markdown文件, 构建Obsidian仓库, 使用Obsidian打开此仓库可以展示人物和剧情之间的联系, 以便方舟文学家考古, 此项目首先在无精二群公开, 现分享到GitHub

Fork自[arknightPlotReader](https://github.com/BRSblackshoot/arknightPlotReader), 可以看看作者的README, 解析思路不做过多赘述

数据依赖解包仓库ArknightsGameDate
github链接：[https://github.com/Kengxxiao/ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData "https://github.com/Kengxxiao/ArknightsGameData")

---
# 使用方法
## 1.准备数据
从ArknightsGameDate数据库获取数据,放到根目录下即可. 
这里有两种方法(确保你已经安装了git):
1. 在此目录运行命令行命令 `git clone https://github.com/Kengxxiao/ArknightsGameData.git` 直接克隆新的数据
2. 使用[子模块](##以下是设置子模块的步骤：)引入数据, 参照下面的说明


## 2.处理数据
如果没有需要的数据则运行`解包剧情阅读器.py`, `character_data_to_md.py` 这两个文件, 分别解析剧情和干员的markdown文件
1. 解包剧情阅读器.py 用于解析剧情
2. character_data_to_md.py 用于解析干员

## 3.数据预览
1. 下载Obsidian, 使用Obsidian打开此文件夹, 并打开关系图谱
2. 在关系图谱筛选条件里添加 `path:(ArknightsGameData/zh_CN OR ArknightsOperator)`, 主要是排除其他文件夹内容




# 更新数据
由Arknights版本更新造成的数据变动, 依赖于ArknightsGameDate的解包项目的更新, 当项目有更新后, 使用git命令拉取更新, 再运行一次处理数据的脚本即可

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
## 效果展示
[Pasted image 20230824032900.png](Pasted image 20230824032900.png)
[[Pasted image 20230824032940.png]]
[Pasted image 20230824033004.png](Pasted image 20230824033004.png)
[[Pasted image 20230824033130.png]]

