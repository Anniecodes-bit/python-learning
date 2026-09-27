#With keyword
#file=open("mast.txt","r")
#data= file.read
#print("File Data",data)
#file.close()

#with open("mast.txt", "r") as f:
    #data= f.read()
    #print("File Data",data)

# with open("newTestfile.py","r") as f:
#     line1=f.readline()
#     line2=f.readline()
#     line3=f.readline()
#     line4=f.readline()
#     print("Line 1",line1) 
#     print("Line 2",line2)
#     print("Line 3",line3)
#     print("Line 4",line4)
#read all lines
with open("newTestfile.py","r") as f: 
    readlinesMethod= f.readlines()
    print("readlinesMethod",readlinesMethod) 