# Finderly main file
#
# Author: Enrique (@Mtxrii)
# Date created: 4/16/20

# -------------------------[ main program ]------------------------- #
from src.Utils import search, index, macroReplace

print("Hello.", end=" ")

done = False # for outer loop
fExists = False # for find file loop
file = None
fileName = ''
allWords = []
deg = 2 # degree of similarity,
        # refers to # of chars that can be different for the 'similar' words

while not done: # outer loop

    while not fExists: # find file loop
        fileName = input("Please input a file name to scan: ")

        if fileName == "-q":
            raise SystemExit

        try:
            file = open(fileName, "r")
            fExists = True
            print("file '" + fileName + "' has been read & indexed. \n")
        except IOError:
            print("\nFile '" + fileName + "' could not be found.")


    allWords = index(file, allWords)

    print("What would you like to do?")
    cmd = input("'-s <string>' to search, \n'-d <number>' to set degree of similarity, \n'-n' to open another file, \n'-q' to quit \n")
    print("") # \n

    if   cmd[:2] == "-q":
        done = True

    elif cmd[:2] == "-n":
        fExists = False

    elif cmd[:2] == "-d":
        try:
            deg = abs(int(cmd[3:]))
            print("Degree set to " + str(deg))
        except ValueError:
            print("Please put an integer after '-d'")

    elif cmd[:2] == "-s":
        word = cmd[3:] + " .|."
        word = word.split()[0]

        if word == ".|.":
            print("Please put a word after '-s")

        else:
            exact, similar = search(word, allWords, deg)
            print("Words found containing '" + word + "' -> " +   macroReplace(str(exact), ['[', ']']) + "\n")
            print("Words found similar to '" + word + "' -> " + macroReplace(str(similar), ['[', ']']) + "\n")

