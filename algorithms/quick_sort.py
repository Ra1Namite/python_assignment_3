def divide_parts(array, low, high):
    i = low -1 
    pivot_element = array[high]
    for j in range(low, high):

        if array[j] < pivot_element:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quick_sorting(array, low, high):
    if low < high:
        x = divide_parts(array, low, high)
    
        quick_sorting(array, low, x-1)
        quick_sorting(array, x+1, high)

#user input

my_list = list()
while True:
    n = input('enter numbers or (quit) to end:').strip()
    if n.lower() == 'quit':
        break
    elif n.isdigit():
        n = int(n)
    
    my_list.append(n)
print('unsorted list:')
print(my_list)


#function calls

length = len(my_list)
quick_sorting(my_list, 0, length-1)
print('Sorted array:')
print(my_list)



