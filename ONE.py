
import pymysql


con = pymysql.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "BEKAT"
)

cursor = con.cursor()
cursor.execute("SELECT * FROM `ONE`;")
table = cursor.fetchall()
print(table)
cursor.close()
