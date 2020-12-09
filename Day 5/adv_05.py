def read_input(path):
    with open(path,'r') as input:
        lines = input.readlines()
    entries = []
    for i in range(len(lines)):
        entries.append(lines[i].strip())
    return entries

def find_seat(str,num,lower_str,upper_str):
    pos_max = num
    pos_min = 0
    


    for i in range(len(str)):
        if str[i] == upper_str:
            pos_min += int((pos_max-pos_min)/2)
        elif str[i] == lower_str:
            pos_max -= int((pos_max-pos_min)/2)
        else:
            print('Invalid letters!')
            
        #print(pos_min,pos_max)
    
    seat = pos_min
    return seat

def puzzle1(input):
    ids = []
    for i in range(len(input)):
        row_str = input[i][:7]
        col_str = input[i][-3:]
        #print(input[i])
        row = find_seat(row_str,128,'F','B')
        col = find_seat(col_str,8,'L','R')
        seat_id = row*8+col
        ids.append(seat_id)
        #print(seat_id)
    
    print('The max seat ID for puzzle 1 is ' + str(max(ids)))

def puzzle2(input):
    taken = []
    ids = []

    for i in range(len(input)):
        row_str = input[i][:7]
        col_str = input[i][-3:]
        #print(input[i])
        row = find_seat(row_str,128,'F','B')
        col = find_seat(col_str,8,'L','R')
        seat = [row,col]
        seat_id = row*8+col
        taken.append(seat)
        ids.append(seat_id)

    ids.sort()

    id=1
    while id <len(ids):
        
        if ids[id] != ids[id-1] + 1:
            return ids[id]-1
        id+=1 
   

if __name__ == "__main__":
    input = read_input('Day 5\\adv_05_input.txt')

    puzzle1(input)
    seat = puzzle2(input)    
    print('My seat is '+str(seat))
    

    

    