import itertools

def disp(temp):
	for x in temp:
		print x,
	print 

def oneFac(num):
	len = num**(1/2.0)
	i = 2
	while i <= len:
		if num % i == 0:
			return i
		i += 1
	return 0

def baseNo(base, num):
	j = 0
	s = 0
	for i in reversed(map(int, str(num))):
		s += pow(base,j) * i
		j += 1

	return s

def solve(N, J):
	table = list(itertools.product([1, 0], repeat=N-2))
	temp = []
	for row in table:
		num = int('1' + (reduce(lambda rst, d: str(rst) + str(d), row)) + '1')
		prime = 0
		for i in xrange(2,11):
			fac = oneFac(baseNo(i, num))
			if fac == 0:
				prime = 1
				break
			else:
				temp.append(fac)
		if prime == 0:
			temp.insert(0, num)
			disp(temp)
			J -= 1
			if J == 0:
				return
		del temp[:]
			

for t in xrange(1, input()+1):
	N, J = map(int, raw_input().split())
	print "Case #{0}:".format(t)
	solve(N, J)
