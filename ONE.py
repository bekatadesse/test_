#!/usr/bin/python3
import pymysql

"""
using python to use database
----USER
----PASWORD
"""

con = pymysql.connect(
    user = "USERONE",
    password = "12345",
    host = "localhost",
    database = "BEKAT"
)

cursor = con.cursor()
cursor.execute("SELECT * FROM `ONE`;")
table = cursor.fetchall()
print(table)
cursor.close()
