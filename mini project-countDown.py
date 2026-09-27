#Goal:
#print a countdown before something "exciting" happens (like"Launching "happy new year!").
count=int(input("Enter the counter num:"))
import time
print("/n coundawn starts now:")
for i in range(count,0,-1 ):
    print(i)
    time.sleep(2)

print("/n wohoo! Happy New Year")