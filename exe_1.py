def max_sum_for_value(num_list):
    d = {}
    max  = None 
    for num in num_list:
        if num in d :
            d[num] += num
        else :
            d[num] = num
        if max is None or max < d[num]:
            max = d[num]
            num_for_max = num

    return num_for_max
print(max_sum_for_value([1,2,1,5,3,6,2,5,4,8,9,5,8,8]))


def value_dict_rec(num_list,i,d={},max=None,num=None):
    if i == len(num_list):
        return num 
    if num_list[i] in d:
        d[num_list[i]] += num_list[i]
        
    else : 
        d[num_list[i]] = num_list[i]

    if max is None or max < d[num_list[i]]:
        max = d[num_list[i]]
        num = num_list[i]
    return value_dict_rec(l,i+1,d,max,num)
     
l = [1,2,1,5,3,6,2,5,4,8,9,5,8,8]
      

max = value_dict_rec(l,0)
print (max)

    
    
       