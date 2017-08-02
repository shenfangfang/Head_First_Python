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
print(yate.start_form("json_generate_timing_data.py"))
print(yate.para("Select an athlete from the list"))
url="http://192.168.1.61:8089/cgi-bin/json_back_names.py"
namelist=json.loads(requests.get(url,timeout=4).text)
try:
	time.sleep(1)  # 单线程，需要等namelist的结果返回后，才能进行下一个web请求,但是还不能解决，头大？？？
	for each_athlete in namelist:
		print(yate.radio_button('which_athlete', each_athlete))
except Exception as err:
	print(err)
print(yate.end_form('Select'))
print(yate.include_footer({"Home": "/index.html"}))
