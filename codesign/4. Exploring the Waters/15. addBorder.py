def addBorder(picture):

    portrait = []

    starline = (len(picture[0])+2) * "*"

    portrait.append(starline)

    for i in range(len(picture)):
        portrait.append('*'+picture[i]+'*')

    portrait.append(starline)
    
    return portrait