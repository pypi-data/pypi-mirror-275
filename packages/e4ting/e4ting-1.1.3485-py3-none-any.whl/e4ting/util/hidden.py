#!/bin/python3
# -*- coding:utf-8 -*-
"""
    隐写术（steganography） 模块
    Add By :陈狍子 e4ting@qq.com 2024-05-25 23:23:32
"""
import sys,os
from pdb import set_trace as strace
from traceback  import format_exc as dumpstack
from e4ting import util,log

class Hidden():
    def read(self):
        import piexif
        exif_data = piexif.load("one_pixel.jpg")

        sign = exif_data["0th"].get(piexif.ImageIFD.Artist)
        if sign:
            log.info( sign.decode("utf-8"))

        user_comment = exif_data["Exif"].get(piexif.ExifIFD.UserComment)
        if user_comment:
            return user_comment.decode("utf-8")
        else:
            return "No user comment found in EXIF data."


    def write(self):
        import piexif
        # 载入JPEG图片的EXIF数据
        exif_dict = piexif.load("one_pixel.jpg")

        # 将文件作为二进制数据读入
        with open("__init__.py", "rb") as f:
            file_data = f.read()

        # 将二进制数据存储在EXIF注释字段中
        exif_dict["Exif"][piexif.ExifIFD.UserComment] = file_data
        # strace()
        # exif_dict["Exif"][piexif.ExifIFD.Copyright] = "e4ting"
        exif_dict['0th'][piexif.ImageIFD.Artist] = util.md5sum("__init__.py")

        # 将修改后的EXIF数据写回图片
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, "one_pixel.jpg")

    def create_one_pixel(self):
        from PIL import Image

        # 创建一个只有1个像素的图像，颜色为白色
        img = Image.new('RGB', (1, 1), color = 'white')

        # 保存图像为JPEG格式
        img.save('one_pixel.jpg', 'JPEG')


if __name__ == '__main__':
    # Hidden().create_one_pixel()
    Hidden().write()
    data = Hidden().read()
    log.info(data)