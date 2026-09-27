
#function defination with parameter
def average(a=10,b=40):
    averageValue=a+b/2
    print(averageValue)
#Function Calling with Arguments
average(5,10)
average(50,80)
average(34,70)
average(2,4)
average()
#Write a function , show_age(name,age) that prints:"Annie is 17 years old."
def show_age(name,age):
    print(f"{name}is{age} years old")
show_age("Annie",17)
show_age("Mani",20)
#creat a  funcion add_numbers(a,b) that prints both the sum and difference.
def add_numbers(a,b):
    print("sum=",a+b)
    print("Difference=",a-b)
add_numbers(20,40)
#write  a function fav_food (food) that prints "Annie loves <food>"
def fav_food(food):
    print(f"Annie loves{food}")
fav_food("chicken")
fav_food("kabab")
fav_food("Jagannath prasad")