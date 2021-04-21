def gen_number(n:int, m:int, prefix=None):
	if m == 0:
		print (prefix)
		return
	prefix = prefix or []
	for digit in range(n):
		prefix.append(digit)
		gen_number(n, m-1, prefix)
		prefix.pop()
	return

def simple_gen(m, prefix=""):
	if m == 0:
		print (prefix)
	else:
		simple_gen(m-1, prefix+"0")
		simple_gen(m-1, prefix+"1")
		simple_gen(m-1, prefix+"2")

def gen_permutations(m:int, n:int, prefix=None):
	m = m if m != -1 else n
	prefix = prefix or []
	if m == 0:
		print (*prefix)
		return
	for number in range(1, n+1):
		if find(number, prefix):
			continue
		prefix.append(number)
		gen_permutations(m-1,n,prefix)
		prefix.pop()

def find(number, A):
	flag = False
	for x in A:
		if number == x:
			flag = True
			break
	return flag


if __name__ == "__main__":
	gen_number(2,2)
	simple_gen(3)
	gen_permutations(3,3)
