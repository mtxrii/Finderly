# Finderly utility functions file
#
# Author: Enrique (@Mtxrii)
# Date created: 4/16/20

# -------------------------[ search tools ]------------------------- #

def macroReplace(string_to_edit, list_of_chars, char_to_replace=""):
    for c in list_of_chars:
        string_to_edit = string_to_edit.replace(c, char_to_replace)
    return string_to_edit



def index(file_to_unpack, list_to_append):

    for line, lineContents in enumerate(file_to_unpack):
        lineContents = lineContents.replace("\n", "")

        for l in lineContents.split():
            l = macroReplace(l, [',', '.', '"'])
            list_to_append.append(str(l) + " (" + str(file_to_unpack.name) + ":" + str(line) + ")")

    return list_to_append



def search(string, list_of_strings, degree):
    exactFinds = []
    similarFinds = []

    for word in list_of_strings:
        compare = word.split()[0]
        if string in compare:
            exactFinds.append(word)
        elif compare in string:
            exactFinds.append(word)


    return exactFinds, similarFinds
