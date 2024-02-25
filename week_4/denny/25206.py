for i in range(10):
    sub = input()
    sublist = sub.split()
    
    if sublist[2] != "P" and sublist[2] != "F":
        def switch(key):
            grade = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0}.get(key, "0")
            print({grade})
        switch(sublist[2])