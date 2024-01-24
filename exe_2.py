def max_digit_rec(num,max_digit = None):
    if num == 0:
        return max_digit
    if max_digit is None or max_digit < num % 10:
        max_digit = num % 10
    return max_digit_rec(num//10,max_digit)
print(max_digit_rec(16375))

def max_digit(num):
    max_digit = 0
    while num > 0 :
        if max_digit < num % 10 :
            max_digit = num % 10
        num //= 10
    return max_digit

print(max_digit(16375))
    