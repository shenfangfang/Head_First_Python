import sqlite3
connection=sqlite3.connect('coachdata.sqllite')
cursor=connection.cursor()

import glob
import athletemodel_old
data_file=glob.glob("../data/*.txt")
athletes=athletemodel_old.put_to_store(data_file)
#可替换为下面注释中的内容，put_to_store是存储的时候返回的字典；下面的get_from_store返回已存储的字典
# athletes=athletemodel_old.get_from_store()
for each_ath in athletes:
	name=athletes[each_ath].name
	dob=athletes[each_ath].dob
	cursor.execute("INSERT INTO athletes(name,dob) VALUES (?,?)",(name,dob))
	connection.commit()

	cursor.execute("SELECT id from athletes WHERE name=?AND dob=?",(name,dob))
	the_current_id=cursor.fetchone()[0]
	for each_time in athletes[each_ath].clean_data:
		cursor.execute("INSERT INTO timing_data(athlete_id,value)VALUES (?,?)",(the_current_id,each_time))
connection.commit()
connection.close()