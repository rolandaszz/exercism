import datetime

#def is_leap_year(year):

def is_leap_year(year):
    isleap = False

    #validate year
    #https://www.tutorialspoint.com/How-to-do-date-validation-in-Python

    yearf = '%Y'

    try:
        date_check = datetime.datetime.strptime(str(year), yearf)
        print('Entry:', date_check.year)
    except ValueError:
        print('Incorrect year format! Accepted values are [0001, 9999]')

    #on every year that is evenly divisible by 4
    #except every year that is evenly divisible by 100
    #unless the year is also evenly divisible by 400
    if int(year) >= 400 and int(year) % 400 == 0:
        isleap = True
    elif int(year) >= 100 and int(year) % 100 == 0:
        isleap = False
    elif int(year) % 4 == 0:
        isleap = True
    else:
        isleap = False

    return isleap
