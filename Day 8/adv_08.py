def read_input(path):
    with open(path,'r') as input:
        lines = input.readlines()
    entries = []
    for i in range(len(lines)):
        entries.append(lines[i].strip())
    return entries

def get_fun(str):
    function = str.split(' ')[0]
    
    arg = str.split(' ')[1]
    print(function,arg)
    if arg[0]=='+':
        arg = int(arg[1:])
    elif arg[0]=='-':
        arg = -int(arg[1:])

    #print(arg)
    return function,arg

def run_fun(str,int,accumulator,index):
    if str == 'acc':
        accumulator+=int
        index+=1
    elif str == 'jmp':
        index+=int
    elif str == 'nop':
        index+=1
    else:
        print('Invalid inputs!')
    #print(accumulator,index)
    return accumulator,index

def puzzle1(input):
    accumulator = 0
    index = 0
    used_indices=[]
    
    while index < len(input):
        ready_to_run = get_fun(input[index])
        result = run_fun(ready_to_run[0],ready_to_run[1],accumulator,index)
        
        print(result)
        accumulator = result[0]
        index = result[1]
        if index in used_indices:
            print('Just hit a step for the second time!')
            print('Accumulator=' + str(accumulator) + 'Index=' + str(index))
            break
        else:
            used_indices.append(index)
    
    print(accumulator)

if __name__ == "__main__":
    input = read_input('Day 8\\adv_08_input.txt')
    
    puzzle1(input)
   

    
        


    


    

        
        

    


    