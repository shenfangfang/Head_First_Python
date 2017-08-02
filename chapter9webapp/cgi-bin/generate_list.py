import athletemodel
import yate  #模板

#启用python的cgi跟踪技术
import cgitb
cgitb.enable()

athletes=athletemodel.get_namesID_from_store() #返回一个列表，包含id、name

print(yate.start_response())
print(yate.include_header("'NUAC' List of Athletes"))

print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list"))
for each_athlete in athletes:
	# 模板函数： def radio_button_id(rb_name, rb_value, rb_id):
	# <input  type="radio" name=rb_name  value= tr(rb_id)> rb_value
	#页面结果<input name='whick_athlete' value="1" type='radio'>James Lee
	#value的值对应数据库中某选手的id值
	print(yate.radio_button_id('which_athlete',each_athlete[0],each_athlete[1]))
print(yate.end_form('Select'))

#新增一个表单，用于给选手增加时间值
print(yate.start_form("test_form.py"))
print(yate.para("Select an athlete from the list,and add a timing data"))
for each_athlete in athletes:
	# 模板函数： def radio_button_id(rb_name, rb_value, rb_id):
	# <input  type="radio" name=rb_name  value= tr(rb_id)> rb_value
	#页面结果<input name='whick_athlete' value="1" type='radio'>James Lee
	#value的值对应数据库中某选手的id值
	print(yate.radio_button_id('which_athlete',each_athlete[0],each_athlete[1]))
print(yate.end_form('Select'))

print(yate.include_footer({"Home":"/index.html"}))





