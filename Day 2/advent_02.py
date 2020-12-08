def read_input(path):

    with open(path,'r') as input:
        lines = input.readlines()
    entries = []
    for item in lines:
        entry = item.rsplit(': ')
        entry[1] = entry[1].strip('\n')
        entries.append(entry)
    return entries
        
def parse_rules1(entry):
    #entry is the list of 2 items, rules and pwd
    rules = entry[0]
    pwd = entry[1]
    rules_num, rules_let = rules.split(' ')
    rules_num_low, rules_num_hi = rules_num.split('-')
    num_pwd = pwd.count(rules_let)

    if int(num_pwd) <= int(rules_num_hi) and int(num_pwd) >= int(rules_num_low):
        return True
    else:
        return False

def parse_rules2(entry):
    rules = entry[0]
    pwd = entry[1]
    rules_num, rules_let = rules.split(' ')
    rules_num_low, rules_num_hi = rules_num.split('-')
    #num_pwd = pwd.count(rules_let)

    num_low = int(rules_num_low)-1
    num_hi = int(rules_num_hi)-1
    pwd_low = pwd[num_low]
    pwd_hi = pwd[num_hi]

    #print(num_low, num_hi, pwd_low, pwd_hi)

    valid = False
    if pwd_low == rules_let:
        if pwd_hi != rules_let:
            valid = True
    else:
        if pwd_hi == rules_let:
            valid = True
    
    return valid


def puzzle1(inputs):
       
    i=0
    valid = 0
    while i< len(inputs):
        result = parse_rules1(inputs[i])
        if result == True:
            valid+=1
        i+=1

    print(str(valid) + ' valid entries in part 1!')

def puzzle2(inputs):
    i=0
    valid = 0
    while i< len(inputs):
        result = parse_rules2(inputs[i])
        #print(inputs[i])
        #print(result)
        if result == True:
            valid+=1
        i+=1

    print(str(valid) + ' valid entries in part 2!')
    

if __name__ == "__main__":
    inputs = read_input('Day 2\\advent_02_input.txt')
    #print(inputs)
    puzzle1(inputs)
    puzzle2(inputs)
    