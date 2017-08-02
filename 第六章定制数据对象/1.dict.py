
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

'''
打开文件，并将文件中的数据以","分隔，分割开的数据项插入到列表中；返回一个字典，字典中的值取自于列表的值
参数：
打开的文件：filename
返回：一个字典

# 调用示例
james_dic={}
james_dic_top3=get_coach_data('james2.txt',james_dic)
未完待续
'''
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
			# return (data.strip().split(','))
			data_list=data.strip().split(',')
			return({
				'Name':data_list.pop(0),
				'Birthday':data_list.pop(0),
				'Times':sorted(set([sanitize(t) for t in data_list]))[0:3]
			})

	except IOError as ioerr:
		print('file error:'+ioerr)
		return(None)

# james=get_coach_data('james2.txt')

#使用列表、集合处理
# (james_name,james_birthday)=james.pop(0),james.pop(0)
# print(james_name+'最快的前三个时间是'+str(sorted(set([sanitize(t) for t in james]))[0:3]))

#使用字典处理
# james2_data={}
# james2_data['Name']=james.pop(0)
# james2_data['Birthday']=james.pop(0)
# james2_data['Times']=james
# print(james2_data['Name']+'最快的前三个时间是'+str(sorted(set([sanitize(t) for t in james]))[0:3]))


james_dic_top3=get_coach_data('james2.txt')
print(james_dic_top3['Name']+'最快的前三个时间是'+str(james_dic_top3['Times']))