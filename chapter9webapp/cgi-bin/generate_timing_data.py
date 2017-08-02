import athletemodel
import yate  #模板
import cgi
#启用python的cgi跟踪技术
import cgitb
cgitb.enable()

#获取表单提交的数据
form_data=cgi.FieldStorage() #获取所有表单数据;cgi.FieldStorage()返回一个字典，字典的每一个key就是变量名，key对应的值就是变量名的值
# athlete_name=form_data['which_athlete'].value
athlete_id=form_data['which_athlete'].value
#从模型得到数据
athletes=athletemodel.get_athlete_from_id(athlete_id)

print(yate.start_response())
print(yate.include_header("---'NUAC's Timing Data---------------"))
print(yate.include_header("Athlete:"+athletes['Name']+"|dob:"+athletes['Bob']))

print(yate.para("The top3 times is:"))
print(yate.u_list(athletes['top3']))

print(yate.include_footer({"Home":"/index.html"}))
print(yate.include_footer({"Other athletes":"/cgi-bin/generate_list.py"}))