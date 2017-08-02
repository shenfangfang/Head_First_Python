import nester
import pickle
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
				A.append(content)
			elif name=='B':
				B.append(content)
		except ValueError:
			pass
	data.close()
except IOError:
	print("the file missing")
print('A[]:',A)
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
	with open('A_file.txt', 'wb') as A_file:# 以wb（可写二进制方式）方式打开,
		# print(A, file=A_file)  ##用print语句写入到A_file中
		# nester.print_lol(A,fh=A_file)#调用nester模块的print_lol方法
		pickle.dump(A,A_file)
	with open('B_file.txt', 'wb') as B_file:# 以wb（可写二进制方式）方式打开
		# print(B, file=B_file)
		# nester.print_lol(B, fh=B_file)#调用nester模块的print_lol方法
		pickle.dump(B, B_file)
except IOError:
	print('File error')
except pickle.PickleError as perr:
	print('Pickling error:'+str(perr))

#新增一个列表，使用pickle进行存储、读取
new_A=[]
try:
	with open('A_file.txt','rb')as A_file: #rb,以二进制读方式打开
		new_A=pickle.load(A_file)
except IOError as err:
	print('File error:'+str(err))
except pickle.PickleError as perr:
	print('Pickling error:'+str(perr))

#打印第一行和最后一行
print(new_A[0])
print(new_A[-1])

#条用print_lol方法，打印所有行
nester.print_lol(new_A)



