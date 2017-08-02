import athletemodel
import yate  #模板
import glob #可以操作系统查询一个文件名列表
import json

import urllib,urllib.request,urllib.parse
import urllib.request #在python 2.x中是urllib2，在python 3.x中是urllib.request，
url = "http://127.0.0.1:8089/cgi-bin/json_back_names.py"
#定义一个函数，使用urllib、urllib.request库的功能，向服务器的某url请求，返回该url的内容；

'''
函数名：send_to_server
参数：url：请求的url地址；
	  post_data:向请求的地址发送的数据
返回值：返回请求的结果数据，并进行解码
使用示例：将请求结果使用json反序列化，并排序，排序结果是一个list类型；
namelist=sorted(json.loads(send_to_server(url)))
print(type(namelist))
for i in namelist:
	print(i)
'''
def send_to_server(url,post_data=None):
	request = urllib.request.Request(url)
	if post_data:
		response=urllib.request.urlopen(url,urllib.parse.urlencode(post_data))
	else:
		response = urllib.request.urlopen(request,None,10)
	return (response.read().decode('utf-8'))
namelist=sorted(json.loads(send_to_server(url)))
namelist0=namelist[0]
# request=urllib.request.Request(url)
# response=urllib.request.urlopen(request)
# response_read=response.read().decode('utf-8')
# print(type(response_read)) #返回的是json字符串<class 'str'>

#启用python的cgi跟踪技术
import cgitb
cgitb.enable()

print(yate.start_response())
print(yate.include_header("List of Athletes"))
# print(yate.start_form("json_generate_timing_data.py"))
print(yate.para("Select an athlete from the list"))
# print(yate.radio_button('which_athlete',sorted(json.loads(send_to_server(url)))))
# print(yate.para('namelist0'))
# for each_athlete in sorted(json.loads(send_to_server(url))):
# 	print(yate.radio_button('which_athlete',each_athlete))
# for each_athlete in ['James Lee','Julie Jones','Mikey McManus','Sally Sanchez','Sarah Sweeney','Vera Vi']:
# 	print(yate.radio_button('which_athlete',each_athlete))
print(yate.end_form('Select'))
print(yate.include_footer({"Home":"/index.html"}))





