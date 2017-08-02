movies=['A',1975,'B',1991,['c',['d1','d2','d3','d4','d5']]]
import sys
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
	for i in the_list:
		if isinstance(i,list):
			print_lol(i,indent,level+1,fh)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t",end='',file=fh)
			print(i,file=fh)

nester_file=open('neste_file.txt','w')
print_lol(movies,fh=nester_file)


