'''
Description: 新流程不再从'https://prts.wiki/w/'的html文件爬取,改用ArknightsGameData项目解包文件获取
Author: Cyletix
Date: 2023-08-06 19:29:59
LastEditTime: 2023-08-07 21:48:47
'''
import json
import pandas as pd


character_table_path = 'E:\OneDrive\Code\Github\ArknightsGameData\zh_CN\gamedata\excel\character_table.json'

# 使用 with 语句打开json文件，确保在操作完成后自动关闭文件
with open(character_table_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

#查看char_285_medic2的所有属性
for key in json_data["char_285_medic2"].keys():
    print(key)


def get_char_keys_list():
    # 获取干员char_key列表
    char_keys_list = [{"char_key": char_key} for char_key in json_data if char_key.startswith("char_")]
    return char_keys_list

def get_name_list():
    # 获取chinese name列表
    name_list = [char_data["name"] for char_key, char_data in json_data.items() if char_key.startswith("char_")]
    return name_list


if __name__ == '__main__':
    char_keys_list=get_char_keys_list()

    # 查找未插入数据库的干员
    op_not_in_db = search_sql(char_keys_list)


    from mypgsql import search_sql, pg_query
    import mypgsql2
    # 插入到数据库
    mypgsql2.insert_char_keys(op_not_in_db)



    # 创建一个空的列表，用于存储每个角色的属性
    character_data_list = []

    # 遍历所有角色数据，提取所需的属性
    for char_key, char_data in json_data.items():
        if char_key.startswith("char_"):
            character_data = {
                "char_key": char_key,
                "chinese": char_data.get("name", ""),
                # "description": char_data.get("description", ""),
                # "canUseGeneralPotentialItem": char_data.get("canUseGeneralPotentialItem", ""),
                # 继续添加其他属性...
            }
            character_data_list.append(character_data)


    if input('是否导入数据库\n')=='Y':
        # 插入函数,测试中...
        mypgsql2.insert_char_keys(character_data_list)



    if input('是否输出excel\n')=='Y':
        # 将列表转换为 pandas 的 DataFrame
        df = pd.DataFrame(character_data_list)

        # 将 DataFrame 导出到 Excel 文件中
        output_file_path = "character_table.xlsx"
        df.to_excel(output_file_path, index=False)

        print(f"已将数据保存到 {output_file_path} 文件中。")












# ####################################################
# # 遍历所有的 "char_285_medic" 数据
# for char_key, char_data in json_data.items():
#     # 获取 "data" 属性
#     data_list = char_data.get("phases", [])[0].get("attributesKeyFrames", [])
    
#     # 遍历 "data" 属性中的列表
#     for data in data_list:
#         level = data.get("level")
#         attributes = data.get("data", {})

#         # 在这里可以访问每个属性的值
#         max_hp = attributes.get("maxHp", 0)
#         atk = attributes.get("atk", 0)
#         defense = attributes.get("def", 0)
#         # 其他属性...

#         # 打印示例输出
#         print(f"Character: {char_key}, Level: {level}")
#         print(f"Max HP: {max_hp}, ATK: {atk}, DEF: {defense}")
#         print("=" * 30)