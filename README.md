# JpegCompress  
## 灵感来源
leancloud 实名要求上传照片，但是照片必须小于300k，折腾了很久，就想着写个工具。
## 原理  
使用pillow将jpeg格式的图片通过降低质量的方法压缩到小于指定大小（有损压缩）。  
可以修改 compress.py 中的 STEP 参数调整每次 quality 减少的数值。
## 使用方法  
```
Usage:
./compress.py [<file>] [output] [<size>]
```