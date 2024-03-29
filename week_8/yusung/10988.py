s = input()
rev_s = s[::-1]  # 문자열을 슬라이싱하여 뒤집음
if s == rev_s:
    print(1)
else:
    print(0)