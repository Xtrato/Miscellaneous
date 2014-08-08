#-------------------------------------------------------------------------------
# Name:        Frequency Analysis
# Purpose:     Count the amount of n-grams in ciphertext
#
# Author:      James Woolley
#
# Created:     28/06/2012
# Copyright:   (c) James 2012
# Licence:     Open Source
#-------------------------------------------------------------------------------
inputText = str(raw_input("Please enter the cipher text to be analysed:")).replace(" ", "") #Input used to enter the cipher text. replace used to strip whitespace.
ngramDict = {}
highestValue = 0
def ngram(n): #Function used to populate ngramDict with n-grams. The argument is the amount of characters per n-gram.
    count = 0
    for letter in inputText:
        if str(inputText[count : count + n]) in ngramDict: #Check if the current n-gram is in ngramDict
            ngramDict[str(inputText[count : count + n])] = ngramDict[str(inputText[count : count + n])] + 1 #increments its value by 1
        else:
            ngramDict[str(inputText[count : count + n])] = 1 #Adds the n-gram and assigns it the value 1
        count = count + 1
    for bigram in ngramDict.keys(): #Iterates over the Bigram dict and removes any values which are less than the adaquate size (< n argument in function)
        if len(bigram) < n:
            del ngramDict[bigram]
ngram(int(raw_input("Please enter the n-gram value. (eg bigrams = 2 trigrams = 3)")))
ngramList = [ (v,k) for k,v in ngramDict.iteritems() ] #iterates through the ngramDict. Swaps the keys and values and places them in a tuple which is in a list to be sorted.
ngramList.sort(reverse=True) #Sorts the list by the value of the tuple
for v,k in ngramList: #Iterates through the list and prints the ngram along with the amount of occurrences
    print("There are " + str(v) + " " + str(k))