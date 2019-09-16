# coding: utf-8
from tr import *
from PIL import Image, ImageDraw, ImageFont
import cv2

if __name__ == "__main__":
    # img_path = "imgs/name_card.jpg"
    img_path = "imgs/id_card.jpeg"

    img_pil = Image.open(img_path)
    MAX_SIZE = 2000
    if img_pil.height > MAX_SIZE or img_pil.width > MAX_SIZE:
        scale = max(img_pil.height / MAX_SIZE, img_pil.width / MAX_SIZE)

        new_width = int(img_pil.width / scale + 0.5)
        new_height = int(img_pil.height / scale + 0.5)
        img_pil = img_pil.resize((new_width, new_height), Image.BICUBIC)

    print(img_pil.width, img_pil.height)

    color_pil = img_pil.convert("RGB")
    gray_pil = img_pil.convert("L")

    rect_arr = detect(gray_pil, FLAG_ROTATED_RECT)

    img_draw = ImageDraw.Draw(color_pil)
    colors = ['red', 'green', 'blue', "purple"]

    for i, rect in enumerate(rect_arr):
        x, y, w, h, a = rect
        box = cv2.boxPoints(((x, y), (w, h), a))
        box = numpy.int0(box)
        img_draw.line(xy=(box[0][0], box[0][1], box[1][0], box[1][1]), fill=colors[i % len(colors)], width=2)
        img_draw.line(xy=(box[1][0], box[1][1], box[2][0], box[2][1]), fill=colors[i % len(colors)], width=2)
        img_draw.line(xy=(box[2][0], box[2][1], box[3][0], box[3][1]), fill=colors[i % len(colors)], width=2)
        img_draw.line(xy=(box[3][0], box[3][1], box[0][0], box[0][1]), fill=colors[i % len(colors)], width=2)

    color_pil.save("~color_pil.png")
    color_pil.show()


