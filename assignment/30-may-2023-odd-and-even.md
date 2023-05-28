homework

odd numbers are 1,3,5,7,9, ...
even numbers are 0,2,4,6,8, ...

 in python a number n is even if:
 
 n % 2 == 0
 
 it is odd if:
 
 n % 2 == 1
 
 assignment:
 
 make three lists:
 
odd = []
even = [] 
numbers = []

use this to create 10 random numbers:

```
for i in range(10):
  numbers.append(random.randint(1,10))
```


then use the range() function to loop
through each number in the list numbers. 

if the number is even
add it to the even list. if it is odd
add it to the odd list.

print the results
