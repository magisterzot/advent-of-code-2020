def parse_passports(path):
    with open(path,'r') as input:
        lines = input.read()

    #breaks up file into list with individual passports as entries
    passports = lines.rsplit('\n\n')
    entries = []

    #separates each individual passport into its own list
    i=0
    while i< len(passports):
        entry = passports[i].split()
        entries.append(entry)
        i+=1

    return entries

def data_validate(field,data):
#does this data meet the criteria? both strings
    data_valid = False

    if field == 'byr':
        if (len(data) <=4 and int(data)>=1920 and int(data)<=2002):
            data_valid =  True
    elif field == 'iyr':
        if (len(data) <=4 and int(data)>=2010 and int(data)<=2020):
            data_valid =  True
    elif field == 'eyr':
        if (len(data) <=4 and int(data)>=2020 and int(data)<=2030):
            data_valid =  True
    elif field == 'hgt':
        if len(data)>2:
            units = data[-2:]
            height = int(data[:-2])
            if (units == 'cm' and height>=150 and height<=193):
                data_valid =  True
            elif (units == 'in' and height>=59 and height<=76):
                data_valid =  True
                
    elif field == 'hcl':
        if (data[0]=='#' and len(data)==7):
            answer = True
            i=1
            while i<len(data):
                if data[i] not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                    answer = False 
                i+=1
            data_valid =  answer
    elif field == 'ecl':
        if data in ['amb','blu','brn','gry','grn','hzl','oth']:
            data_valid =  True
    elif field == 'pid':
        if (len(data) == 9 and data.isdecimal()):
            data_valid =  True
    elif field == 'cid':
        data_valid = True

    return data_valid

def validate(entry,fields):
#does this list meet the criteria of having all the fields?
    valid = True
    has_fields = []

    #make a pretty list of fields for this entry
    i=0
    while i<len(entry):
        field = entry[i][:3]
        has_fields.append(field)
        i+=1
    #print(entry)
    #print(fields)
    #print(has_fields)
    #check for the presence of the required fields

    j=0
    while j<len(fields):
        if fields[j] not in has_fields:
            valid = False
            break
        else:
            j+=1
            continue
    
    return valid

def run_puzzle1():
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    passports = parse_passports('advent_04_input.txt')

    valid_passports = 0

    i=0
    while i<len(passports):
        valid = validate(passports[i],fields)
        
        if valid == True:
            valid_passports+=1
        i+=1
    
    print(str(valid_passports) + ' valid passports found for puzzle 1!')

def run_puzzle2():
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    passports = parse_passports('advent_04_input.txt')
    
    valid_passports = 0

    i=0
    while i<len(passports):
        
        entry = passports[i]
        #print(entry)
        passport_valid = True
        valid = True

        j=0
        while j<len(entry):
            field = entry[j][:3]
            data = entry[j][4:]
            field_valid = data_validate(field,data)
            #print(field, data, field_valid)
            if field_valid==False:
                passport_valid = False
                break
            j+=1
            
        #print(passport_valid)
        if passport_valid == True:
            valid = validate(entry,fields)
            #print(valid)
            if valid == True:
                valid_passports+=1
        i+=1

    print(str(valid_passports) + ' valid passports found for puzzle 2!')

if __name__ == "__main__":
    run_puzzle1()
    run_puzzle2()

    
    