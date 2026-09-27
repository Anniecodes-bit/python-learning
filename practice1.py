#Write a program to read a text from a given file certificate.txt and find whether it contains the word live.
file= open("test.txt","r")
dataOfFile=file.read()
dataOfFile=dataOfFile.lower()
if "live" in dataOfFile:
    print("Yeshh Live word is present in the file")
else:
    print("No")
file.close()
#import os
#os.remove("test.txt")
#RENAMING THE FILE
os.rename("file.txt","test1.txt")