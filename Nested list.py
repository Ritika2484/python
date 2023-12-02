# l=[[1,2,3],[4,5,6],[4,8,9]]
# for i in range(0,len(l)):
#     for j in range(0,3):
#         print(l[i][j])
# p=0
# q=0
# i=int(input("Enter the number: "))
# for j in range(i):
#   p=j+1
#   q=i-p
#   print(" "*q,"*"*p)      
# p=0
# q=0
# i=int(input("Enter the number: "))
# for j in range(i):
#     p=j+1
# for j in range(i):
#     p=j+1
#     q=i-p
#     print 
# p=0
# i=int(input("Enter the number: "))
# for j in range(i):
#     p=j+1
#     print("*"*p)
# p=0
# q=0
# i=int(input("Enter the number: "))
# for j in range(i):
#     p=j+1
#     q=i-p
#     print(" "*q,"*"*p)
# 
# p=0
# q=0
# x=int(input("Enter the number: "))
# for i in range(x):
#     p=i+1
#     q=(x*2)-(p*2)
#     print("*"*p+" "*q+"*"*p)
  
# n = int(input("Enter the number: "))
# s = n*2-2
# for i in range(1,n+1):
#     print("*"*i + " "*s+"*"*i)
#     s =s-2
# l = []
# for i in range(1,5):
#     l1=[]
#     for j in range(1,5):
#         l1.append(int(input("number: ")))
#     l.append(l1)
# print(l)    
# p=0
# q=0
# i=int(input("Enter the number: "))
# for j in range(i):
#     p=j+1
#     q=i-p
#     print(" "*q,"*"*p)
# l=int(input("Enter the number: "))
# l=s
# for i in  range(l,l+1):
#     for j in range(l,s):
#         print(" ",end="")
#         for z in range(1,i+1):
#             print("*",end="")
#         s=s-1
#         print()
l=int(input())
for i in range(1,l+1):
    if i==1 :
        print("x")
    elif i==l:
        print('*'*l)
    else:
        print("*"+" "*(i-2)+"*")
