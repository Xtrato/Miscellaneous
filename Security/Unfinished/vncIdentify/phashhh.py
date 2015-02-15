#This script generates a fuzzy hash for a VNC screen capture.
from PIL import Image
import os
import imagehash
import ssdeep

screenshotPath = '/root/Desktop/vnchash/arena/'

for file in os.listdir(screenshotPath):
    screenshot = Image.open(screenshotPath + file)
    screenshot = screenshot.resize((10, 10))
    screenshot = screenshot.convert('P', palette=Image.ADAPTIVE, colors=20)

    hash = imagehash.dhash(screenshot)


    print str(hash) + '            ' + file

def hashFileCreator():
    screenshot = Image.open('/root/Desktop/vnchash/ubuntu/ubuntu200.17.220.25%3A02.jpg')
    screenshot = screenshot.resize((100, 100))
    screenshot = screenshot.convert('P', palette=Image.ADAPTIVE, colors=10)
    screenshot.save('/root/Desktop/vnchash/ubuntu/compressed.gif')
    hash = ssdeep.hash_from_file('/root/Desktop/vnchash/ubuntu/compressed.gif')
    print hash

def compareHashes()
    hashone = ssdeep.hash_from_file('/root/Desktop/vnchash/win7/win7hash.jpg')
    hashtwo = ssdeep.hash_from_file('/root/Desktop/vnchash/win7/win7hash.jpg-temp.jpg')

    print hashone
    print hashtwo

    print ssdeep.compare(hashone, hashtwo)

compareHashes()