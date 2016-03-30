A = map(int, raw_input().split())
x = A[0] if A[0] >= A[1] else A[1]
y = A[1] if A[1] != x    else A[0]

r =  x % y
while r > 0:
	x = y
	y = r
	r = x % y

print y
