james=[]
julie=[]
mikey=[]
sarah=[]


'''
sanitize():将时间字符串格式化为mins.secs
'''
def sanitize(time_string):
	#处理使用'-'、 '：'分割开来的数据项；
	# split（）返回分割后的字符串列表；  x,y=[1,2]《===等同于将列表中的项赋值给等号前面的变量====》x=1;y=2
	if '-'in time_string:
		mins,secs=time_string.split('-')
	elif ':'in time_string:
		mins, secs = time_string.split(':')
	else:
		return time_string

	return(mins+'.'+secs)


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

# with open('james.txt') as james_data:
# 	data=james_data.readline()
# 	james=data.strip().split(',') #split()通过指定分隔符对字符串进行切片,返回分割后的字符串列表。

#创建新列表；迭代处理源列表中的字符串；将处理后的字符串追加到新列表;对新列表进行排序
#方法1
# clean_james = []
# for time_string in james:
# 	time_string=sanitize(time_string)
# 	clean_james.append(time_string)
# clean_james = sorted(clean_james)



#一行代码解决#【创建新列表；迭代处理源列表中的字符串；将处理后的字符串追加到新列表】
#方法2
#据说这种方发叫做：列表推导  list comprehension
#设计列表推导是为了减少将一个列表转换为另一个列表所需编写的代码

james=get_coach_data('james.txt') #调用函数，获得转换后的列表
clean_james=[sanitize(time_string) for time_string in james]
clean_james=sorted(clean_james)
print(clean_james)


##对排序后的列表 clean_james 去重，并且拿到时间最短的三个数据
unique_james=[]
#方法一：
# for clean_time in clean_james:
# 	if clean_time not in unique_james:
# 		unique_james.append(clean_time)
# print(unique_james[0:3])

#方法二：
#使用set()去重非常之简洁，因为set（）本身就不允许有重复项
unique_james=set(clean_james[0:3])
print(unique_james)
