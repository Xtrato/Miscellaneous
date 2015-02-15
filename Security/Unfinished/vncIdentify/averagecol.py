#This script attempts to identify VNS screen captures based on the average image colour.
import ssdeep
import os
from PIL import Image


def hashgen(path, fileName):
    screenshot = Image.open(path + fileName)
    screenshot = screenshot.resize((10, 10))
    screenshot = screenshot.convert('P', palette=Image.ADAPTIVE, colors=3)
    screenshot.save(path + 'compressed.gif')
    hash = ssdeep.hash_from_file(path + 'compressed.gif')
    os.remove(path + 'compressed.gif')
    return hash

def averageColour(path, fileName):
    screenshot = Image.open(path + fileName)
    width, height = screenshot.size
    totalsize = width * height
    data = []
    red = 0
    green = 0
    blue = 0
    image = screenshot.load()
    for x in range(width):
        for y in range(height):
            data.append(image[x, y])
    for pix in data:
        red = red + pix[0]
        green = green + pix[1]
        blue = blue + pix[2]
    red = red / totalsize
    green = green / totalsize
    blue = blue / totalsize
    return red, green, blue

def checker(rgb, comparitor):
    red = abs(rgb[0] - comparitor[0])
    green = abs(rgb[1] - comparitor[1])
    blue = abs(rgb[2] - comparitor[2])
    return red, green, blue



screenshotPath = '/root/Desktop/vnchash/arena/'

windows7Hash = (52, 142, 202)
ubuntuHash = (144, 70, 79)
danfossHash = (181, 179, 181)
terminalHash = (10, 10, 10)
server2003Hash =
print windows7Hash

for file in os.listdir(screenshotPath):
    found = False
    hash = averageColour(screenshotPath, file)
    if abs(hash[0] - windows7Hash[0]) < 40 and abs(hash[1] - windows7Hash[1]) < 40 and abs(hash[2] - windows7Hash[2]) < 40:
        print 'THIS IS WINDOWS 7' + '              ' + file
        found = True
    if abs(hash[0] - ubuntuHash[0]) < 40 and abs(hash[1] - ubuntuHash[1]) < 40 and abs(hash[2] - ubuntuHash[2]) < 40:
        print 'THIS IS UBUNTU' + '              ' + file
        found = True
    if found == False:
        print 'I DONT KNOW!!1'
    #total = hash[0] + hash[1] + hash[2]

    #print file + '           ' + str(hash) + '              ' + str(total)

print 'End'