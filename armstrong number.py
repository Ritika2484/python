# an n digit armstrong number is a special number which is equal to the sum of its own digits ,each raised to the power of n 
#program to check whether a given 3-digit number is an Armstrong number
num=int(input("Enter a 3-digit number: "))
sum = 0
temp = num
while temp>0:
    digit=temp % 10
    sum +=digit **3
    temp//+10
if num == sum:
    print(f"{num} is an Armstrong number.")    
else:
    print(f"{num} is not an Armstrong number.")