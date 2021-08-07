# I created two slices and these slices are separates in two
# these two are are compared if the first number is equal to second
# in order to check the ascending order.
# After that If first is equals or major to second we insert 1 and then,
# finally, check If we have a number lower than 1.

def almostIncreasingSequence(sequence):

    slice2 = sum(
                [1 for x, y
                 in zip(sequence[:-2], sequence[2:])
                 if x >= y]) <= 1

    slice1 = sum(
                [1 for x, y
                 in zip(sequence[:-1], sequence[1:])
                 if x >= y]) <= 1

    return slice1 and slice2
