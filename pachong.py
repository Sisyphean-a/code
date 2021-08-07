import random

def suiji():
	num0=40
	num1=random.randint(0,num0)
	num2=num0-num1
	a=random.randint(0,num1)
	b=num1-a
	c=random.randint(0,num2)
	d=num2-c
	jieguo=a+b+c+d

	return jieguo

def wending():
	a=random.randint(0,10)
	b=random.randint(0,10)
	c=random.randint(0,10)
	d=random.randint(0,10)
	jieguo=a+b+c+d

	return jieguo

i=1000
sj=0
wd=0

while i!=0:
	i=i-1
	s=suiji()
	w=wending()
	if s>w:
		sj=sj+1
	elif s<w:
		wd=wd+1
	
		

end=sj/1000

print(end)




