#This script attempts to identify VNS screen captures based on the average image colour.
import os
from PIL import Image

averageHashes = [['Terminal', (182, 183, 183)],
['Ubuntu Hash', (191, 103, 103)],
['Windows Server 2003', (195, 194, 203)],
['Windows Server 2008', (176, 193, 197)],
['Windows 7', (118, 209, 233)],
['Danfoss', (228, 229, 230)],
]


def averageColour(path, fileName):
    screenshot = Image.open(path + fileName)
    width, height = screenshot.size
    red = 0
    green = 0
    blue = 0
    counter = 0
    image = screenshot.load()
    for x in range(width):
        for y in range(height):
            if image[x, y][0] > 50 and image[x, y][1] > 50 and image[x, y][2] > 50:
                red = red + image[x, y][0]
                green = green + image[x, y][1]
                blue = blue + image[x, y][2]
                counter = counter + 1
    red = red / counter
    green = green / counter
    blue = blue / counter
    return red, green, blue



def averageHashCalculator(screenshotPath):
    red = 0
    green = 0
    blue = 0

    for file in os.listdir(screenshotPath):
        hash = averageColour(screenshotPath, file)

        red = red + hash[0]
        green = green + hash[1]
        blue = blue + hash[2]

    red = red / len(os.listdir(screenshotPath))
    green = green / len(os.listdir(screenshotPath))
    blue = blue / len(os.listdir(screenshotPath))
    hash = (red, green, blue)

    print 'Your RGB value for this group of screenshots is:' + str(hash)


def main(screenshotPath):
    for file in os.listdir(screenshotPath):
        hash = averageColour(screenshotPath, file)

        for averageHash in averageHashes:
            if abs(hash[0] - averageHash[1][0]) < 40 and abs(hash[0] - averageHash[1][1]) < 40 and abs(hash[0] - averageHash[1][2]) < 40:
                print str(averageHash) + '                  ' + str(file)



#averageHashCalculator('/root/Desktop/vnchash/danfoss/')

main('/root/Desktop/vnchash/arena/')