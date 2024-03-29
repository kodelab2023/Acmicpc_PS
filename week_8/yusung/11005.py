import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r].upper()
    else:
        return convert(q, base) + tmp[r].upper()
s, n = map(int, input().split())
print(convert(s, n))