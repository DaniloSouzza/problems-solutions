# I took sometime to think abou this...(actually took a lot of time u.u)
# so I decided to split once we have a symetric pattern
# after get all 4 sides we put our little center square at coune :)

def shapeArea(n):
    
    center =  n - 1
    diagonals = 0
    
    for x in range(1, center):
        diagonals += x

    return 4 * (diagonals + center) + 1