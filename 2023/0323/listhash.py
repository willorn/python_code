import hashlib
import os
import time


def get_file_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_dir_files_md5(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            md5 = get_file_md5(file_path)
            # if md5 == "e19514644951229bc0668d14623fce6b":
            #     print("我找到了，就是下面的这个")
            #     time.sleep(100000)
            print(f"{file_path} md5: {md5}")


if __name__ == '__main__':
    # dir_path = r'D:\download\pty_sdf_[1]_20230323113729\source'
    dir_path = r'D:\download\dingding\Classify_0\source'
    get_dir_files_md5(dir_path)
# e19514644951229bc0668d14623fce6b
