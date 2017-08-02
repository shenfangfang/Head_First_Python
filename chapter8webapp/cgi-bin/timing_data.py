import athletemodel
import yate  #模板
import glob #可以操作系统查询一个文件名列表
import json
import requests
import urllib
import urllib.request #在python 2.x中是urllib2，在python 3.x中是urllib.request，
url = "http://127.0.0.1:8089/cgi-bin/generate_data_json.py"
athlete=json.loads(requests.get(url).text)
#启用python的cgi跟踪技术
import cgitb
cgitb.enable()

print(yate.start_response())
print(yate.include_header('data from generate_data'))
print(yate.include_header("Athlete:"+athlete['name']+"|dob:"+athlete['bob']))
print(yate.para("The top3 times is:"))
print(yate.u_list(athlete['top3']))
print(yate.include_footer({"Home":"/index.html"}))





