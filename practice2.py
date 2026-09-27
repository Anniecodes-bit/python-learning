#you are given a list of programmng languages :
#["python","java","c++","python","java","c"]
#convert it into a set and print how many unique languages Annie knows.
programmingList=["python","java","c++","python","java","c"]
print(type(programmingList))
#how to convert a list into set
programmingSet=set(programmingList)
print(type(programmingSet))
print("Annie knows these many languages",len(programmingSet))