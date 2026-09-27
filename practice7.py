foods=["pizza","burger","momos","pasta"]
for i in foods:
    print(foods)

#write a program that prints all numbers from 100 to 1 using for and range().
for i in range(100,0,-1):
    print(i)

#1-10 but 7 skip karo how to do this 
for i in range(1,11):
    if i==7:
        continue
    print(i)

#😍NASTED LOOP
for i in range(1,4):
    for j in range(1,4):
        print(i,j)