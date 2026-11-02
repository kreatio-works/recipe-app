# ホーム画面用アイコンを作る（鍋と湯気）。使い方: py -3 make_icons.py
import os
from PIL import Image, ImageDraw

here = os.path.dirname(os.path.abspath(__file__))
S = 1024
BG = (184, 80, 28)
FG = (255, 248, 238)

img = Image.new('RGB', (S, S), BG)
d = ImageDraw.Draw(img)
# 鍋の本体・ふた・取っ手
d.rounded_rectangle((232, 500, 792, 800), radius=70, fill=FG)
d.rounded_rectangle((192, 440, 832, 492), radius=26, fill=FG)
d.rounded_rectangle((120, 560, 240, 610), radius=25, fill=FG)
d.rounded_rectangle((784, 560, 904, 610), radius=25, fill=FG)
d.rounded_rectangle((462, 392, 562, 440), radius=24, fill=FG)
# 湯気
for x in (372, 512, 652):
    pts = []
    for i in range(61):
        t = i / 60
        import math
        pts.append((x + 26 * math.sin(t * 2 * math.pi), 340 - t * 150))
    d.line(pts, fill=FG, width=30, joint='curve')
    d.ellipse((pts[0][0] - 15, pts[0][1] - 15, pts[0][0] + 15, pts[0][1] + 15), fill=FG)
    d.ellipse((pts[-1][0] - 15, pts[-1][1] - 15, pts[-1][0] + 15, pts[-1][1] + 15), fill=FG)

for n in (180, 192, 512):
    img.resize((n, n), Image.LANCZOS).save(os.path.join(here, 'icon-%d.png' % n))
print('ok')
