def read_input1(path):
    with open(path,'r') as input:
        doc = input.read()
    inputs = doc.rsplit('\n\n')
    #print(inputs)
    entries = []
    for i in range(len(inputs)):
        entry = inputs[i].split('\n')
        row = ''
        for j in range(len(entry)):
            row += entry[j]
        entries.append(row)
    return entries

def read_input2(path):
    with open(path,'r') as input:
        doc = input.read()
    inputs = doc.rsplit('\n\n')
    #print(inputs)
    entries = []
    for i in range(len(inputs)):
        entry = inputs[i].split('\n')
        row = ''
        for j in range(len(entry)):
            row += entry[j]
        entry.insert(0,list(set(row)))        
        entries.append(entry)
    return entries

def count_yes(str):
    return len(set(str))


def count_all_yes(list):
#first element of the list is the set of unique letters included
    
    unique = list[0]
    total = 0
    for i in range(len(unique)):    #cycle through each unique answer
        j=1
        in_all = True
        
        while j <len(list):      #does the answer appear in all entries?

            if unique[i] not in list[j]:
                in_all = False
                
            j+=1
            
    
        if in_all == True:
            total+=1
    return total

def puzzle1(inputs):
    total = 0
    for entry in range(len(inputs)):
        total+=count_yes(inputs[entry])
    
    print(str(total) + ' total yes answers for part 1.')

def puzzle2(inputs2):
    running_total = 0

    for i in range(len(inputs2)):
        #print(inputs2[i])
        total = count_all_yes(inputs2[i])
        #print(total)
        running_total+=total

    print(str(running_total) + ' total unanimous answers for part 2!')

if __name__ == "__main__":
    inputs1 = read_input1('Day 6\\adv_06_input.txt')
    inputs2 = read_input2('Day 6\\adv_06_input.txt')
    
    puzzle1(inputs1)
    puzzle2(inputs2)


    