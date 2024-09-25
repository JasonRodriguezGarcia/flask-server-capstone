# use as following
# python initdb.py

import sqlite3
#opening connection to database which will be created
connection = sqlite3.connect('./databases/database.db')

#opening schema.sql
with open('./schemas/schemaresultados.sql') as f:

#Next you execute its contents using the executescript() method
#that executes multiple SQL statements at once, which will create the posts table
    connection.executescript(f.read())

connection.close()