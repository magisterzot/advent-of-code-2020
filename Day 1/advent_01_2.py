def adv01(file):

    txtfile = open(file,"r")
    data = txtfile.read()
    datalist = data.split("\n")
    #print(datalist)

    num1 = 0
    num2 = 0
    num3 = 0

    for i in datalist:
        di=int(i)
        tot = di

        for j in datalist:
            dj = int(j)
            tot = di + dj

            for k in datalist:
                dk = int(k)
                tot = di + dj + dk

                if tot == 2020:
                    num1 = di
                    num2 = dj
                    num3 = dk
                    break


    print(num1)
    print(num2)
    print(num3)
    print(num1+num2+num3)
    print(num1*num2*num3)        


adv01('advent_01.txt')