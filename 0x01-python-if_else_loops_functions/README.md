# python conditions

computer don't understand human language what they understand is machine code, 1 and 0. 1 for true zero for false.

python has a variety of ways to check conditions these are called conidtional statements. python unlike other high level programming languages that use curl brackets to indicate the body of condition, python uses indentation.

The condition will check if the provided expression is true, then it's body block will be executed, if false the program will jump to the next conditional

```py
#!/usr/bin/python3

condition check 1 expression:
    body
    body
    body
condition check2 expression:
    body
    body
    body
```

`if, elif, else`

```py
#!/usr/bin/python3
if expression:
    then do this
else:
    do this
```

```py
#!/usr/bin/python3
age = 19
if age >= 18:
    prinnt("You are an adult")
else:
    print("You are a child")
```
```py
#!/usr/bin/python3
age = 9
if age <= 3:
    print('infant')

elif age <= 12:
    print('a child/kid')

elif age >= 13 <= 19:
    print("Teenager")


else:
    print("Adult")
```

`while`

```py
#!/usr/bin/python3
count = 0
count_to = 100

while count < count_to:
    print(count)
    count += 1
```

`for`

```py
#!/usr/bin/python3
names = ['Dut', 'Fred', 'Wlliam']

for name in names:
    print("Hello {}, how are you doing today")
```
