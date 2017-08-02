import cgi
import json
import athletemodel
import yate
import requests
# import cgitb
# cgitb.enable()

url="http://127.0.0.1:8089/cgi-bin/json_back_timing_data.py"
athletes=json.loads(requests.get(url,timeout=4).text)

print(yate.start_response("application"))
print(yate.include_header("---'NUAC's Timing Data---------------"))
print(yate.include_header("Athlete:"+athletes['Name']+"|dob:"+athletes['Bob']))

print(yate.para("The top3 times is:"))
print(yate.u_list(athletes['top3']))

print(yate.include_footer({"Home":"/index.html"}))
print(yate.include_footer({"Other athletes":"/cgi-bin/json_generate_list.py"}))