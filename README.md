# tr - Offline OCR
Tested under Python3 with *Ubuntu 16.04* and *Ubuntu 18.04*

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

#### Requirements
<pre>pip install numpy Pillow
</pre>
#### Install
+ 安装方法一
<pre>git clone https://github.com/myhub/tr.git
cd ./tr
sudo python setup.py install
</pre>
+ 安装方法二
<pre>pip install git+https://github.com/myhub/tr.git@master
</pre>
+ 测试是否安装成功
<pre>python test.py
python test_angle.py
</pre>

#### How To Use?
<pre>import tr

# detect text lines, return list of (x, y, width, height)
print(tr.detect("imgs/web.png"))

# detect text lines with angle, return list of (cx, cy, width, height, angle)
print(tr.detect("imgs/id_card.jpeg", tr.FLAG_ROTATED_RECT))

# recognize text line, return (text, confidence)
print(tr.recognize("imgs/line.png"))

# detect and recognize, return list of ((x, y, width, height), text, confidence)
print(tr.run("imgs/name_card.jpg"))
</pre>

#### Test
https://github.com/myhub/tr/blob/master/test.ipynb
