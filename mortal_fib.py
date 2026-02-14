n = 36
m = 5
x = [0] * (n + 1)

x[0] = 1
x[1] = 1
x[2] = 1

for i in range(3, n + 1):
    if i <= m:
        x[i] = x[i - 1] + x[i - 2]
    else:
        x[i] = x[i - 1] + x[i - 2] - x[i - m - 1]
print(x[n])