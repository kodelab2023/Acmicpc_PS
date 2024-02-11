hours, minutes = map(int, input().split())
add_minutes = int(input())
minutes += add_minutes
hours += minutes//60
hours %=24
minutes%=60
print(hours, minutes)