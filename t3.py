def gcd(a:int, b:int):
	"""Рекурсия. Алгоритм Евклида. Поиск НОД
	
	"""
	if a == b:
		return b
	elif a > b:
		return gcd(a-b, b)
	else:
		return gcd(a, b-a)

def power(a, n):
	"""Рекурсия. Возведение в степень.


	"""
	if n == 1:
		return a
	return power(a, n-1)*x

if __name__ == '__main__':
	x = gcd(8, 70)
	a = power(2, 5)
	print (x, a)