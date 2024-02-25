a = int(input())
cnt = 0

for i in range(a):
    checklist = []
    m = input()
    m_list = list(m)
    for x in range(len(m_list)):
        if x == 0:
            checklist.append(m_list[x])
        elif m_list[x] == m_list[x-1]:
            continue
        else:
            if m_list[x] not in checklist:
                checklist.append(m_list[x])
            else:
                cnt+=1
                break
        
result = a - cnt          
print(result)
