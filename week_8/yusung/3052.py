a = []
for i in range(10):
    b = int(input()) % 42
    a.append(b)

set_a = list(set(a))
print(len(set_a))