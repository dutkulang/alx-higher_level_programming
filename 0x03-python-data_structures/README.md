# Python data structures

`data structure are a way of organising data that will be passed to a computer to process.` They make the computer work efficiently but if `not well used` can be a programmer's worst dream

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
 
    ```

1. **lists**

2. **dictionary**

3. **set**