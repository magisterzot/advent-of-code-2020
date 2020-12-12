from copy import deepcopy 

def read_input(path):
    with open(path,'r') as input:
        lines = input.readlines()
    entries = [line.strip() for line in lines]
    array = [list(entry) for entry in entries]
    return array

def adjacents(array,y,x):
    adjacents = []
    #new_array = array
    
    for i in range(x-1,x+2):
        #print(i)
        for j in range(y-1,y+2):
            #print(i,j)
            if j in range(0,len(array)) and i in range(0,len(array[0])) and [x,y]!=[i,j]:
                adjacents.append(array[i][j])
            
                
    #print_chart(new_array)
    return adjacents

def print_chart(array):
    for i in range(len(array)):
        row=''
        for j in range(len(array[0])):
            row+=array[i][j]
        print(row)
    print('')

def populate(array):
    new_array = deepcopy(array)

    for i in range(len(array)):
        for j in range(len(array[0])):
            adj = adjacents(array,j,i)
            #print(adj)
            if array[i][j]=='L' and '#' not in adj:    
                new_array[i][j]='#'
            elif array[i][j]=='#' and adj.count('#')>=4:
                new_array[i][j]='L'

    #print_chart(new_array)
    return new_array

def count_occ(array):
    occ=0
    for i in range(len(array)):
        occ+=array[i].count('#')
    return occ

def puzzle1(input):
    new_input = deepcopy(input)
    prev_input = []
    #print_chart(input)
    occupied = []
    while new_input!=prev_input:
        prev_input = deepcopy(new_input)
        new_input = populate(new_input)
        #print_chart(new_input)
        #print(count_occ(new_input))
        occupied.append(count_occ(new_input))
        #print('\n')
    print(occupied[-1])

if __name__ == "__main__":
    input = read_input('Day 11\\adv_11_input.txt')
    
    puzzle1(input)
    


    

    

        

        




    
    
   

    
        