class galua:
	def __init__(self, string_value):
		self.factors = list(map(lambda x: int(x), string_value))
		
	def __add__(self, other):
		temp = self.factors[:]
		temp = [0] * (max(len(self.factors), len(other.factors)) + 1 - len(temp)) + temp
		print(temp)
		print(other.factors)
		for i in range(1, len(temp)):
			temp[-i] = (temp[-i] + other.factors[-i]) % 2
		return galua(temp[temp.index(1):])
		
	def __mul__(self, other):
		temp = [0] * (max(len(self.factors), len(other.factors)) * 2)
		for i in range(1, len(other.factors) + 1):
			if other.factors[-i] == 1:
				mul = [0] * (len(temp) - i + 1 - len(self.factors)) + self.factors + [0] * (i - 1)
				for j in range(1, len(temp)):
					temp[-j] = (temp[-j] + mul[-j]) % 2
		return galua(temp[temp.index(1):])
		
	def __mod__(self, other):
		temp = self.factors[:]
		length = len(other.factors) - other.factors.index(1)
		while (temp.count(1) > 0) and (len(temp) - temp.index(1) >= length):
			mod = other.factors + [0] * (len(temp) - temp.index(1) - length)
			for i in range(1, len(mod) + 1):
				temp[-i] = (temp[-i] + mod[-i]) % 2
		return galua(temp)
		
	def __str__(self):
		return self.info(self.factors)
		
	def __repr__(self):
		return __str__()
				
	def info(self, value):
		str = ''.join(map(lambda x: chr(x + 48), value))
		if str.count('1') > 0:
			return str[str.index('1'):]
		else:
			return str

	
def bs(s):
	return str(s) if s<=1 else bs(s>>1) + str(s&1)

def muls(pln, mod):
	module = galua(mod)
	const = galua(pln)
	for i in range(1, 256):
		gal = galua(bs(i))
		print('temp =', gal, (gal * const % module))
