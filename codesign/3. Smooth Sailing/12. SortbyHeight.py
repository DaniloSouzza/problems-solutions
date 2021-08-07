def sortByHeight(a):
    # here we're mapping our trees
    trees = [x for x in range(len(a)) if a[x] < 0]
    # let's remove them for a while :x
    while -1 in a:
        a.remove(-1)
    # organizing the line
    a.sort()
    # ok tree, you can go back!
    [a.insert(z, -1) for z in trees]

    return a
