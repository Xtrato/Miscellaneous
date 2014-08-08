#This script performs a twitter search every 3 minutes for the search term “my bbm pin” and saves the pin into a
# results.txt file in the same folder.
#README at https://github.com/Xtrato/Miscellaneous/blob/master/Readme%27s/bbmPinEnumerator.md
import twitter
import string
import re
import time
api = twitter.Api(consumer_key ='YOUR_KEY',  consumer_secret='YOUR_SECRET',  access_token_key='YOUR_ACCESS_KEY',  access_token_secret='YOUR_ACCESS_SECRET') #Enter your Twitter API details here.
loopControl = True
while loopControl == True: #used to keep the programming running
    bbmPins = api.GetSearch(term='my bbm pin') #The search term sent to the twitter API
    for bbm in bbmPins:
        status =  bbm.GetText().encode('utf-8') #Converts the unicode string returned by the API to UTF-8. this allows for punctuation to be removed more easily.
        statusNoPunct = status.translate(None, string.punctuation).lower() #Removes the punctuation and converts the statuses to lower case.
        wordList = statusNoPunct.split() #Splits the statuses into individual words.
        for word in wordList:
            if len(word) == 8: #Checks if the word in 8 characters long. (BBM pins are 8 characters long).
                #Filters out any non-hexadecimal words (BBM pins are hexadecimal)
                if not 'g' in word and not 'h' in word and not 'i' in word and not 'j' in word and not 'k' in word and not 'l' in word and not 'm' in word and not 'n' in word and not 'o' in word and not 'p' in word and not 'q' in word and not 'r' in word and not 's' in word and not 't' in word and not 'u' in word and not 'v' in word and not 'w' in word and not 'x' in word and not 'y' in word and not 'z' in word:
                    results = open('results.txt', 'a+')
                    if not word in results.read(): #Checks if the pin already exists in the file
                        results.write(word + "\n") #Writes the pin to the file
                        results.close()
                    print word
            if len(word) == 11: #Some people posted the BBM pins as so Pin:25B46EE0. With the : and . omitted in line 11 this will be 11 characters long.
                if 'pin' in word:
                    sliceWord = word[3: len(word)] #Strips the word "pin" from the beginning of the pin (pin25B46EE0 > 25B46EE0)
                    results = open('results.txt', 'a+')
                    if not sliceWord in results.read(): #Checks if the pin already exists in the file.
                        results.write(sliceWord + "\n") #Writes the pin to the file
                        results.close()
                    print sliceWord
    time.sleep(180) #sleep for 3 minutes before starting again.