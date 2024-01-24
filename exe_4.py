def num_length(num):
    len = 1
    while num >= 10:
        len *= 10
        num //= 10
    return len

def similar_signif_num(num1,num2):
    len1 = num_length(num1)
    len2 = num_length(num2)
    count = 0
    similar = None
    while len1 > 0 and len2 > 0:
        if num1 // len1 != num2// len2:
            return similar
        similar = num1 // len1
        len1 //= 10
        len2 //= 10
    return similar

print (similar_signif_num(11300,11301))

def num_length_rec(num,num_length = 1):
    if num < 10:
        return num_length
    return num_length_rec(num // 10 , num_length *10)

def similar_signif_num_rec(num1,num2,len1=None,len2 =None,similar=None):
    if len1 is None :
        len1 = num_length_rec(num1)
        len2 = num_length_rec(num2)
    if len1 == 0 or len2 == 0:
        return similar
    if num1 // len1 == num2 // len2:
        similar = num1 //len1
    
    return similar_signif_num_rec(num1,num2,len1//10,len2//10,similar)

print(similar_signif_num_rec(102443,10230000))


        
