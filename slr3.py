from PIL import Image, ImageDraw
import math

n = 6
pole = Image.new('RGB', (960, 960), (255,255,220))
angle = 10*(n+1)*math.pi/180
draw = ImageDraw.Draw(pole)

strfilesplit = []
file = open('DS6.txt')
cordgiven = file.readlines()

for i in range(len(cordgiven)):
  line = cordgiven[i]
  cordread = line.split(" ")
  
  x = 480 + (int(cordread[0])-480)*math.cos(angle) - (int(cordread[1])-480)*math.sin(angle)
  y = 480 + (int(cordread[0])-480)*math.sin(angle) + (int(cordread[1])-480)*math.cos(angle)
  
  draw.point((int(round(x,0)), int(round(y,0))), fill=(0,155,75))

pole.save('picture.png', 'PNG')
