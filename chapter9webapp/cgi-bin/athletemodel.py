# 功能说明：从数据库中取出需要的数据

# cursor.fetchone()：将只取最上面的第一条结果，返回单个元组如('id','title')，然后多次使用cursor.fetchone()，依次取得下一条结果，直到为空。
# cursor.fetchall() :将返回所有结果，返回二维元组，如(('id','title'),('id','title')),

import sqlite3
db_name='coachdata.sqllite'
def get_names_from_store():
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    results=cursor.execute("""SELECT name FROM athletes""")
    response=[row[0] for row in results.fetchall()] #产生所有name的一个列表；    results.fecthall()返回((name1),(name2)....)
    connection.close()
    return (response)
def get_namesID_from_store():
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    results=cursor.execute("""SELECT name,id FROM athletes""")
    response=results.fetchall() #results.fecthall()返回((name1,id1),(name2,id2)....)
    connection.close()
    return (response)

def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name,dob FROM athletes WHERE id=?""",(athlete_id,))
    (name,bob)=results.fetchone()
    results=cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""",(athlete_id))
    data=[row[0] for row in results.fetchall()] #results.fetchall() 返回((value1),(value2)...)
    response ={
        'Name':name,
        'Bob':bob,
        'data':data,
        'top3':data[0:3]
    }
    connection.close()
    return (response)

#测试数据库返回
names=get_names_from_store()
print(names)

names_id=get_athlete_from_id("1")
print(names_id['Name'])
print(names_id['data'])
print(names_id['top3'])