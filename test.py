# 解析文本正则测试

import re

juqing = []
juqing.append(r"""[name="能天使"] 牛逼""")
juqing.append(r"""[name="拜松&能天使"]   又来？""")

# 编译正则表达式模式
re_mingzi = re.compile(r'\[name=".*"\]')
re_duihua = re.compile(']\s*(.*)')
re_huifu = re.compile('"(.*)",')
re_xuanxiang = re.compile('"(.*)"')

jiexijuqing=[]

for i in juqing:
    # 第一种类型 对话
    if i[:5] == "[Name" or i[:5] =="[name":
        mingzi=re_mingzi.findall(i)
        duihua=re_duihua.findall(i)
        
        # print(mingzi[0]+": "+duihua[0])
        jiexijuqing.append('[['+mingzi[0]+"]]: "+duihua[0])
    
    # 第二种类型 无人物文字
    if i[:5] =="[Dial" or i[:5] =="[dial" :
        # print("")
        jiexijuqing.append("")
    
    # 第三种类型 选择支
    if i[:5] =="[Deci" or i[:5] =="[deci" :
        huifulist = re_huifu.findall(i)[0].split(";")
        # print("\n下面是可选择的回复：")
        jiexijuqing.append("\n下面是可选择的回复：")
        j = 1
        for huifu in huifulist:
            # print("    选项{}：".format(j)+huifu)
            jiexijuqing.append("    选项{}：".format(j)+huifu)
            j+=1
    if i[:5] =="[Pred" or i[:5] =="[pred" :
        xuanxianglist = re_xuanxiang.findall(i)
        
        # print("\n下面是回复选项{}的剧情：".format(xuanxianglist))
        jiexijuqing.append("\n下面是回复选项{}的剧情：".format(xuanxianglist))
    
    # 遇到文字直接输出
    if i[:1] !="[":
        # print(i)
        jiexijuqing.append(i)


print(jiexijuqing)





strings = ["[A]", "[A&B]", "[A&B&C]"]

re_mingzi = re.compile(r'\[([^\]]+)\]')

name_list = []

for s in strings:
    match = re_mingzi.match(s)
    if match:
        names = match.group(1).split('&')
        name_list.extend(names)