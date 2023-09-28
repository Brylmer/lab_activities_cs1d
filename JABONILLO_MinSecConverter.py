time = float(input("enter time in seconds: "))
time = time % (24 * 3600)
hour = time // 3600
time %= 3600

min = time // 60
time %=60
seconds = time
print("h:m:s-> %d:%d:%d" % (hour, min, seconds))