def read_input(path):
    with open(path,'r') as input:
        lines = input.readlines()
    entries = []
    for i in range(len(lines)):
        entries.append(lines[i].strip('\n. '))
    return entries

def parse_rules(str):
    rules = []
    outside_bag = str.split(' contain ')
    inside_bags = outside_bag[1].split(', ')
    rules.append(outside_bag[0])
    rules.append(inside_bags)
    print(rules)
    return rules

def can_have(str,list): #str is the color (e.g. 'dark olive'). list is the rule list output by parse_rules
    has = False
    j=1
    while j<len(list):
        for i in range(len(list[j])):
            if str in list[j][i]:
                has = True
        j+=1
    print(has)
    return has


if __name__ == "__main__":
    rules = read_input('Day 7\\adv_07_test.txt')
    print(rules)

    search = 'shiny gold'

    total_has = 0


   


    print(str(total_has) + ' bags can contain ' + search + ' bags.')
        
        

    


    