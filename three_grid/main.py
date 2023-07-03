def T(n):
    ans = 1
    for i in range(2, n):
        ans += (i-1)*T(n-i)
    return ans


for i in range(1, 100):
    print(i, T(i), 2**(i-2))