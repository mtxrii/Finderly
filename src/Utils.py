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

        else:
            dist = iterative_levenshtein(string, compare)
            if dist <= degree:
                similarFinds.append(word)

    return exactFinds, similarFinds


def iterative_levenshtein(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        dist[i][0] = i

    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                 dist[row][col - 1] + 1,  # insertion
                                 dist[row - 1][col - 1] + cost)  # substitution

    return dist[row][col]