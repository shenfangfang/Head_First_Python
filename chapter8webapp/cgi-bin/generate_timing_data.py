import athletemodel
import yate  #模板
import glob
import cgi
#启用python的cgi跟踪技术
import cgitb
cgitb.enable()


#从模型得到数据
athletes=athletemodel.get_from_store()

#获取表单提交的数据
form_data=cgi.FieldStorage() #获取所有表单数据，并放在一个字典中
athlete_name=form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header('------------------'))
print(yate.include_header("Athlete:"+athlete_name+"|dob:"+athletes[athlete_name].dob))

print(yate.para("The top3 times is:"))
print(yate.u_list(athletes[athlete_name].top3))

print(yate.include_footer({"Home":"/index.html"}))
print(yate.include_footer({"Other athletes":"/cgi-bin/generate_list.py"}))