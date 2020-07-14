def binary_search(array, low, high, search_value):
    
    
    if high >= low:
        mid = (low + high)//2
        if array[mid] == search_value:
            return mid
        elif array[mid] > search_value:
            return binary_search(array,low, mid-1,search_value)
        else:
            return binary_search(array, mid+1, high, search_value)
        
    else:
        return None

#user input

my_list = list()
while True:
    n = input('enter numbers or (quit) to end:').strip()
    if n.lower() == 'quit':
        break
    elif n.isdigit():
        n = int(n)
    
    my_list.append(n)
print('array:')
print(my_list)
high = len(my_list) - 1
n = input('enter item to be searched: ').strip()
if n.isdigit():
    n = int(n)

output = binary_search(my_list, 0 , high, n)

if output == -1:
    print('value not found')
else:
    print('value found at index:',output)
