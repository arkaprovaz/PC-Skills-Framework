import os, platform
from PIL import Image, ImageDraw, ImageFont
import path

os_info = "OS name: " + os.name
cpu_count = "CPU count: " + str(os.cpu_count()) 
cpu_info = platform.processor()
system_info = "System: " + platform.system() 
release_info = "Release: " + platform.release() 
arch_info = "Architecture: " + str(platform.architecture())


left_margin = 40
top_margin = 50
gap = 30

img = Image.new('RGB', (500, 500), color = (0, 0, 0))
 
fnt = ImageFont.truetype(path.path + 'resources/Arial.ttf', 18)
d = ImageDraw.Draw(img)
c = top_margin
d.text((left_margin, c), "PC Information", font=fnt, fill=(255, 255, 0))
c = top_margin+15
d.text((left_margin, c), "------------------------------------", font=fnt, fill=(255, 255, 0))
c = c + 2*gap
d.text((left_margin, c), os_info, font=fnt, fill=(255, 255, 255))
c = c + gap
d.text((left_margin, c), cpu_count, font=fnt, fill=(255, 255, 255))
c = c + gap
d.text((left_margin, c), cpu_info, font=fnt, fill=(255, 255, 255))
c = c + gap*3
d.text((left_margin, c), "Platform------", font=fnt, fill=(255, 255, 255))
c = c + gap
d.text((left_margin, c), system_info, font=fnt, fill=(255, 255, 255))
c = c + gap
d.text((left_margin, c), release_info, font=fnt, fill=(255, 255, 255))
c = c + gap
d.text((left_margin, c), arch_info, font=fnt, fill=(255, 255, 255))
c = c + 3*gap
d.text((left_margin+280, c), "#PCSkills", font=fnt, fill=(0, 255, 255))
img.save(path.path + 'pc_info.jpg')

taskvalue = 'python ' + path.path + 'tweetomatic.py -i ' + path.path + 'pc_info.jpg' + ' -t "Tweeting PC info! #PCSkills"'
os.system(taskvalue)
#os.system('python tweetomatic.py -i .\pc_info.jpg -t "Tweeting PC info! #PCSkills"')