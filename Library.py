import mysql.connector

conn = mysql.connector.connect(
   user='root', password='', host='127.0.0.1', database='ishita_database'
)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS employee")

sql ='''CREATE TABLE `employee`(
   USERNAME CHAR(20) NOT NULL,
   PASSWORD CHAR(20) ,
   STATUS CHAR(20),
   INITIAL_DATE DATETIME NOT NULL
)'''
sql1='''INSERT INTO `employee`(
   `USERNAME`,`PASSWORD`,`STATUS`,`INITIAL_DATE`)
   VALUES('ishi70','goyal30','book issued',NOW())'''
cursor.execute(sql)
cursor.execute(sql1)
cursor.execute("commit")
conn.close()