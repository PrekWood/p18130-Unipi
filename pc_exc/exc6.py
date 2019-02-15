print("--THE MINESWEEPER--")

def check(x,table):#Making a function that will place the right number
    if table[x]=='[ ]':
        table[x]='[1]'
    elif table[x]=='[1]':
        table[x]='[2]'
    elif table[x]=='[2]':
        table[x]='[3]'
    elif table[x]=='[3]':
        table[x]='[4]'

def mine_table(n1,n2,m):
    #Making a list foul of empty brackets
    table=[]
    for i in range(n1*n2):
        item='[ ]'
        table.append(item)

    length=len(table)


    #Placing the mines
    import random
    for i in range(m):
        r=random.randint(0,length-1)
        table[r]=' M '

    #Adding the numbers
    for i in range(length):
        if table[i]==' M ':
            #Up
            if i>=n1:#Excluding the first line
                cell=i-n1
                check(cell,table)
            #Down
            if (i+n1)<=(length-1):#Excluding the last line
                cell=i+n1
                check(cell,table)
            #Right
            if (i+1)<=(length-1) and ((i+1)%n1)!=0:#Excluding the last column
                cell=i+1
                check(cell,table)
            #Left
            if (i%n1)!=0:#Excluding the first column
                cell=i-1
                check(cell,table)
            #Down-Right
            if (i+n1+1)<=(length-1) and ((i+1)%n1)!=0:#Excluding the last line and the last column
                cell=i+n1+1
                check(cell,table)
            #Down-Left
            if (i+n1-1)<=(length-1) and i%n1!=0:#Excluding the last line and th first column
                cell=i+n1-1
                check(cell,table)
            #Up-Left
            if i>n1 and i%n1!=0:#Excluding the fist line and the first column
                cell=i-n1-1
                check(cell,table)
            #Up-Right
            if i>=n1 and (i+1)%n1!=0:#Ecluding the first line and the last column
                cell=i-n1+1
                check(cell,table)

    #Printing the table
    for i in range(length):
        if i%n1==0:
            print('\n')
        print table[i],

print('\n->Please input the number of lines')
num1=input()
print('\n->Please input the number of columns')
num2=input()
print('\n->Please input the number of the mines')
mine=input()
if type(num1)==int and type(num2)==int and type(mine)==int:
    mine_table(num1,num2,mine)
else:
    print("Wrong input!")
