import math

# https://c-for-dummies.com/blog/?p=2431

def easter(year, month, day):
  
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

