#Making a fuction that turns every number written in words into intergers
def numberizaton(x):
    if x=='one':
        num=1
    elif x=='two':
        num=2
    elif x=='three':
        num=3
    elif x=='four':
        num=4
    elif x=='five':
        num=5
    elif x=='six':
        num=6
    elif x=='seven':
        num=7
    elif x=='eight':
        num=8
    elif x=='nine':
        num=9
    return(num)

#Making a function that takes as parameters the two numbers and the operator in characters and executes the calculation
def calculator(list,n1,n2):
    if list[1]=='plus':
        result=n1+n2
    elif list[1]=='minus':
        result=n1-n2
    elif list[1]=='times':
        result=n1*n2
    return(result)

print('-WORD CALCULATOR-\n-->Please enter the operation:')
x=raw_input()
if type(x)!=str:
    print("Wrong input!")
else:
    list=x.split("(")#Splitting the input
    n1=list[0]
    n2=list[2]
    num1=numberizaton(n1)
    num2=numberizaton(n2)
    result=calculator(list,num1,num2)
    print "\n", num1,list[1],num2,"=",result
