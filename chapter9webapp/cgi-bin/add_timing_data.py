import cgi
import sqlite3
import yate

print(yate.start_response('text/plain'))
form=cgi.FieldStorage()
the_id=form['1'].value
the_time=form['TimeValue'].value
connection=sqlite3.connect('coachdata.sqllite')
cursor=connection.cursor()
cursor.execute("INSERT INTO timing_data(athlete_id,value) VALUES (?,?)",(the_id,the_time))
connection.commit()
connection.close()
print(the_id,the_time)
print('OK')