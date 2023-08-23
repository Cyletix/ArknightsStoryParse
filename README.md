# 明日方舟剧情解析

# 说明

此项目用于从解包数据生成Arknights剧情和人物关联的markdown文件, 构建Obsidian仓库, 使用Obsidian打开此仓库可以展示人物和剧情之间的联系, 以便方舟文学家考古, 此项目首先在无精二群公开, 现分享到GitHub


# 使用方法
1. 如果没有数据则运行`解包剧情阅读器.py`, `character_data_to_md.py` 这两个文件, 分别解析剧情和干员的markdown文件
2. 下载Obsidian, 使用Obsidian打开此文件夹, 并打开关系图谱
3. 在关系图谱筛选条件里添加 `path: (ArknightsGameData/zh_CN) OR -(ArknightsOperator)`


## 效果展示

![[Pasted image 20230824032900.png]]
![[Pasted image 20230824032940.png]]
![[Pasted image 20230824033004.png]]
![[Pasted image 20230824033130.png]]

Fork自[arknightPlotReader](https://github.com/BRSblackshoot/arknightPlotReader), 可以看看作者的README, 解析思路不做过多赘述

数据依赖解包仓库ArknightsGameDate
github链接：[https://github.com/Kengxxiao/ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData "https://github.com/Kengxxiao/ArknightsGameData")

由于本人不太懂MIT开源协议, 若有版权等问题请联系我, 我会积极处理