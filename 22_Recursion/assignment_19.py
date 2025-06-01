from assignment_18 import is_odd_number

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    s = n + sum_of_natural_numbers(n-1)
    return s

def sum_of_odd_natural_numbers(n):
    if n == 1:
        return 1
    if is_odd_number(n):
        s = n + sum_of_odd_natural_numbers(n-1)
        return s
    return sum_of_odd_natural_numbers(n - 1)

def sum_of_even_natural_numbers(n):
    if n >= 2:
        if not is_odd_number(n):
            s = n + sum_of_even_natural_numbers(n-1)
            return s
        return sum_of_even_natural_numbers(n - 1)
    else:
        return 0

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def get_sqr(n):
    return n*n

def sum_of_sqr_of_natural_numbers(n):
    if n == 1:
        return 1
    s = get_sqr(n) + sum_of_sqr_of_natural_numbers(n-1)
    return s

# print(sum_of_natural_numbers(5))
# print(sum_of_odd_natural_numbers(3))
# print(sum_of_even_natural_numbers(5))
# print(factorial(6))
# print(sum_of_sqr_of_natural_numbers(4))
