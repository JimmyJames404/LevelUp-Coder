import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

name = "Jimmy J"

im = Image.open(r'certificate\template.png')
d = ImageDraw.Draw(im)
location = (100, 398)
text_color = (0, 137, 209)
font = ImageFont.truetype("arial.ttf", 70)
d.text(location, name, fill = text_color, font = font)
im.save("certificato_" + name + ".pdf")
os.startfile("certificato_" + name + ".pdf")
