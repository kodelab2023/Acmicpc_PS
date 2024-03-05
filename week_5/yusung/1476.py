E, S, M = map(int, input().split())

e_val, s_val, m_val, year = 1, 1, 1, 1

while(True):
    if e_val == E and s_val == S and m_val == M:
        break
    e_val+=1; s_val+=1; m_val+=1; year+=1
    if e_val>=16:
        e_val-=15
    if s_val>=29:
        s_val-=28
    if m_val>=20:
        m_val-=19
    
print(year)