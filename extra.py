def file_exists(path):
	try:
		with open(path,"r") as x:
			x.read()
			return True
	except FileNotFoundError:
		return False
	except:
		return True