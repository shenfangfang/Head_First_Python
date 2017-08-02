import cgi
import json
import athletemodel
import yate

# import cgitb
# cgitb.enable()

athletes=athletemodel.get_from_store()

 #获取表单数据,
# form_data=cgi.FieldStorage()  #返回一个字典
# athlete_name=form_data['which_athlete'].value #返回字典对应的健的值

print(yate.start_response("application/json"))
print(json.dumps(athletes["James Lee"].as_dict)) #直接使用某个选手的名字