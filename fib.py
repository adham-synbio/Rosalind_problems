n = 36
k = 5
x = [0] * (n + 1)

x[0] = 1
x[1] = 1
x[2] = 1
for i in range(3, n + 1):
    x[i] = x[i - 1] + k * x[i - 2]
print(x[n])
