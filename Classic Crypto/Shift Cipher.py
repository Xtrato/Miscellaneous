#-------------------------------------------------------------------------------
# Name:        Ceaser Shift Cipher
# Purpose:      Example code for analysing shifts on plain text by a Caesar shift cipher.
#
# Author:      James Woolley
#
# Created:     14/06/2012
# Copyright:   Open Source
#-------------------------------------------------------------------------------
#Creates the base Alphabet which is used for finding preceeding characters from the ciphertext.
baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print ("Welcome to a python Caesar shift cipher analyser. You will first be asked to enter the cipher text to be decrypted and then the amount of shifts you want to perform. Entering ALL for the shift amount will iterate through all 26 combinations.")
cipherText = raw_input("Please enter the Cipher text")
shiftAmount = raw_input("Please enter the shift amount. Enter ALL for brute force shifting.")
if shiftAmount == "all":
    shiftAmount = str(shiftAmount)
else:
    shiftAmount = int(shiftAmount)
baseLetterIndex = 0
completePlainText = [] #The variable each processed letter is appended to
def shiftAndStore(shift):
    for increment in cipherText:
        for value in baseAlphabet:
                    if value == increment:
                            while shift + baseAlphabet.index(value) >= 26: #Checks if the shift will be higher more than the 26 letters of the alphabet.
                                shift = shift - 26 #If shifts are higher 26 is subtracted till the shift and base alphabet value is lower than 26.
                            baseLetterIndex = baseAlphabet.index(value) + shift #assigns the index value of the processed letter to baseLetterIndex variable.
                            completePlainText.append(baseAlphabet[baseLetterIndex]) # appends the processed letter to the completePlainText variable.
                    if increment == (" "): #Handles the spaces Temporarily makes the value of increment X to prevent it looping 26 times.
                        completePlainText.append(" ")
                        increment = ("X")


if shiftAmount == "all": #Checks weather user selected brute force method or specific shift value.
    shiftAmount = int(0)
    while shiftAmount < 25: #Iterates through all 26 combinations producing a processed value each time.
        shiftAndStore(shiftAmount)
        shiftAmount = shiftAmount + 1
        print "The Encoded / Decoded text on shift  " + str(shiftAmount - 1) + " is " + (''.join(completePlainText)) #Prints the shift amount and processed text.
        completePlainText = []
else: #Executed if specific shift value is chosen and not brute force.
    shiftAndStore(shiftAmount)
    print "The Shift Amount is " + str(shiftAmount)
    print "The Encoded / Decoded text is " + (''.join(completePlainText))
