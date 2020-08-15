def factorial(x):
    z=x
    for i in range(x-1,0,-1):
        z=z*i
    return z

def sine(x):
    
    return x - (x**3)/factorial(3) + (x**5)/factorial(5) - (x**7)/factorial(7) + (x**9)/factorial(9)
