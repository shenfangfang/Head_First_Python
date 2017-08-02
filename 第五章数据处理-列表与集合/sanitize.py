'''
sanitize():将时间字符串格式化为mins.secs
'''
def sanitize(time_string):
	if '-'in time_string:
		mins,secs=time_string.split('-')
	elif ':'in time_string:
		mins, secs = time_string.split(':')
	else:
		return time_string

	return(mins+'.'+secs)