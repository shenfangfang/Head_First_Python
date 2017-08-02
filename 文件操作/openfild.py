import nester
A=[]
B=[]
try:
	data=open('sketch.txt','r', encoding='utf-8')
	print(data.readline())#读取一行
	data.seek(0) #归为到0，从第一行读取
	for i in data:
		try:
			(name,content)=i.split(":",1)
			content = content.strip()#当strip参数为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
			if name=='A':
				A.append(content) #在A列表中追加内容
			elif name=='B':
				B.append(content)
		except ValueError:
			pass
	data.close()
except IOError:
	print("the file missing")
print('A[]:',A) #打印A列表中的内容
print('B[]:',B)

#将列表中的数据写入到文件中
# try:
# 	A_file=open('A_file.txt','w',encoding='utf-8') #以w方式打开
# 	B_file=open('B_file.txt','w',encoding='utf-8')
# 	print(A,file=A_file) ##用print语句写入到A_file中
# 	print(B,file=B_file)
# except IOError:
# 	print('File error')
# finally:
# 	if A_file in locals():
# 		A_file.close()
# 	if B_file in locals():
# 		B_file.close()

# 将列表中的数据写入到文件中
#使用with实现,可以省略文件.close（）操作,
try:
	with open('A_file.txt', 'a', encoding='utf-8') as A_file:# 以w方式打开
		# print(A, file=A_file)  ##用print语句写入到A_file中
		nester.print_lol(A,fh=A_file)#调用nester模块的print_lol方法
	with open('B_file.txt', 'a', encoding='utf-8') as B_file:
		# print(B, file=B_file)
		nester.print_lol(B, fh=B_file)#调用nester模块的print_lol方法
except IOError:
	print('File error')

#使用print方法追加文本到文件中
A_file_read=open('A_file.txt','a',encoding='utf-8')
print('我猜着了开头，但我猜不中这结局',file=A_file_read)

