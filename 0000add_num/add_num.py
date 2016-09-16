# coding=utf-8
# Author:paukey
# Date:2016-9-16
# python 2.7(PIL)

"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果(暂无save)
"""

import Image
import ImageDraw
import ImageFont


def draw_number(sjx, number):
    image = Image.open(sjx)
    pos = (image.size[0] - 90, 0)
    font = ImageFont.truetype('arial.ttf', 140)

    draw = ImageDraw.Draw(image)
    draw.text(pos, number, fill=(255, 0, 0), font=font)

    image.show()


#    image.save()


if __name__ == '__main__':
    draw_number("sjx.jpg", "2")
