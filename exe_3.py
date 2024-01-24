num = 333747755

def match_followin(num):
    count = 0
    while num > 10:
        if num % 10 == (num // 10) % 10 :
            count += 1
        num //= 10
    return  count


print(match_followin(num))

def match_followin_rec(num,count):
    if num <= 10:
        return count
    if num % 10 == num //10 %10 :
        count += 1
    return match_followin_rec(num//10 , count)

print(match_followin_rec(num,0))
