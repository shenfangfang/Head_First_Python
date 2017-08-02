import yate,cgi
import athletemodel
form=cgi.FieldStorage()
the_id=form['which_athlete'].value
# the_athletes_name=athletemodel.
print(yate.start_response())
print(yate.include_header("Add a timing data"))
print(yate.do_form('add_timing_data.py',the_inputs=[[the_id],['TimeValue']],method='post',text='Send'))