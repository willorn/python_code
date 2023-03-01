from_file = 'file_origin_menu.txt'
to_file = 'file_to_menu.txt'

print("此程序用作国际化文件的排序，按照key排序")
print("1、input读取原始文件并将其存储为一个字典")
origin_arr = []
with open(from_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    origin_data = {}
    for line in lines:
        if line.startswith('UPDATE `aqrose`'):
            origin_arr.append(line.replace('\n', ''))
            print(line.replace('\n', ''), ";")
    # origin_arr.append("'" + line.replace('\n', '') + "'")

# output_dict = {}
# # # 对字典按照键进行排序，返回一个元组列表
# sorted_tuples = sorted(origin_data.items(), key=lambda x: x[0])

print("2、正在写出文件")
# 将所有键值对写入一个新文件中
# with open(to_file, 'w', encoding='utf-8') as f:
#     idx = 0
#     for item in origin_arr:
#         idx = idx + 1
#         f.write(item + ';\n')
        # f.write('i18_menu_idx' + str(idx) + ': ' + item + ',\n')

print("3、写出文件完成", to_file)
