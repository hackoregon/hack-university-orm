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

## Advantages and Disadvantages



### Group By

#### Django

```
In [13]: qs = Crimedataraw.objects.values('neighborhood').annotate(n_count=Count('neighborhood'))

In [14]: print(qs.query)
SELECT "crimedataraw"."Neighborhood", COUNT("crimedataraw"."Neighborhood") AS "n_count" FROM "crimedataraw" GROUP BY "crimedataraw"."Neighborhood"

In [15]: {d['neighborhood']: d['n_count'] for d in qs[:10]}
Out[15]:
{u'BRIDGETON': 73,
 u'CULLY': 1149,
 u'GRESHAM - NORTH CENTRAL': 3,
 u'GRESHAM - NORTH GRESHAM': 6,
 u'HOSFRD-ABRNETHY': 878,
 u'MILL PARK': 817,
 u'ROSE CITY PARK': 357,
 u'UNIVERSITY PARK': 339,
 u'W PORTLAND PARK': 141,
 u'WOODSTOCK': 600}

# And we can order that too
In [21]: {d['neighborhood']: d['n_count'] for d in qs.order_by('-n_count')[:10]}
Out[21]:
{u'CENTENNIAL': 2076,
 u'CHINA/OLD TOWN': 3243,
 u'DOWNTOWN': 5394,
 u'HAZELWOOD': 3727,
 u'LENTS': 2513,
 u'LLOYD': 1542,
 u'MONTAVILLA': 1374,
 u'NORTHWEST': 2047,
 u'PEARL': 1549,
 u'POWELHST-GILBRT': 2437}
```

## Introspection 
What if a data base already exists and it was not created nor managed using the ORM
you have at hand?

Most ORMs provide a way to integrate with an existing data base, whether to migrate to a new application code base, to normalize over several different data base syntaxes (MySQL, PostgreSQL, Oracle, MS SQL, etc.), or because a developer is more familiar with a particular ORM. Django provides the management command [`inspectdb`](https://docs.djangoproject.com/en/1.9/howto/legacy-databases/)  

```console
python manage.py inspectdb > models.py
```
