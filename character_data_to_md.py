import json
import os

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], f"{name}{a}_")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, f"{name}{i}_")
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

character_table_path = 'ArknightsGameData\zh_CN\gamedata\excel\character_table.json'

# 读取JSON文件
with open(character_table_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 生成Markdown文件
output_directory = 'Character/Operator'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for char_key in json_data:
    if char_key.startswith("char_"):
        character_data = json_data[char_key]
        # 展开嵌套的JSON对象
        flattened_data = flatten_json(character_data)
        character_name = flattened_data.get('name', 'unknown')
        
        markdown_content = "---\n"
        for key, value in flattened_data.items():
            markdown_content += f"{key}: {value}\n"
        markdown_content += "---\n\n"
        
        markdown_filename = os.path.join(output_directory, f"{character_name}.md")

        # if os.path.exists(markdown_filename):
        #     print(f"Markdown文件 '{markdown_filename}' 已存在，跳过生成。")
        #     continue

        with open(markdown_filename, 'w', encoding='utf-8') as markdown_file:
            markdown_file.write(markdown_content)
            
print("Markdown文件已生成。")
