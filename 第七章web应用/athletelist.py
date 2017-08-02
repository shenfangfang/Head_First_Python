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
打开文件，并将文件中的数据以","分隔，分割开的数据项插入到列表中；
参数：
打开的文件：filename
返回：类对象

# 调用示例
james=get_coach_data('james2.txt')
未完待续
'''
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
			# return (data.strip().split(','))
			data_list=data.strip().split(',')
			# return({
			# 	'Name':data_list.pop(0),
			# 	'Birthday':data_list.pop(0),
			# 	'Times':sorted(set([sanitize(t) for t in data_list]))[0:3]
			# })
			return (AthleteList(data_list.pop(0),data_list.pop(0),data_list))

	except IOError as ioerr:
		print('file error:'+ioerr)
		return(None)




#增加一个类,继承list后，add_time、add_times方法都不用实现了，list中自带append、extend方法
class AthleteList(list):
	def __init__(self,a_name,a_birthday=None,a_times=[]):
		list.__init__([])
		self.name=a_name
		self.birthday=a_birthday
		# self.times=a_times
	#增加一个方法，返回对象的self.times中最小的三个值
	def top3(self):
		return sorted(set([sanitize(t) for t in self]))[0:3]
	# #方法：添加1个时间值
	# def add_time(self,time_value):
	# 	return self.times.append(time_value)
	# #方法：添加多个时间值（使用列表的方式）
	# def add_times(self,time_list):
	# 	return self.times.extend(time_list)

#创建实例
# james=get_coach_data('james2.txt')
#方法调用
# james.append('1.99')
# james.extend(['1.90','1-33'])
# print(james.name+'最快的前三个时间是'+str(james.top3()))



