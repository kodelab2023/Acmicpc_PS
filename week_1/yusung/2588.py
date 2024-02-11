A = int(input())
B = int(input())
B_1 = B//100
B_2 = (B%100)//10
B_3 = B%10
print(A*B_3)
print(A*B_2)
print(A*B_1)
print((A*B_1*100)+(A*B_2*10)+A*B_3)