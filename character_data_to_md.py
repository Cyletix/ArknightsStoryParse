import json
import os

character_table_path = 'ArknightsGameData\zh_CN\excel\character_table.json'

# 读取JSON文件
with open(character_table_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 生成Markdown文件
output_directory = 'ArknightsOperator'  # 替换为你想要保存Markdown文件的文件夹路径

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for char_key in json_data:
    if char_key.startswith("char_"):
        character_data = json_data[char_key]
        character_name = character_data.get('name', 'unknown')
        
        markdown_content = "---\n"  # YAML开始标记
        for key, value in character_data.items():
            markdown_content += f"{key}: {value}\n"
        markdown_content += "---\n\n"
        
        markdown_filename = os.path.join(output_directory, f"{character_name}.md")

        if os.path.exists(markdown_filename):
            print(f"Markdown文件 '{markdown_filename}'\t已存在，跳过生成。")
            continue

        with open(markdown_filename, 'w', encoding='utf-8') as markdown_file:
            markdown_file.write(markdown_content)
            
print("Markdown文件已生成。")
