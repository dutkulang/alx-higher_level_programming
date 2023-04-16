# Object Relational Mapping

This is a process of which object oriented code is translated to its SQL equivalent by the use of a special program known as an ORM -> **Object Relational Mapper**

### Connect MySQL database client to python

1. import the MySQL connector module and establish a connection

```py
import MySQLdb

db = MySQLdb.coonect(
host="host_name",
user="db_account_user_name",
passwd="db_usr_password",
db="db_name_that_you_wish_to_connect_to"
)
```