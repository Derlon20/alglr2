from PIL import Image, ImageDraw

pole = Image.new('RGB', (540, 960), (255,255,220))
draw = ImageDraw.Draw(pole)

strfilesplit = []
file = open('DS6.txt')
strfile = file.readlines()

for i in range(len(strfile)):
  line = strfile[i]
  dot = line.split(" ")
  draw.point((int(dot[0]), int(dot[1])), fill=(0,155,75))

pole.save('picture.png', 'PNG')
