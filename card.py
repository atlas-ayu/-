cards=('武则天','李白','兰陵王','姜子牙','貂蝉','安琪拉')
package=[]
import random

while 1 :
	print('\n  充值让你变得更强！\n  请选择指令：\n  1.抽卡\n  2.查看背包\n  3.整理背包\n  4.离开')
	a=input()

	if a==1:
		b=input('输入抽卡次数:')
		if b<=0:
			print('请输入正确的次数')
			continue
		else:
			i=1
			for i in range(1,b):
				i=i+1
				c=random.choice(cards)
				package.append(c)
	print(package)
