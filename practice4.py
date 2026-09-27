#read only the first line of bio.txt
try:
    with open("bio.txt","r") as f:
      line1=f.readline()
      print("Line 1",line1)
except:
    print("That files doesnot exits")