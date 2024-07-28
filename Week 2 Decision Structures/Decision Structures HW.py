distance = float(input("Enter the distance in miles "))
speedlimit = float(input("Enter MPH speed limit"))
speed = float(input("Enter your average MPH "))

time = distance / speedlimit
speedtime = distance / speed

minhours = 60
speedtimemin = speedtime*minhours
timemin = time*minhours

    
print(f'time taken at speedlimit {timemin:.2f} minutes')
print(f'time taken at your speed {speedtimemin:.2f} minutes')

if speed > speedlimit:
    print(f'Time saved in min: {savedtime:.2f}')
    savedtime = timemin - speedtimemin
else:
    print("safe driver but no time saved")
