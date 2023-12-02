#number of whitespaces before the first star=number of rows-row number
row=int(input("Enter the number of rows: "))
for i in range(1,row+1):
    for space in range(1,row-i+1):
        print(end=' ')
    for star in range(1,i+1):
        print("*",end=' ')
    print('')    

