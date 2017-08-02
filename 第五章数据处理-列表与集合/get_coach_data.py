'''
打开文件，并将文件中的数据以","分隔，分割开的数据项插入到列表中
参数：
打开的文件：filename
返回的列表：处理好的list

# 调用示例
# james=get_coach_data('james.txt')
# print(james)

未完待续
'''
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
			return (data.strip().split(','))
	except IOError as ioerr:
		print('file error:'+ioerr)
		return(None)