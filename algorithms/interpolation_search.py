def interpolation_serach(array,n, search_value):
    low = 0
    high = n-1

    while low <= high and search_value >= array[low] and search_value <= array[high]:
        if low == high:
            if array[low] == x:
                return low
            return -1
        index  = low + int(((float(high - low) / 
            ( array[high] - array[low])) * ( search_value - array[low])))     

        if array[index] == search_value:
            return index
        if array[index] < search_value:
            low = index +1
        else:
            high = index -1
    return -1

#user input
my_list = list()
print('enter item in list')
while True:
    n = input('enter numbers or (quit) to end:').strip()
    if n.lower() == 'quit':
        break
    elif n.isdigit():
        n = int(n)
    
    my_list.append(n)
my_list = sorted(my_list)
print('sorted array:')
print(my_list)
high = len(my_list) - 1
search = input('enter item to be searched: ').strip()
if search.isdigit():
    search = int(search)

#function call
length = len(my_list)

output = interpolation_serach(my_list, length, search)
if output == -1:
    print('value not found')
else:
    print('value at index:',output)
