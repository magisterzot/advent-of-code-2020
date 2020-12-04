
def read_input(path): 
#path is the file path string
    with open(path,'r') as input:
        lines = input.readlines()

    stripped_lines = []
    for i in lines:
        stripped_lines.append(i.rstrip())
    
    return stripped_lines

def move31(list,x,y): 
#list is the input grid (all lines same length)
#x and y the starting coordinates (upper left being 1,1)
       
    width = len(list[0])
    height = len(list)

    x+=3
    y+=1
    if x>=width:
        x= x-width
    return x, y

def movexy(list,x,y,dx,dy): 
#list is the input grid (all lines same length)
#x and y the starting coordinates (upper left being 1,1)
       
    width = len(list[0])
    height = len(list)

    x+=dx
    y+=dy
    if x>=width:
        x= x-width
    return x, y
    
def tree_state(str,x):
    state=str[x-1]
    return state

def count_trees(in_str,char,count):
#in_str is input string. char is the character to compare against
    if in_str == char:
        count +=1
    return count

def sled1(path):
    hill = read_input(path)
    x=1
    y=1
    count=0

    for i in hill:
        is_tree = tree_state(i,x)
        count=count_trees(is_tree,'#',count)
        next_line = move31(hill,x,y)
        x=next_line[0]
        y=next_line[1]
    return count

def sled2(path,dx,dy):
    hill = read_input(path)
    x=1
    y=1
    count=0
    i=0

    while i < len(hill):
        is_tree = tree_state(hill[i],x)
        count=count_trees(is_tree,'#',count)
        next_line = movexy(hill,x,y,dx,dy)
        x=next_line[0]
        y=next_line[1]
        i=i+dy
    return count

if __name__ == "__main__":

    #part1 = sled1('advent_03_input.txt')

    sl11 = sled2('advent_03_input.txt',1,1)
    sl31 = sled2('advent_03_input.txt',3,1)
    sl51 = sled2('advent_03_input.txt',5,1)
    sl71 = sled2('advent_03_input.txt',7,1)
    sl12 = sled2('advent_03_input.txt',1,2)
    part2 = sl11*sl31*sl51*sl71*sl12
    print(part2)