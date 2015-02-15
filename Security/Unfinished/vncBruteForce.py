#A work in progress, An attempt to interact with the VNC servers authentication process.
import binascii

password = 'testing1'

def bitflip(password):
    #convert the password to hexidecimal.
    hexPassword = binascii.hexlify(password)
    #Convert the hexidecimal to binary form without the prepending 0b.
    binaryPassword = bin(int(hexPassword, 16)).replace('0b', '0')

    current = 0
    flipped = ''
    #Iterate through the binaryPassword one byte at a time, Reverse the order of bits and append to the flipped string.
    while current <= len(binaryPassword):
        flipped = flipped + binaryPassword[current:current+8][::-1]
        current += 8
    print flipped
    #Convert the flipped binary digits back to hexidecimal and remove the prepending 0x and spaces.
    flippedHex =  hex(int(flipped, 2)).replace('0x', '0').replace(' ', '')[:-1]

    #Add padding 0's to the end of the password to make it 8 bytes in length.
    while len(flippedHex) < 16:
        flippedHex = flippedHex + '0'

    print flippedHex


bitflip(password)