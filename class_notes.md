# Object-Relational Mapping (ORM)

## Overview

ORMs provide idiomatic access to data in data bases. In Python, this means data base rows are translated into Python objects and relations are represented commonly as attributes or methods. Queries can be represented as Python objects, and querying the database is often lazily evaluated, allowing the programmer to create queries as and pass them through the program to be updated and evaluated only when needed.

## Motivation 

#### the old way
```python
import MySQLdb
import config

connection = MySQLdb.connect(
    host=config.HOST,
    user=config.USER,
    passwd=config.PASS,
    db='test'
)
cursor = connection.cursor()
sql = """SELECT foo id FROM foo WHERE bar IN ('A', 'C')"""
cursor.execute(sql, args)
data = cursor.fetchall()
print(data)
```

#### with an ORM
```python
data = Foo.objects.filter(bar__in=['A', 'C'])
print(data)
```

Connecting to the database via the shell may feel very natural when needing to run a report, adjust some data, or batch process a new set of data, but using raw SQL statements within a program has its limitations and security concerns, and wouldn't it be far easier to use python to interact with the database from a python program?
