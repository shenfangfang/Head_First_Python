#####此页面不展露在前端页面,只是dumps数据,以便前端页面loads数据#########

import athletemodel
import yate  #模板

import json

import cgitb
cgitb.enable()

#接收表单数据,获取value值,从数据库中查出对应的top3数据,并使用json.dumps存储成json格式,
# form_data=cgi.FieldStorage()  #返回一个字典
# athlete_id=form_data['which_athlete'].value #返回字典对应的健的值； 参照yate，在这里的value值==id值
# athletes=athletemodel.get_athlete_from_id(athlete_id)
athletes=athletemodel.get_athlete_from_id('1') #不知原因，上一行在浏览器无法取得选手athlete_id，这里指定一个id参数=‘1’
#根据方法 get_athlete_from_id(athlete_id)返回一个字典
# {
    #     'Name':name,
    #     'Bob':bob,
    #     'data':data,
    #     'top3':data[0:3]
    # }
print(yate.start_response("application/json"))
print(json.dumps(athletes))





