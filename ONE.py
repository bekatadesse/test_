#!/usr/bin/python3

import MySQLdb
"""
using python to use database
----USER
----PASWORD
"""

con = MySQLdb.connect(
    user = "USERONE",
    password = "12345",
    host = "localhost",
    database = "BEKAT"
)

cursor = con.cursor()
cursor.execute("INSERT INTO ONE (ID, NAME) VALUES(4,'MEGENASA');")
cursor.execute("SELECT * FROM `ONE`;")
table = cursor.fetchall()
print(table)
cursor.close()
