'''
类继承了list后，可以直接储存成绩数据，调用时直接调用对象名，就可以查询数据
例如：James=AthleteList('James','2017-3-1',['5.31','3,33'])
     print(James)   #['5.31','3,33']
'''
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times) #extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。

#规范计时数据，分秒使用.分隔
    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)

    @property
    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])

    @property
    def clean_data(self):
        return(sorted(set([self.sanitize(t) for t in self])))

    @property
    def as_dict(self):
        return ({
            'name':self.name,
            'bob':self.dob,
            'top3':self.top3
        })
