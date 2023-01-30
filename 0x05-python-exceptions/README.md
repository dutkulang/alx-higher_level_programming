# Exception handling in python (handling errors)

As we engineers write computer software, it is common that they contain bugs `errors`. Most times these bugs break our programs, hindering the results, or functionality of our programs, in that case, we must handle these errors in a way that will not hinder or halt the execution process of our code.

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
