def merge(A:list, B:list):
	"""Алгоритм слияния
	Создаем в памяти пустое место под массив С
	i индекс прохода A
	k индекс прохода B
	n индекс прохода C


	"""
	C = [0] * (len(A) + len(B)) #Резервируем место под элементы
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1

	return C

def merge_soft(A):
	#проверяем крайний случай
	#подстроимcя под интерфейс ф-ции middle
	if len(A) <= 1:
		return
	middle = len(A) // 2
	L = [A[i] for i in range(0, middle)]
	R = [A[i] for i in range(middle, len(A))]
	merge_soft(L)
	merge_soft(R)
	C = merge(L,R)
	#Тут ниже интересное действо
	for i in range(len(A)):
		A[i] = C[i]
	return C

def hoar_sort(A):
	#крайний случай
	if len(A) <= 1:
		return None
	barrier = A[0]
	L = []
	R = []
	M = [] 
	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
	hoar_sort(L)
	hoar_sort(R)
	k = 0
	for x in L + M + R:
		A[k] = x
		k += 1

def check_sorted(A, ascending=True):
	"""
	Проверка отсортированности за O(len(A))
	int(True) = 1
	int(Fasle) = 0
	s = 2*x- 1
 	"""
	flag = True
	s = 2 * int(ascending) - 1 #Флаг что массив отсортирован по возрастанию

	for i in range(0, N-1):
		if s*A[i] > s*A[i+1]:
			flag = False
			break
	return flag

def bin_mass():
	pass


if __name__ == '__main__':
	B = [2,5,7,3,1]
	merge_soft(B)
	print(*B)