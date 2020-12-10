def read_input(path):
    with open(path,'r') as input:
        lines = input.readlines()
    entries = [int(line.strip()) for line in lines]
    return entries

def make_sums(list):
#generate list of all possible pairwise sums where the number is different
    sum_list = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=j:
                sum_list.append(int(list[i])+int(list[j]))
    return sum_list

def find_invalid(list,num):
    valid = True
    inv_value = 0
    inv_index = 0
    i=num
    while i<len(list):
        sub_list = make_sums(list[i-num:i])
        sub_list.sort()
        #print(sub_list)
        #print(list[i])
        if list[i] not in sub_list:
            valid = False
            inv_value = list[i]
            inv_index = i
            break
        i+=1
    return valid,inv_value,inv_index

if __name__ == "__main__":
    input = read_input('Day 9\\adv_09_input.txt')
    #print(input)

    valid_test = find_invalid(input,25)
    print('Number '+ str(valid_test[1])+ ' failed the first test!')
    
    
   

    
        


    


    

        
        

    


    