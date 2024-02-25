total = 0
total2 = 0

for i in range(20):
    sub = input()
    sublist = sub.split()
    
    if sublist[2] != "P":
        total += float(sublist[1])
        def switch(key):
            grade = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0}
            return grade.get(key,0)
        total2 += float(sublist[1]) * float(switch(sublist[2]))
    else:
        continue
print(total2/total)