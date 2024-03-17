import sys
input = sys.stdin.readline

N = int(input().rstrip())

def sort_digits(number):
    digits = [int(digit) for digit in str(number)]
    sort_digits = sorted(digits, reverse=True)
    sorted_number = int(''.join(map(str, sort_digits)))
    return sorted_number

print(sort_digits(N))