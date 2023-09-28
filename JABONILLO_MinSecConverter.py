time = float(input("enter time in seconds: "))
time = time % (24 * 3600)
hour = time // 3600
time %= 3600

min = time // 60
time %=60
seconds = time
print("hour > %d" %(hour))
print("minute > %d" %(min))
print("second > %d" %(seconds))
