num = int(435827)
m = 8 % 10
a = 8 // 10
while a > 0:
    if a % 10 > m:
        a = a//10
print(m)
