# Exception handling in python (handling errors)

As we engineers write computer software, it is common that they contain bugs `errors`. Most times these bugs break our programs, hindering the results, or functionality of our programs, in that case, we must handle these errors in a way that will not hinder or halt the execution process of our code.

Whenever an error occurs in our programs, python usually does not know what to do, causing our program execution to crash, terminating it completely. But if there is an exception, the program will continue running i.e the error or bug will be taken care of and our program's execution will not be crashed.

If exceptions are not handled, the program will halt and show a traceback, which includes a report of the exception that was raised.

<hr>
<br>

python has mechanisms to handle exception, that is using the `try except` functions

```py
#!/usr/bin/python3

try:
    # try block
except ErrorName:
    # how to handle the error usually a message
```
--> try block contains the code that we suspect will cause an error or could raise an exception.

`It is where an error is likely to occur`

--> except block contains the code that will run incase the error / exception is raised.

`It is where error handling is performed incase it occurs.`

```py
#!/usr/bin/python3

try:
    """try this code block but if an error of ErrorName occurs"""
except ErrorName:
    """ then this block will handle it"""
```

### Examples

If you know all the error name that might occur then you can choose to handle them one by one

`method1.py`
```py
#!/usr/bin/python3

try:
    # trying code
except ErrorName1:
    # code to handle ErrorCode1
except ErrorName2:
    # code to handle ErrorCode2
except ErrorName3:
    # code to handle ErrorCode3
except ErrorName4:
    # code to handle ErrorCode4
....
else:
    #else body
```