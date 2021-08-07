# This was a easy one. First we get the minimum similar char
# between the two entries and put it into `counter` list
# and then we just sum :)

def commonCharacterCount(s1, s2):

    items, counter = set(s1), list()

    for char in items:
        counter.append(min(s1.count(char), s2.count(char)))

    return sum(counter)
