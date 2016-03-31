N = int(raw_input())
A = []
for i in range(N):
	A.append(int(raw_input()))

prime_cnt = 0
for num in A:
	divisor_cnt = 0
	for i in range(1, num+1):
		if num % i == 0:
			divisor_cnt += 1
	if divisor_cnt == 2:
		prime_cnt += 1

print prime_cnt


