total = 0
for i in range(0, 101, 1):
    if i == 1:
        total = 1
    if i % 2 == 0:
        total += i
print(total)
