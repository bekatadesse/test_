#!/usr/bin/python3
import pymysql


con = pymysql.connect(
    user = "USERONE",
    password = "123",
    host = "localhost",
    database = "BEKAT"
)

cursor = con.cursor()
cursor.execute("SELECT * FROM `ONE`;")
table = cursor.fetchall()
print(table)
cursor.close()
