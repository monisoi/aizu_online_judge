import math

N = int(raw_input())
A = []
for i in range(N):
	A.append(int(raw_input()))

diff_max = -float('inf')
for i in range(N):
	for j in range(i+1, N):
		if diff_max < (A[j] - A[i]):
			diff_max = A[j] - A[i]

print diff_max