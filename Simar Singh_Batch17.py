import time
​
#time
a = time.time()
print("Seconds : ",a , "\n")
​
#Converting Date to string
print("Current Date and Time: ")
print(time.ctime(a))
​
#sleep
time.sleep(1)
print("\nExection starts after one second...")
​
#localTime
print("Local Time: ")
print(time.localtime(a), "\n")
​
#gmtime
print("Local Time in UTC format")
print(time.gmtime(a),"\n")
​
#mktime
print("Current time in Seconds...")
b =(2021,11,12,15,43,34,5,314,0)
print(time.mktime(b),"\n")
​
#strftime
c = time.localtime()
d=time.strftime("%m,%d,%Y,%H,%M,%S",c)
print("Representing date and time in string: ",d,"\n")
​
#strptime
e="12 NOVEMBER, 2021"
f= time.strptime(e,"%d %B, %Y")
print(f)
