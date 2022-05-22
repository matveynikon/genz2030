from PIL import Image,ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw 

msg = "I ligged on deez nuts"
img = Image.open('wedmadudes.png')
converter = ImageEnhance.Color(img)
img2 = converter.enhance(30)
img2.save("coom.png")
img2 = Image.open('coom.png')
w, h = img2.size
draw = ImageDraw.Draw(img2)
font = ImageFont.truetype("Neucha-Regular.ttf", 49)
w2, h2 = draw.textsize(msg)
msg2 = "whats next?"
w3, h3 = draw.textsize(msg2)
draw.text(((w-w2)/7,40),msg,(255,255,255),font=font)
draw.text(((w-w3)/7,420),msg2,(255,255,255),font=font)
img2.save("coom2.png")
