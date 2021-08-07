# one more! :)

def makeArrayConsecutive2(statues):

    statues.sort()
    missing = 0
    # here we get the last item for the loop
    last_range = statues[-1] - statues[0]

    for i in range(last_range - 1):
        if statues[i] != statues[i + 1] - 1:
            # here we insert that missing silly statue
            statues.insert(i + 1, statues[i] + 1)
            missing += 1

    return missing
