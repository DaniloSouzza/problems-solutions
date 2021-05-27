# this one is easy but some kind tricky for new programmers
# I decide to input all pair sums into a list and then our champ :)

def adjacentElementsProduct(inputArray):
    sums = []
    for i in range(len(inputArray)):
        if i != 0:
            sums.append(inputArray[i] * inputArray[i - 1])
            
    return max(sums)