# For this one the approach was quite simple.
# - First we loop throught the list in order to discover
# our higest number
# - Finally we loop again getting the higest items

def allLongestStrings(inputArray):

    length, new_list = list(), list()

    for string in inputArray:
        length.append(len(string))

    for string in inputArray:
        if max(length) == len(string):
            new_list.append(string)

    return new_list

