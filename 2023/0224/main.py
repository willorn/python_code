
# 读取原始文件并将其存储为一个字典
with open('zh.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    origin_data = {}
    for line in lines:
        if ':' in line:
            key, value = line.strip().split(':', 1)
            origin_data[key] = value.strip()

output_dict = {}

# 找到所有重复的值，并为它们创建一个新的带有前缀的键
duplicates = {}
for key, value in origin_data.items():
    if list(origin_data.values()).count(value) > 1:
        duplicates[key] = value

# # 对字典按照value进行排序，返回一个数组
sorted_tuples = sorted(duplicates.items(), key=lambda x: x[1])

# 将排序结果存入列表
sorted_list = [item for item in sorted_tuples]
# for key, value in sorted_list:
#     print(key, value)
# print("输出排序后的结果，debug使用")

# 将所有键值对写入一个新文件中，并将所有的key都加上了i18前缀
with open('zh_new.js', 'w', encoding='utf-8') as f:
    print("1、先向文件写入已排序的键值对")
    for key, value in sorted_list:
        f.write(f'i18_{key}: {value}\n')
    print("2、再将剩下的键值对写到文件中")
    # 再写入未排序的键值对
    for key, value in origin_data.items():
        if key not in [item[0] for item in sorted_list]:
            f.write(f'i18_{key}: {value}\n')

print("文件导出结束")


# #   有一个文件名为zh.js，存放了很多键值对类似 "key: 'value',"，下面是例子
# #   i18_class:'班别',
# #   i18_blameName:'工厂责任站名称',
# #   i18_blameCode:'工厂责任站编码',
# #   false_point_removal_rate_formula: '假点去除率（标准）= (点AI_OK ∩ 点人工_OK) / (总点数 - 点人工_NG)',
# #   i18_please_input:'请输入',
# #   i18_operate_success:'操作成功',
# #   i18_operate_success:'操作成功',
# #   能编写一个java代码找到所有相同的value的键值对，并为这些键值对的key加上'new_kkk'前缀，然后将这些键值对都放到文件的最后输出吗，输出的文件名为new_zh.js


# 读取原始文件并将其存储为一个字典。
#
# 找到所有重复的值，并为它们创建一个新的带有前缀的键。
#
# 将所有新键值对添加到原始字典中。
#
# 将原始字典中的所有键值对按照键的顺序排序。
#
# 将所有键值对写入一个新文件中。