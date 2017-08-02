#####此页面不展露在前端页面,只是dumps数据,以便前端页面loads数据#########
import json
import athletemodel
import yate

import cgitb
cgitb.enable()

#get_namesID_from_store()返回一个元祖((name1,id1),(name2,id2)....)
namesID=athletemodel.get_namesID_from_store()
#在浏览器中请求本页面时，将使用json格式进行响应
print(yate.start_response('application/json'))
# 使用json的dumps方法，将names列表进行排序后，转换为JSON列表，发送到浏览器中（STDOUT）
print(json.dumps(namesID))
#获取json列表中的第一个数据，发送到浏览器中
# print(json.dumps(namesID[0]))



