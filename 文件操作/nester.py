import sys
'''
概述：处理一个列表[]，将列表中的数据输出，可以规定是否缩进、缩进深度、输出到哪里
参数说明
	the_list:列表名称
	indent：遇到列表嵌套列表情况是否缩进
	level：初始缩进深度
	fh：输出到哪里，可以是文件或屏幕上
'''
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
	for i in the_list:
		if isinstance(i,list):
			print_lol(i,indent,level+1,fh)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t",end='',file=fh)
			print(i,file=fh)
# 测试
movies=['A',1975,'B',1991,['c',['d1','d2','d3','d4','d5']]]
nester_file=open('neste_file.txt','w')
print_lol(movies,fh=nester_file)


