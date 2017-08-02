#功能说明：
#原始数据经过加工存入pickle
#从pickle中取出需要的数据

import pickle

from athletelist import AthleteList
#将.txt原始文件中的的数据加工，返回一个AthleteList对象，对象的参数（a_name, a_dob=None, a_times=[]）
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error (get_coach_data): ' + str(ioerr))
        return(None)

#将 经过加工的数据（AthleteList对象）存储为字典，字典中的key的值=AthleteList对象.'name'
#{
 #   'name1':[AthleteList对象1]
#    'name2':[AthleteList对象2]
# }
def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return(all_athletes)

#将 经过加工的数据（AthleteList对象）取出，同样的取出的是一个字典
def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return(all_athletes)

#调用时，返回选手名列表
#使用列表生成式：字典[字典的key].name for 字典的key in 字典
# 字典的key值==单个类示例
def get_names_from_store():
    athletes=get_from_store()
    response=[athletes[each_ath].name for each_ath in athletes]
    return (response)

