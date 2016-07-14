# https://www.hackerrank.com/contests/infinitum12/challenges/a-birthday-party
# the number of solutions would be the total 99991 to the power of dependent rows/columns
# the number of dependent rows it n - number of dependent. The easiest way is to triangulate the
# matrix and this is done by standard algorithm the only addition is that we need to work in
# Modular arithmetic (is not done here). So division is modular inverse and minus is modular minus
def triangulate(A):
    n = len(A)
    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[j], A[i] = A[i], A[j]
                    break
        for j in range(i+1, n):
            if A[i][i] != 0:
                la = A[j][i]/A[i][i]
                for k in range(i, n):
                    A[j][k] = A[j][k] - la*A[i][k]
    return A

def dimKer(A):
    T = triangulate(A)
    return sum(1 for i in range(len(T)) if T[i][i] == 0)

N, M = input(), []
for i in range(N):
    x = list(map(int, raw_input().split()))[1:]
    M.append([1*(j in x) for j in range(1,N+1)])

for i in range(N):
    M[i][i] = -1

print pow(99991, dimKer(M), 10**9 + 7)