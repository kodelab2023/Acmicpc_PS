def find_divisors(num):
    return [i for i in range(1, num) if num % i == 0]

def is_perfect_number(num):
    if num <= 0:
        return False
    
    divisors = find_divisors(num)
    divisors_sum = sum(divisors)
    return divisors_sum == num

def represent_as_sum_of_divisors(num):
    divisors = find_divisors(num)
    return " + ".join(map(str, divisors))

while True:
    n = int(input())
    if n == -1:
        break
    if is_perfect_number(n):
        representation = represent_as_sum_of_divisors(n)
        print(f"{n} = {representation}")
    else:
        print(f"{n} is NOT perfect.")
