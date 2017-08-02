import pickle
from athletelist import  AthleteList
from athletelist import get_coach_data

def put_to_store(files_list):
	all_athletes={}
	for each_file in files_list:
		ath=get_coach_data(each_file) #将各个文件转换为AthleteList对象实例
		all_athletes[ath.name]=ath #把对象实例存储到字典中,对象实例的键名与实例的name属性相同；对象实例是值
		# print(all_athletes[ath.name].name)
	try:
		with open('athletes.pickle','wb')as athf:  #'wb' 二进制写方式
			pickle.dump(all_athletes,athf)
	except IOError as ioerr:
		print('File error(put_to_store):'+str(ioerr))
	return(all_athletes)

def get_from_store():
	all_athletes={}
	try:
		with open('athletes.pickle','rb')as athf: #二进制读方式
			pickle.load(athf)
	except IOError as ioerr:
		print('File error(put_to_store):'+str(ioerr))
	return(all_athletes)

#查看当前命名空间下所有可用的方法，确认导入成功
# print(dir())

the_files=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
#条用put_to_store()函数 将文件列表中的数据转换为一个字典，存储在一个pickle文件中
data=put_to_store(the_files)
#遍历字典查看选手的名字和出生日期
for each_athlete in data:
	print(data[each_athlete].name+' '+data[each_athlete].birthday)


#通过get_from_store()函数将pickle中的腌制数据加载到一个字典中，遍历查看各个选手的名字、出生日期
data2=get_from_store()
for each_athlete in data:
	print(data[each_athlete].name+' '+data[each_athlete].birthday)
