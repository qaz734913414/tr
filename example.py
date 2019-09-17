import tr

# detect text lines, return list of (x, y, width, height)
print(tr.detect("imgs/web.png"))

# detect text lines with angle, return list of (cx, cy, width, height, angle)
print(tr.detect("imgs/id_card.jpeg", tr.FLAG_ROTATED_RECT))

# recognize text line, return (text, confidence)
print(tr.recognize("imgs/line.png"))

# detect and recognize, return list of ((x, y, width, height), text, confidence)
print(tr.run("imgs/name_card.jpg"))
