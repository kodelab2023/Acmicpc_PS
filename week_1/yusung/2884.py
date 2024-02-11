hours, minutes = map(int, input().split())
if(minutes<45):
    minutes = minutes+15
    if(hours==0):
        hours = 23
        print(hours, minutes)
    else:
        hours = hours -1
        print(hours, minutes)
else:
    minutes = minutes -45
    print(hours, minutes)