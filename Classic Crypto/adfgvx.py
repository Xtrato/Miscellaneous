#-------------------------------------------------------------------------------
# Name:        ADFGVX Cipher
# Purpose:
#
# Author:      James Woolley
#
# Created:     17/07/2012
# Copyright:   (c) James 2012
# Licence:     Open Source
#-------------------------------------------------------------------------------
from decimal import *
###Creates the base Alphabet which is used for finding preceeding characters from the ciphertext.
##baseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
adfgvx = ['a', 'd', 'f', 'g', 'v', 'x']#List created to assign numerical values to each cipher letter
##polybiusInput = raw_input("Welcome to a ADFGVX encrypter. Firstly, please enter the characters which will become the polybius square used in the encryption process. Thease characters will be placed from top left of the square along each row and finish on the bottom right.")

textToEncode = str(raw_input("Please enter the text you would like to encrypt:"))#User input for the text to be encrypted

##textToEncode = ("short")
inputKey = str(raw_input("Please input the key to be used during the encryption process:"))#User input for the encryption key.
##inputKey = ("key")
key = list(inputKey)
if len(inputKey) < len(textToEncode):#Creates a key string which is the same length as the text to encrypt.
    while len(key) < len(textToEncode):
        for keyChar in inputKey:
                key.append(str(keyChar))
if len(key) > len(textToEncode):
    key = key[0:len(textToEncode)]
    key = list(key)
print key
textToEncode = list(str(textToEncode))#Converts the user inputted text into a list for eaiser lookup.
polybiusInput = ("ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8")
polybiusSquare = []
sliceCount = 0
count = 0
while count < 6:#Iterates through each slice of 5 characters of the string polybiusInput
    polybiusSquare.append(list(polybiusInput[sliceCount:sliceCount + 6]))#Appends the 5 character blocks of user entered text into nexted lists in polybiusSquare variable.
    sliceCount = sliceCount + 6
    count = count + 1
print polybiusSquare
finalSubstitution = []#Used to store the final substituted letters before being fractionated.
substitutionPart = []#Used to store the ciphertext after substitution.
fractionating = []


incrementCounter = 0#used to increment through each list within the polybiusSquare list
for char in textToEncode:
    while incrementCounter < 6:#MABY delete somhow future James
        if polybiusSquare[incrementCounter].count(char) > 0:#if the current incremented list contains the the char to be encoded it finds its substituted ciphertext value (either ADFGVX) and appends it to the substitutionPart list
            substitutionPart.append(adfgvx[incrementCounter])
            substitutionPart.append(adfgvx[polybiusSquare[incrementCounter].index(char)])
            incrementCounter = 0
            break
        else:
            incrementCounter = incrementCounter + 1#executed if the current incremented list does not contain the char so it moves onto the next list.
            continue
print ("Substitution part is:" + "".join(substitutionPart))
splitValue = len(key)#used to indicate where the substituted values wrap round.
incrementCounter = 0
rows = float(len(substitutionPart)) / float(len(inputKey))#calculates the rows so that each substituted letter can be assigned to the correct key letter later on.
if rows > int(rows):#Rounds the row count up and converts the value back to an integer
    rows = int(rows + 1)
else:
    rows = int(rows)
print rows
rowCount = rows
for char in substitutionPart:#used to generate the finalSubstitution list where each letter pair is assigned to the key letter.
    if incrementCounter < splitValue:
        while rowCount < rows:
            finalSubstitution.append([key[incrementCounter],char, substitutionPart[incrementCounter + splitValue]])#########CHANGE THIS WHOLE LOOP STATEMENT TO TAKE INTO EFFECT THE ROWS OF SUBSTITUTED CHARACTERS ADDED TO EACH KEY. ATM IT JUST DOES 2.
            incrementCounter = incrementCounter + 1
finalSubstitution.sort()#Sorts the substituted values by the key(the first element.)

cipherTextList = []
incrementCounter = 0
for char in finalSubstitution:#Appends the letter pairs in order of the key to a list called CipherTextList
    cipherTextList.append(char[1])
    cipherTextList.append(char[2])

cipherText = ''.join(cipherTextList)#Converts the cipherTextList to a String so it can be outputted.

print cipherText
