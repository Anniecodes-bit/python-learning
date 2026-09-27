#write a program that prints the sum of first n natural numbers.
#for example,if n=5,then output should be 1+2+3+4+5=15
#(Hint:keep a running total inside the loop.)
n=int(input("Enter a numbers:"))
sum=0
while n>=1:
    sum= sum + n
    n= n-1
print("sum=",sum)
print("n=")

#write a program to print this pattern using a while loop:
#*
#**
#***
#****
n=1
while n<=4:
    print("*"*n)
    n= n+1
print("we are out of the while loop,and value of n should be 5.is it 5?check: ",n)

i=1
while i<=5:
     print(i,"Annie")
     i+=1
     


