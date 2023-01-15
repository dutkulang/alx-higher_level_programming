# lambda, map, filter and reduce functions

1. <**ins**>**lambda**</ins>

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

2. <ins>**map**</ins>
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