import math


def easter(year):
  
    Y = year
    a = Y%19
    b = math.floor(Y/100)
    c = Y%100
    d = math.floor(b/4)
    e = b%4
    f = math.floor((b+8)/25)
    g = math.floor((b-f+1)/3)
    h = (19*a+b-d-g+15)%30
    i = math.floor(c/4)
    k = c%4
    L = (32+2*e+2*i-h-k)%7;
    m = math.floor((a+11*h+22*L)/451)
    month = math.floor((h+L-7*m+114)/31)
    day = ((h+L-7*m+114)%31)+1
    
    return year, month, day
  
  
 easter(2021)

  # convert Gregorian to Julian
  # assignment is to calculate easter for next 10 years in gregorian and julian formats
  # pip install jdcal
  # https://pypi.org/project/jdcal/
  
  # find algorithm to calculate Ramadan
  

