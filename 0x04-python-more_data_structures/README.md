# lambda, map, filter and reduce functions

1. <ins>**lambda funnction**</ins>

lambda is a function that does not have a name.

lambda return returns memory to address object class lambda

## Declaration

```py
lambda argument(s) : expression
```

**Examples**
<hr>
`lambda1.py`

```py
#!/usr/bin/python3

#Using lambda to find the square of a number

x = lambda x : x*x
print(x(5)) #25
```

`lambda2.py`

```py
#!/usr/bin/python3

#Using lambda to cube a number
x = lambda n : n*n*n
print(x(3)) #27
```
`lambda3.py`

```py
#!/usr/bin/python3

#Using lambda to find number is even or odd
#prints True if number is even else false

x = lambda x : x if True % 2 == 0 else False
print(x(5)) #False
```
<hr><br>

2. <ins>**map function**</ins>

map is a function that takes in two arguments, a function, and an iterable. It loops through the iterable passing each of its elemnts in the function. iterable can be a list or a tuple.

## Declaration

```py
map(function, iterable)
```

Example without using map
<hr>

`without_map.py`

```py
#!/usr/bin/python3

def squareit(n):
    return n*n

my_numbers = [2,3,4,5,6,7,8,9]
squared_numbers = []

def square_func(afunc, alist):
    for element in alist:
        squared_numbers.append(afunc(element))

square_func(squareit, my_numbers)
print(squared_numbers)

#[4, 9, 16, 25, 36, 49, 64, 81]
```

`with_map.py`
```py
#!/usr/bin/python3

def squareit(n):
    return n*n

my_numbers = [2,3,4,5,6,7,8,9]
result = list(map(squareit, my_numbers))
print(result)

#[4, 9, 16, 25, 36, 49, 64, 81]
```

map loops through the members of the iterable and pass `each` to the function. Note that map returns the memory address of object class map, the place in memory where the map is stored. with that address we can't do much so we coonvert it to another data structure that is viewable for our case a list. so it's return is now being stored in a list.

`without_map2.py`

```py
#!/usr/bin/python3

def even_func(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
numbers = [0,1,2,3,4,5,6,7,8,9,10,20,55,79]
even_only = []
odd_only = []

def odd_or_even(afunc, alist):
    for i in alist:
        if afunc(i):
            even_only.append(i)
        else:
            odd_only.append(i)
odd_or_even(even_func, numbers)
print("Even: {}".format(even_only))
print("Odd: {}".format(odd_only))

# Even: [0, 2, 4, 6, 8, 10, 20]
# Odd: [1, 3, 5, 7, 9, 55, 79]
```

`with_map.py`

```py
#!/usr/bin/python3

def even_func(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
numbers = [0,1,2,3,4,5,6,7,8,9,10,20,55,79]
result = list(map(even_func, numbers))
print(result)
#[True, False, True, False, True, False, True, False, True, False, True, True, False, False]
```
<hr>
implementing the above with lambda and map

`map_and_lambda.py`

```py
#!/usr/bin/python3

numbers = [0,1,2,3,4,5,6,7,8,9,10,20,55,79]
result = list(map((lambda x: True if x % 2 == 0 else False), numbers))

#[True, False, True, False, True, False, True, False, True, False, True, True, False, False]
```
**Map can also be used with builtin python functions like len, capitalize, upper, lower, title etc**

lets look at some examples

<hr>

`map_with_len.py`

```py
#!/usr/bin/python3

# return a list with the length count of each string length
my_strings = ["Dut", "python", "apple","linux"]

lengths = list(map(len,my_strings))
print(lengths)
#[3,6,5,5]
```

Map can also take in more than one iterable.

```py
map(function, iterable1, iterable2)
```

```py
#!/usr/bin/python3

base = [1, 2, 3, 4]
power = [1, 2, 3, 4]

result = list(map(pow, base, power))
print(result) # [1, 4, 27, 256]
```
For each loop, map will go inside each iterable pick one element in each at the same time and pass them to the `pow` funnction

`pow(a, b)` -> a b times

`pow(2,2)` -> 2*2

`pow(3,4)` -> 3*3\*3\*3


3. <ins>**filter function**</ins>

The filter function as the it's name says, just filters out the elements inside the iterable that the function returns as `true`.

Filter like other functions takes in a function and an iterable. it also return a object class filter so it is up to the programmer to covert it back to something readable like a list or tuple.

```py
filter(function, iterable)
```

Example.

`without_filter.py`
```py
#!/usr/bin/python3

#return only odd number

def odd(num):
    if (num % 2) != 0:
        return True

my_nums = [12,13,14,16,18,19]
odd_only = []

def oddfunc(afunc, alist):
    for i in alist:
        if afunc(i):
            odd_only.append(i)

oddfunc(odd, my_nums)

print(odd_only)
#[13, 19]
```
`with_filter.py`

```py
#!/usr/bin/python3

#return only odd number

def odd(num):
    if (num % 2) != 0:
        return True

my_nums = [12,13,14,16,18,19]
result = list(filter(odd, my_nums))
print(result)
#[13, 19]
```

4. <ins>**reduce function**</ins>

reduce is not a built python function it has to be imported from `functools` library that comes with python. 

```py
from functools import reduce

```