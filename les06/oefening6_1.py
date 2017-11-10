def getResult(pythonCijfer, miniProject):
	result=0

	if pythonCijfer >= 5.5:
		if miniProject == "VD":
			result=1
	elif pythonCijfer>4.5:
		if miniProject =="VD":
			result=2
		else:
			result=3
	else:
		result=4

	return result
getResult(7,'VD')



