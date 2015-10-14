#!/usr/bin/env python
#coding:utf-8

import sys,os,shutil,re,time


#处理程序的标志位
def flag():
	while True:
		Flag=raw_input(u'\t\t\t是否继续？(y/n):\n')
		if Flag=='y' or Flag=='n':
			return Flag
		else:
			print u'\t\t\t\033[31;5m输入错误，请重新输入\033[0m'

def notepad():
	try:
		print '\t'*18,u'\033[32;5m欢迎使用记事本的程序\033[0m\n'
		con=True
		while con:
			k=int(raw_input(u'请输入您的操作：\t\033[33;1m1.【我要写日记】\t2.【查看往事】\t3.【格式化笔记本】\t4.【备份文件】\t5.【恢复记事本】\t6.【搜索关键字】\t7【记事本分类】\t8【记事本文件列表】\t9.【退出】\033[0m\n'))
			if k==1:
				o=open(os.getcwd()+'notepad.log','a+')
				content=raw_input(u'请输入您需要记录的事情:\n')
				o.write(content)
				o.close()
				print u'========================================='

			elif k==2:
				print u'日记内容:\n'
				o=open(os.getcwd()+'notepad.log','a+')
				listcontent=o.readlines()
				for content in listcontent:
					print content
				o.close()
				print u'========================================'

			elif k==3:
				g=raw_input(u'您确定要格式化笔记本吗？格式化后数据将全部消失!!!\ny:确定\tn:取消:\n')
				if g=='y':
					print u'记事本正在进行格式化中...'
					if os.path.exists(os.getcwd()+'notepad.log'):
						os.remove(os.getcwd()+'notepad.log')
						print u'笔记本格式化成功!'
					else:
						print u'\t\t\t\033[1;31;41m记事本不存在\033[0m'
				else:
					print u'取消格式化笔记本'
					continue
			elif k==4:
				bf=raw_input(u'您确定要备份记事本吗？\ny:确定\tn:取消:\n')
				if bf=='y':
					print u'记事本正在备份中...'
					shutil.copyfile(os.getcwd()+'notepad.log','c:\\notepad.log')
					shutil.move(os.getcwd()+'notepad.log','c:\\notepad.log')
					print u'记事本备份成功!'
				else:
					continue

			elif k==5:
				hf=raw_input(u'您确定要恢复记事本吗?\ny:确定\tn:取消:\n')
				if hf=='y':
					print u'正在恢复记事本中...'
					shutil.copyfile('c:\\notepad.log',os.getcwd()+'notepad.log')
					print u'记事本恢复成功!'
				else:
					continue

			elif k==6:
				o=open(os.getcwd()+'notepad.log','a+')
				fileInfo=o.readlines()
				o.close()
				break_Flag=''
				while break_Flag!='n':
					while True:
						k=raw_input(u'您确定要进行关键字的搜索吗？(y/n):\n')
						if k=='y':
							searchInfo=raw_input(u'请输入您需要查询的信息:\n')
							if len(searchInfo)>2:
								break
							else:
								print u'您输入的字符不合法，请重新输入！'
						else:
							break
					count_number=0
					search_Info_List=[]
					for i in fileInfo:
						search_Info_List.append(i.replace(searchInfo,'\033[32;1m %s \033[0m'%searchInfo))
						count_number+=i.count(searchInfo)
						if count_number>0:
							print u'搜索到关键字:\033[31;1m%s\033[0m条信息！\n'%(count_number)
							for i in search_Info_List:
								print i
							break_Flag=flag()

			elif k==7:
				k=raw_input(u'您确定要对记事本进行分类吗？(y/n):\n')
				if k=='y':
					print u'正在进行记事本分类...'
					dirs=os.getcwd()+time.strftime('%Y-%m-%d',time.localtime())
					os.makedirs(dirs)
					files=dirs+'\\notepad.log'
					f=open(files,'a+')
					content=raw_input(u'请输入您需要记录的事情：\n')
					f.writelines(content)
					print u'记事本已分类完成！'
				else:
					continue

			elif k==8:
				def ListDir(path,fun,par):
					for filespath in par:
						print os.path.join(fun,filespath).strip(os.getcwd())
				k=raw_input(u'是否要查看日记分类信息？(y/n):\n')
				if k=='y':
					print u'记事本分类信息为：\n'
					os.path.walk(os.getcwd(),ListDir,())
				else:
					continue

			elif k==9:
				for i in range(3):
					print u'\033[34;5m感谢您使用记事本程序，%s秒后程序将会自动退出！\033[0m'%(3-i)
					time.sleep(1)
					con=False

			else:
				print u'\t\t\t\033[31;1m输入不合法，请重新输入，谢谢！\033[0m'
				continue
	except:
		print u'输入错误，请再次执行程序！'

if __name__=='__main__':
	notepad()
