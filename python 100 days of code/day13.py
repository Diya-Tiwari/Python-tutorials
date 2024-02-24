import time
timeline=time.strftime("%H:%M:%S")
print(timeline)
timeline=int(time.strftime("%H"))
print(timeline)
timeline=int(time.strftime("%M"))
print(timeline)
timeline=int(time.strftime("%S"))
print(timeline)
if(4<timeline>=12):
    print("GOOD MORNING!")
elif(12<timeline>=16):
    print("GOOD AFTERNOON!")
elif(16<timeline>=20):
    print("GOOD EVENING!")
else:
    print("GOOD NIGHT!")