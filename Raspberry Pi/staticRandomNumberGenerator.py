#This program is used to calculate a random number using the static from an analogue TV signal. It outputs the number
#to outpux.txt. More information: http://jamesdotcom.com/?p=417
import Image
import subprocess
devNull = open('/dev/null', 'w')
name = 0
while True:
    name = name + 1
    randomBits = ""
    pixelRow = 0
    pixelColumn = 0
    captureImage = subprocess.Popen(["fswebcam", "-r", "356x292", "-d", "/dev/video0", "static.jpg", "--skip", "10"], stdout=devNull, stderr=devNull)
    captureImage.communicate()
    staticImage = Image.open("static.jpg")
    bW_Image = staticImage.convert('1')
    bW_Image.save('bw' + str(name) + '.jpg')
    imageToProcess = bW_Image.load()
    while pixelRow < staticImage.size[0]:
        while pixelColumn < staticImage.size[1]:
            if imageToProcess[pixelRow, pixelColumn] == 0:
                randomBits = randomBits + "0"
            else:
                randomBits = randomBits + "1"
            pixelColumn = pixelColumn + 1
        pixelRow = pixelRow + 1
        pixelColumn = 0
    output = open('output.txt', 'w')
    output.write(str(int(randomBits, 2)))
    print int(randomBits, 2)
    output.close()