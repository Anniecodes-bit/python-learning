#write a program to print the multiplication table of any number using a while loop
n=int(input("Enter a number:"))
i=1
while i<=16:
    print(f"{n}*{i}={n*i}")
    i=i+1