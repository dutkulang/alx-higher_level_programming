# lambda, map, filter and reduce functions

<ins>lambda</ins>

lambda is a function that does not have a name.

lambda return returns memory to address object class lambda

## Declaration

```py
lambda argument(s) : expression
```

**Examples**

`lambda1.py`

```p
#Using lambda to find the square of a number

x = lambda x : x*x
print(x(5)) #25
```

`lambda2.py`

```py
#Using lambda to cube a number
x = lambda n : n*n*n
print(x(3)) #27
```
`lambda3.py`

```py
#Using lambda to find number is even or odd
#prints True if number is even else false

x = lambda x : x if True % 2 == 0 else False
print(x(5))
```



