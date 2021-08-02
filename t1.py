def find(number, A):
	for x in A:
		if number == x:
			return True
	return False

def gen_perm(M=-1,N:int,prefix=None):
	M = M if M != -1 else N
	prefix = prefix or []
	if M == 0:
		print (*prefix)
		return
	for number in range(1, N+1):
		if find(number, prefix):
			continue
		prefix.append(number)
		gen_number(M-1, N, prefix)
		prefix.pop()

if __name__ == "__main__":
	print ("Start")
	gen_number(3,2)