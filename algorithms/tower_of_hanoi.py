def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f'move disk 1 form {from_rod} to {to_rod}')
        return
    
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f'move disk {n} from rod {from_rod} to {to_rod}')
    tower_of_hanoi(n-1,aux_rod, to_rod,from_rod)

#user input

n = int(input('enter number of disk: ').strip())
tower_of_hanoi(n, 'x', 'z', 'y')
