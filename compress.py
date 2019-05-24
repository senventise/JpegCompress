#!/usr/bin/python3
import sys
import os
from PIL import Image

STEP = 5 # 每次quality减小的数值


def print_help():
    tip = """Usage:
./compress.py [<file>] [output] [<size>]"""
    print(tip)


if len(sys.argv) == 3 or len(sys.argv) ==4:
    l = len(sys.argv)
    try:
        target_size = int(sys.argv[l-1]) * 1024 # 尺寸
    except(ValueError):
        # 尺寸无法转为 int
        print(f"Invaild argument: {sys.argv[l-1]} (size should be a integer)\n")
        print_help()
        sys.exit(22)
    # 判断文件是否存在
    if os.path.exists(sys.argv[1]):
        name = sys.argv[1] # 文件名
        # 比较文件大小与预期大小
        f = open(name,"rb")
        if len(f.read()) <= target_size:
            print(f"Invaild argument: {sys.argv[l-1]} (Target size is greater than actual size)\n")
            print_help()
            f.close()
            sys.exit(22)
        f.close()
    else:
        # 文件不存在
        print(f"No such file or directory: {sys.argv[1]}\n")
        print_help()
        sys.exit(2)
else:
    print_help()
    sys.exit(22)


img = Image.open(name)
if not img.format == "JPEG":
    print(f"Invaild argument: {sys.argv[2]} (uncorrect format)\n")
    print_help()
    sys.exit(22)
quality = 95
while(True):
    img.save("temp.jpeg",quality=quality)
    with open("temp.jpeg","rb") as f:
        if len(f.read()) <= target_size:
            if l == 3:
                img.save(name,quality=quality)
            elif l == 4:
                img.save(sys.argv[2],quality=quality)
            print(f"Success.\nQuality:{quality}")
            os.remove("temp.jpeg")
            break;
        else:
            quality = quality - STEP
    