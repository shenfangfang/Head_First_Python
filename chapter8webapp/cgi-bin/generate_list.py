import athletemodel
import yate  #模板
import glob #可以操作系统查询一个文件名列表

#启用python的cgi跟踪技术
import cgitb
cgitb.enable()

data_files=glob.glob('data/*.txt')
athletes=athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("List of Athletes"))
# print(yate.start_form("generate_timing_data.py"))

print(yate.start_form("generate_timing_data.py"))

print(yate.para("Select an athlete from the list"))
for each_athlete in athletes:
	print(yate.radio_button('which_athlete',athletes[each_athlete].name))
print(yate.end_form('Select'))

print(yate.include_footer({"Home":"/index.html"}))





