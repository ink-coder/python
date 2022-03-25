f1, f2, s = 0, 1, 0
while f2 <= 4000000:
    s = s + f2 if f2 % 2 == 0 else s
    f1, f2 = f2, f1 + f2
print(s)
