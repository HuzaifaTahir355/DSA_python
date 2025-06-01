# Print first N natural Numbers
def print_natural_number(n):
    if n > 0:
        print_natural_number(n - 1)
        print(n)

# Print first N natural Numbers in reverse Order
def print_reverse_natural_number(n):
    if n > 0:
        print(n)
        print_reverse_natural_number(n-1)

# Print first N natural odd Numbers
def is_odd_number(num):
    if num % 2 == 0:
        return False
    else:
        return True

def print_odd_natural_number(n):
    if n > 0:
        print_odd_natural_number(n-1)
        if is_odd_number(n):
            print(n)

# Print first N natural even Numbers
def print_even_natural_number(n):
    if n > 0:
        print_even_natural_number(n-1)
        if not is_odd_number(n):
            print(n)

# Print first N natural even Numbers in reverse order
def print_reverse_even_natural_number(n):
    if n > 0:
        if not is_odd_number(n):
            print(n)
        print_reverse_even_natural_number(n-1)

# Print first N natural odd Numbers in reverse order
def print_reverse_odd_natural_number(n):
    if n > 0:
        if is_odd_number(n):
            print(n)
        print_reverse_odd_natural_number(n-1)




# print_natural_number(5)
# print_reverse_natural_number(5)
# print_odd_natural_number(9)
# print_even_natural_number(9)
# print_reverse_even_natural_number(10)
# print_reverse_odd_natural_number(10)