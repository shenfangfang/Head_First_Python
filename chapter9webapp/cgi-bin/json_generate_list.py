import athletemodel
import yate  # 模板
import time
import glob  # 可以操作系统查询一个文件名列表
import json
import requests
# 启用python的cgi跟踪技术
import cgitb
cgitb.enable()

print(yate.start_response())
print(yate.include_header("List of Athletes"))
print(yate.start_form("json_back_timing_data.py"))
print(yate.para("Select an athlete from the list"))
url="http://127.0.0.1:8089/cgi-bin/json_back_names.py"
namesID=json.loads(requests.get(url,timeout=4).text)
# print(namesID[0])
try:
	time.sleep(1)  # 单线程，需要等namelist的结果返回后，才能进行下一个web请求,但是还不能解决，头大？？？
	for each_athlete in namesID:
		print(yate.radio_button_id('which_athlete', each_athlete[0],each_athlete[1]))
except Exception as err:
	print(err)
print(yate.end_form('Select'))
print(yate.include_footer({"Home": "/index.html"}))
