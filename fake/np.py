class ndarray(list):
	its = [list, tuple]
	def array(lst, shape):
		for i in range(len(shape)-1, -1, -1):
			lst = [lst for c in range(shape[i])]
		return ndarray(lst)
	def istrailend(big, smol):
		for i in range(len(big)):
			if big[i:]==smol:
				return i
		return False
	def getshape(self):
	self.shape = []
	i = self
	while 1:
		if not type(i) in its:
		break
		else:
		self.shape.append(len(i))
	return self.shape
	def __add__(augend, addend):
		if type(addend) not in (int, float) and ndarray.istrailend(ndarray.getshape(augend), ndarray.getshape(addend)==False:
			raise Exception("Invalid addition")
			return 1
		Sum = augend.copy()
		for i in range(len(Sum)):
			try: # if their shapes are the same
				if augend.shape == addend.shape:
					raise Exception("rong: shapes are not the same")
				# shapes are the same
				naddend = addend[i]
			except: # shapes are different / addend is an int
				naddend = addend
			Sum[i] = augend[i] + naddend
ndarray.its.append(ndarray)
