#This is a simple script used to search every file for a specific string. Enter the search term into the searchTerm
#variable and the starting directory for which you want to begin the search in the starting directory variable.
import subprocess
import os

searchTerm = 'cwmp'
startingDirectory = '/'
allFiles = []

#Loops through all files and adds the file path to a list called allFiles.
for root, dirs, path in os.walk(startingDirectory):
    for path2 in path:
        allFiles.append(root + '/' + path2)

#Iterates through each file
for file in allFiles:
    fileString = ''
    #Runs the string command on each file which times out after 5 seconds
    stringsProcess = subprocess.Popen(["timeout","5", "strings", file], stdout=subprocess.PIPE)
    fileOutput = stringsProcess.stdout.read()

    #If the searchterm is in the output from the strings command, prints the file name and location to the screen.
    if searchTerm in fileOutput:
        print 'Search term in ' + file