# Python data structures

`data structures are a way of organising data that will be passed to a computer to process.` They make the computer work efficiently but if `not well used` can be a programmer's worst dream

python as a high level programming langauge has data structures; strings, lists, tuples, dictionaries and sets

1. **strings**

A string is a sequence of characters between single or double qoutes.

```py
#!/usr/bin/python3
string1 = 'a single qouted string'
string2 = "a double quoted string"
```
- are immutable (once created can not be changed)
  ```py
    #!/usr/bin/python3
    name = 'Dut'
    name[0] = 'P'
    name[-1] = 'tin'

    #trying to change the strings by assigning new data at an index will cause an error 
    # TypeError: 'str' object does not support item assignment
    ```
- have a defined length
     ```py
    #!/usr/bin/python3
    name = "Dut Kulang"
    print(len(name))
    #10
    ```
- are indexed
    ```py
    #!/usr/bin/python3
    name = "Dut Kulang"
    print(name[1]) #u
    print(name[-1]) #g
    ```
- can contain any data type
    ```py
    #!/usr/bin/python3
    my_string = 'a 123 45.678 @ ! - * '
    print(my_string)
 
    ```

1. **lists**
list is a sequence of data types between sqaure brackets.
```py
#!/usr/bin/python3
my_list = [123, True, 456.78, 'am inside a list']
print(my_list)
#[123, True, 456.78, 'am inside a list']
```

2. **dictionary**

A dictionary is a collection data type that is unordered and mutable. It consists of a collection of key, value pair separated by a colon `:`.

`Each key is mapped to a value`

```py
#!/usr/bin/python3
my_dict = {
    'key': 'value'
}
print(my_dict['key'])
# value
```

```py
#!/usr/bin/python3
presidents = {
    'p1':'Dut Kulang',
    'p2': 'Salva Kiir',
    'p3': 'Robert Mugabe'
}
print(pr)
print(presidents[p1])

```

1. ## **set**

A set is a collection of `unordered`, `unique`, and `unindexed` elements.

A set is a collection of data of different data types.

Elements in a set can be of any data type but are `not indexed`.

Elements in a set can not be duplicate, can not be repeated inside the set, elements in a set are not `indexed`. Since sets are not indexed, operations like slicing is `NOT` possible.


<ins>When to use sets</ins>
- when order of data does not matter
- when data needs to be uniquea collection of data types.

<hr>

## Declearing a set.

`method1.py`

```py
#!/usr/python3
my_set = {12,'Dut', True, False, 345.67, 7/3}
#{False, True, 2.3333333333333335, 'Dut', 345.67, 12}
```

`method2.py`

```py
#!/usr/bin/python3

"""
using the set method
set(argument)
set takes in one argument ONLY usually another data structure

set will convert the provided data structure into a set. 
"""
my_set = {[12,'Dut', True, False, 345.67, 7/3]}
print(my_set)

#{12, 2.3333333333333335, 345.67, 'Dut', False, True}
```
`method3.py`

```py
#!/usr/bin/python3
empty = set()
print(empty)

#{}
```
<hr>

### <ins>Finding length  of a set

`Warning Since sets are not indexed, you can not perform slicing using indexes but you can loop through the elements in a set printing out each element`
<hr>

`length_of_set1.py`
```py
#!/usr/bin/python3
my_set = {[12, 'Dut', True, False, 345.67, 7/3]}
print(len(my_set)) #returns the number of elements inside a set
```

`length_of_set2.py`
```py
#!/usr/bin/python3

my_set = {12,'Dut', True, False, 345.67, 7/3}

for element in my_set:
    print(element)
```

<ins>**Adding Elements**

- `add(element)` :- Allows one element to be added to a set.
- `update(elements)` :- allows multiple elements to be added to a set.

<ins>**Removing elements from a set**

- `remove(element_to_removed)` :- Removes an element specified from a set but returns an error if the element does not exist.
- `discard(element)` :- Removes an element specified from a set but returns no error if the element does not exist.
- `pop()` :- Randomly removes an element from a set.

```py
#!/usr/bin/python3

my_set = {12,'Dut', True, False, 345.67, 7/3}
my_set.remove(12) # removes 12 from the set

my_set.remove(`elehant`) #returns an error cause `elephant` is not an element in the set
```

```py
#!/usr/bin/python3

my_set = {12,'Dut', True, False, 345.67, 7/3}
my_set.discard(True) # removes True from the set
my_set.discard("Hello") # returns no error though "Hello" does not exist
```

```py
#!/usr/bin/python3

my_set = {12,'Dut', True, False, 345.67, 7/3}
print(my_set.pop()) #randomly removes any element from a set and returns the deleted element
```

## **Union**
Union returns all the elements in sets without repeating duplicate elements.

`Using pipe (|) method`
```py
#!/usr/bin/python3

a = {1,2,3,4,5, 'Dutin'}
b = {"Dutin","ALX","Putin"}
c = {"cow", "Dutin", "rat", 1}
print(a|b|c) #union of set a, b, c
#{1, 2, 3, 4, 5, 'rat', 'Dutin', 'cow', 'Putin', 'ALX'}
```

`Using the union method`
```py
#!/usr/bin/python3

a = {1,2,3,4,5, 'Dutin'}
b = {"Dutin","ALX","Putin"}
c = {"cow", "Dutin", "rat", 1}
print(a.union(b,c)) #finds the union of set a, b, c
#{1, 2, 3, 4, 5, 'rat', 'Dutin', 'cow', 'Putin', 'ALX'}
```
