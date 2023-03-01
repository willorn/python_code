from_file = 'file_from.js'
to_file = 'file_to.js'

print("此程序用作国际化文件的排序，按照key排序")
print("1、input读取原始文件并将其存储为一个字典")
with open(from_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    origin_data = {}
    for line in lines:
        if ':' in line:
            key, value = line.strip().split(':', 1)
            origin_data[key] = value.strip()

output_dict = {}
# # 对字典按照键进行排序，返回一个元组列表
sorted_tuples = sorted(origin_data.items(), key=lambda x: x[0])

print("2、正在写出文件")
# 将所有键值对写入一个新文件中
with open(to_file, 'w', encoding='utf-8') as f:
    for item in sorted_tuples:
        f.write(item[0] + ': ' + item[1] + '\n')

print("3、写出文件完成", to_file)
