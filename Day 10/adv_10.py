def read_input(path):
    with open(path,'r') as input:
        lines = input.readlines()
    entries = [int(line.strip()) for line in lines]
    entries.sort()
    return entries

def end_chargers(list):
    #print(list)
    #print(list[-1])
    list.append(list[-1]+3)
    list.insert(0,0)
    return list

def find_diff(list):
        
    dif1 = 0
    dif2 = 0
    dif3 = 0
    i=1
    while i<len(list):
        diff = list[i]-list[i-1]
        #print(diff)
        if diff == 1:
            dif1+=1
        elif diff == 2:
            dif2+=1
        elif diff == 3:
            dif3+=1
        else:
            print("Something went wrong")
            break
        i+=1
    return dif1,dif2,dif3


if __name__ == "__main__":
    input = end_chargers(read_input('Day 10\\adv_10_test.txt'))
    #print(input)
    diffs = find_diff(input)
    print(str(diffs[0]*diffs[2]) + ' is the product of jumps of 1 and jumps of 3 for part 1.' )

    '''
    total_paths = 0
    i=0
    index=0
    num_paths = []
    while i<len(input):
        num=input[i]
        paths = 0
        
        #index=i

        for j in range(i,len(input)):
            if input[j]>input[i] and input[j]<=input[i]+3:
                duple = [i,input[j]]
                num_paths.append(duple)
        
        print(num_paths)
        print(max(num_paths))

        i=num_paths.index(max(num_paths))+1
        print(i)
        
        paths+=len(num_paths)
        #print(paths)
        total_paths+=paths
        #print(total_paths)
        index+=1
        if index>100:
            break
    
    print(total_paths)
    #return total_paths        
    '''

        




    
    
   

    
        