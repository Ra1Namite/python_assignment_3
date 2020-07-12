my_list = [12, 11, 13, 5, 6]
for i in range(1, len(my_list)):
    key = my_list[i]
    k = i - 1
    while k >= 0 and key < my_list[k]:
        my_list[k+1] = my_list[k]
        k -= 1
    my_list[k+1] = key

print('sorted list:')
print(my_list)
