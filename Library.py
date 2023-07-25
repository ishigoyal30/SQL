import mysql.connector

conn = mysql.connector.connect(
   user='root', password='', host='127.0.0.1', database='ishita_database'
)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql ='''CREATE TABLE EMPLOYEE(
   USERNAME CHAR(20) NOT NULL,
   PASSWORD CHAR(20) ,
   STATUS CHAR(20),
   INTIAL_DATE DATETIME
)'''
cursor.execute(sql)

conn.close()
