regel=0
while regel<3:
	print('regel '+str(regel), end=': ')
	for index in range(0, 3):
		if regel==1:
			break
			print('$', end=", ")
		elif index==0:
			pass
			print('@', end=", ")
		elif index==1:
			continue
			print("#", end=', ')
		print(str(index), end=', ')
	regel+=1
	print(end='\n')
