# 1、input读取原始文件并将其存储为一个字典
with open('from.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    origin_data = {}
    for line in lines:
        if ':' in line:
            key, value = line.strip().split(':', 1)
            origin_data[key] = value.strip()

output_dict = {}

# 找到所有重复的值，并为它们创建一个新的带有前缀的键
# duplicates = {}
# for key, value in origin_data.items():
#     if list(origin_data.values()).count(value) > 1:
#         duplicates[key] = value

# # 对字典按照键进行排序，返回一个元组列表
sorted_tuples = sorted(origin_data.items(), key=lambda x: x[0])

# 将排序结果存入列表
# sorted_list = [item for item in sorted_tuples]
#
# # 输出排序后的结果
# for key, value in sorted_list:
#     print(key, value)
#
# # 将所有键值对写入一个新文件中
# with open('pack/zh_new.js', 'w', encoding='utf-8') as f:
#     # 先写入已排序的键值对
#     for key, value in sorted_list:
#         f.write(f'i18_{key}: {value}\n')
#     # 再写入未排序的键值对
#     for key, value in origin_data.items():
#         if key not in [item[0] for item in sorted_list]:
#             f.write(f'i18_{key}: {value}\n')
#
# # # 输出排序后的结果
# key_set = {}
# for item in sorted_tuples:
#     key_set.pop(item[0])
#     print(item[0], item[1])

# 将所有键值对写入一个新文件中
with open('to.js', 'w', encoding='utf-8') as f:
    for item in sorted_tuples:
        f.write(item[0] + ': ' + item[1] + '\n')
    # for key, value in sorted_tuples.items():
    #     f.write(key + ': ' + value + '\n')
