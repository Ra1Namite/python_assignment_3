#function definition
def linear_search(array, search_value):
    for _ in range(len(array)):

        if array[_] == search_value:
            return _
    return -1

#user input

my_list = list()
while True:
    n = input('enter numbers or (quit) to end:').strip()
    if n.lower() == 'quit':
        break
    elif n.isdigit():
        n = int(n)
    
    my_list.append(n)
print('List:')
print(my_list)

n = input('enter item to be searched: ').strip()
if n.isdigit():
    n = int(n)

#function call
output = linear_search(my_list, n)
if output == -1:
    print('value is not present in array')
else:
    print('value is present at index:',output)
