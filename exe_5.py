def  get_sum(arr,size):
    max_sum = None
    for i in range(len(arr)-size+1):
        temp_sum = 0
        for j in range(i,i+size):
            temp_sum += arr[j]
        if max_sum is None or max_sum < temp_sum:
            max_sum = temp_sum
    print (max_sum)



def get_size_rec(arr, size, j):
    if size == 0:
        return 0
    return arr[j] + get_size_rec(arr, size - 1, j + 1)

def get_sum_size_rec(arr, size, i):
    if i > len(arr) - size:
        return None
    my_sum = get_size_rec(arr, size, i)
    neighbor_sum = get_sum_size_rec(arr, size, i + 1)
    if neighbor_sum is None or my_sum > neighbor_sum:
        return my_sum
    return neighbor_sum

nums = [int(x) for x in input("Enter list numbers: ").split()]
size = int(input("Enter size: "))
size_sum = get_sum_size_rec(nums, size, 0)
print(f"Max sum of size {size} = {size_sum}")
