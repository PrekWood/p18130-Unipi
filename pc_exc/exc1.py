print("--SUMINTERVALS--")

def sumintervals(list):
    #Making a simpler list,so I can work with it easier
    new_list=[]
    for sublist in list:
        for item in sublist:
            new_list.append(item)

    #Starting to examine every interval one by one,trough the 'new_list'
    sum=0
    for i in range(len(new_list)):
        if i%2==1:
            print "->",list[i//2]#Printing the interval I'm working on each time

            start=new_list[i-1]#Setting the borders of each interval
            end=new_list[i]
            pos_start=i-1
            pos_end=i

            p='Outside other intervals'#Examiing the intervals' relationship to the other ,already registered,intervals
            dif=end-start
            for i in range(len(new_list)):
                if i%2==1 and i<pos_start and i<pos_end:
                    #The occassion that there is a larger interval,over these values,that has already been registered
                    if end>=new_list[i-1] and end<=new_list[i] and start>=new_list[i-1] and start<=new_list[i]:
                        p='Fully inside another interval'
                        dif=0
                    #The occassion that there is a smaller interval that includes some of the values of the interval being examined
                    elif start<=new_list[i-1] and end>=new_list[i]:
                        p='There is a smaller interval inside it'
                        dif=new_list[i-1]-start+end-new_list[i]
                    #The occassion that there is an interval that inclued the starting values of the one examined interval
                    elif start>=new_list[i-1] and start<=new_list[i]:
                        p='Starting inside another interval'
                        start=new_list[i]
                        dif=end-start
                    #The occassion that there is an interval that included the ending values of the examined interval
                    elif end>=new_list[i-1] and end<=new_list[i]:
                        p='Ending inside another interval'
                        end=new_list[i-1]
                        dif=end-start

            #Adding the length of each interval to the overall sum
            sum=sum+dif
            print p,'\n','The length of the interval is equal to :',dif,'\n'

    print '-->The result of the function Sumintervals is:',sum

print("->Please insert a list of Intervals")
x=input()
if type(x)==list:
    sumintervals(x)
else:
    print("Wrong input!")
