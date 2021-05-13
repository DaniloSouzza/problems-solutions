# for this on I decided to use a list approach

def centuryFromYear(year):
    if year % 100 == 0:
        return year / 100
    else:
        return int(str(year / 100).split('.')[0]) + 1