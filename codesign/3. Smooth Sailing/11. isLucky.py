# One more :)

def isLucky(n):

    ticket = [int(x) for x in str(n)]
    return sum(ticket[int(len(ticket)/2):]) == sum(ticket[:int(len(ticket)/2)])
