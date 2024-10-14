import re
import pinyin
# 定义一个函数用于提取中文作者名字的拼音
def extract_chinese_pinyin(author_name):
    pinyin_list = pinyin.get(author_name)
    return ''.join(pinyin_list)
# 定义一个函数用于按中文作者拼音排序
def sort_chinese_references(references):
    return sorted(references, key=lambda x: extract_chinese_pinyin(re.findall(r'[\u4e00-\u9fff]+', x)[0]))
# 定义一个函数用于按英文作者排序
def sort_english_references(references):
    return sorted(references, key=lambda x: x.split(".")[0])
# 读取文献信息
with open("references.txt", "r", encoding="utf-8") as file:
    references = file.readlines()
# 分别对中文和英文文献进行排序
chinese_references = [ref for ref in references if re.search("[\u4e00-\u9fff]", ref)]
english_references = [ref for ref in references if not re.search("[\u4e00-\u9fff]", ref)]
sorted_chinese_references = sort_chinese_references(chinese_references)
sorted_english_references = sort_english_references(english_references)
# 合并排序后的结果
sorted_references = sorted_chinese_references + sorted_english_references
# 将结果保存到文本文件
with open("sorted_references.txt", "w", encoding="utf-8") as file:
    for reference in sorted_references:
        file.write(reference)
print("排序结果已保存到 sorted_references.txt 文件中。")
