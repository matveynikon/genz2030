from PIL import Image,ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw 
import os, random

c1 = ["beans", "shite", "20 sea horses", "walter", "juan", "helicopter", "rubber"]
c2 = ["helicopter", "ligged...", "candis", "beans", "analog clock", "cheef keef"]
msg = random.choice(c1)
img = Image.open("memes/"+str(random.choice(os.listdir("memes"))))
converter = ImageEnhance.Color(img)
img2 = converter.enhance(30)
img2.save("coom.png")
img2 = Image.open('coom.png')
w, h = img2.size
draw = ImageDraw.Draw(img2)
font = ImageFont.truetype("Neucha-Regular.ttf", 49)
w2, h2 = draw.textsize(msg)
msg2 = random.choice(c2)
w3, h3 = draw.textsize(msg2)
draw.text(((w-w2)/7,(h-h2)/6),msg,(255,255,255),font=font)
draw.text(((w-w3)/7,(h-h3)/1.5),msg2,(255,255,255),font=font)
img2.save("coom2.png")
