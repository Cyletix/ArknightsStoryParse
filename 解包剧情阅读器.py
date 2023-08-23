'''
Description: 文件描述
Author: Cyletix
Date: 2023-06-08 19:31:10
LastEditTime: 2023-06-17 21:01:10
FilePath: \arknightPlotReader\解包剧情阅读器.py
'''
import re
import os
from walkFile import walkFile

def parse_arknights_story(file_path_name,save_path_name):

    with open(file_path_name, 'r',encoding='utf-8') as f:
        juqing = f.readlines()

    re_mingzi = re.compile('name= ?"(.*)"')
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



    with open(save_path_name, 'w', encoding='utf-8') as f:
        for i in jiexijuqing:
            f.write("\n"+i)



if __name__=='__main__':
    path="Arknights剧情\story"
    
    story_language=input('请选择story语言(1.Chinese; 2.Japanese; 3.English):')
    if story_language==2:
        path+='_jp'
    elif story_language==3:
        path+='_en'


    file_path_list=walkFile(path)

    for file_path_name in file_path_list:
        file_path,file_name=os.path.split(file_path_name)
        file_name2,ext_name=os.path.splitext(file_name)
        # save_name = os.path.join(file_name+"_parse"+ext_name)
        save_name=file_name
        save_path=path
        save_path2=file_path.split(path)[1]
        save_path_name=os.path.join(save_path+save_path2,file_name2+'.md')
        
        parse_arknights_story(file_path_name,save_path_name)