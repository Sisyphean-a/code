#continue break
#continue的意思是此次循环从此处截止，直接开始下一次循环。break的意思是循环结束

i=1
summ=0

while i<=20:
	print('新的一年')

	if i==10:
		print('今年让你休息一年')
		i=i+1
		continue 

	j=0
	while j<=12:
		summ=summ+0.1
		print('第',i,'年，第',j,'月，应支付1000元，累计支付',round(summ,2),'万')  
		j+=1
	i+=1 
print('终于，结束了o(╥﹏╥)o')


'''i=1
summ=0

while i<=20:
	print('新的一年')

	if i==10:
		print('你负债还完了了')
		i=i+1
		break

	j=0
	while j<=12:
		summ=summ+0.1
		print('第',i,'年，第',j,'月，应支付1000元，累计支付',round(summ,2),'万')  
		j+=1
	i+=1 
print('终于，结束了o(╥﹏╥)o')