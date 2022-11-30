from PIL import Image, ImageDraw
import re

pole = Image.new('RGB', (540, 960), (0,0,0))
draw = ImageDraw.Draw(pole)

strfilesplit = []
file = open('DS6.txt', "r")
strfile = file.readlines()

for i in range(len(strfile)):
  strfilesplit.append(re.findall(r'\d+', strfile[i]))
  draw.point((int(strfilesplit[i][0]), int(strfilesplit[i][1])), fill="white")

pole.show()