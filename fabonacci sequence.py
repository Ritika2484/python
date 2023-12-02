#write the program to print the fibonacci sequence as shown :
#0,1,1,2,3
#sequence in which each term is obtain by adding previous two term
#nth=(n-1)th+(n-2)th
n=int(input("Enter the number: "))
n1,n2=0,1
if n<=0:
    print("please enter the positive value")
elif n==1:
    print("fabonacci sequence:{n1}")
else:
    for n in range(n):
        print(n1,end=' ')
        n=n1+n2
        n1=n2
        n2=n    
  