a = 1
if float(a) == int(a):
	a = str(a) + '.' + '00'
else:	
	a = float('{:.3f}'.format(a))

print(a)