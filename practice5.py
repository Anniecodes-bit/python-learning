# print how many lines are present in notes.txt
with open("notes.txt","r") as f:
    listOfLines=f.readlines()
    print("Output of readLines Funciton",listOfLines)
    print("Number of lines in file",len(listOfLines))
