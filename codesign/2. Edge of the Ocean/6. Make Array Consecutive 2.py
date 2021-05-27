# one more! :)

def makeArrayConsecutive2(statues):

    statues.sort()
    
    missing = 0

    last_range = statues[-1] - statues[0] # here we get the last item for the loop

    for i in range(last_range - 1):
        if statues[i] != statues[i + 1] - 1:
            statues.insert(i + 1, statues[i] + 1) # here we insert that missing silly statue
            missing += 1

    return missing
