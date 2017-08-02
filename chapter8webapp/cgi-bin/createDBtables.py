#创建coachdata.sqlite数据库

import sqlite3

connection=sqlite3.connect('coachdata.sqllite')
cursor=connection.cursor()

cursor.execute("""CREATE TABLE athletes(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
name TEXT NOT NULL,
dob DATE NOT NULL)""")
cursor.execute("""CREATE TABLE timing_data(
athlete_id INTERGER NOT NULL,
value TEXT NOT NULL,
FOREIGN KEY (athlete_id)REFERENCES athletes)""")
connection.commit()
connection.close()