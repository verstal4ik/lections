def f1(n:int):
	"""
	Рассчет факториала, на входе целые числа больше 0
	Если меньше нуля, вернет ошибку.
	"""
	assert n >= 0, "Факториал отр не определен"

	if n == 0:
		return 1

	return f1(n-1)*n

def gcd(a:int,b:int):
	"""Алгоритм Евклида
	На входе 2 целых числа a и b
	Если a равно b возвращаем a
	Если a > b, отправляем на следующий круг a-b, b 
	Иначе b < a, отправляем на следующий круг b, b-a 
	"""
	if a == b:
		return a
	elif a > b:
		return gcd(a-b, b)
	else: # a < b
		return gcd(a, b-a)

def power(a, n):
	"""Функция возведения в степень получаем на входе:
	a - число 
	n - степень 
	возвращаем a * a с понижением показателя степени на 1
	"""
	if n == 1:
		return a
	else:
		return power(a, n-1)*a

def even_power(a:float, n:int):
	"""Ускорим расчет степени относительно стандартного способа шаг n=1
	Если показатель степень нечетный, то выполним умножнение 2ух чисел
	Иначе, т.е. показатель четный, шагами с n/2 возводим встепень
	"""
	if n == 0:
		return 1
	elif n % 2 == 1:
		return even_power(a, n-1)*a
	else:
		return even_power(a*a, n//2)


if __name__ == '__main__':
	print (f1(n=4))
	print (gcd(10, 40))
	print (power(2,9))
	print (even_power(2,9)) 
