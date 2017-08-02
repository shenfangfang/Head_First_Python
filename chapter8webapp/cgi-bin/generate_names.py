import json
import athletemodel
import yate

import cgitb
cgitb.enable()

#get_names_from_store()返回一个names列表
names=athletemodel.get_names_from_store()

#在浏览器中请求本页面时，将使用json格式进行响应
print(yate.start_response('application/json'))
# 使用json的dumps方法，将names列表进行排序后，转换为JSON列表，发送到浏览器中（STDOUT）
print(json.dumps(sorted(names)))

#获取json列表中的第一个数据，发送到浏览器中
# print(json.dumps(sorted(names)[0]))



