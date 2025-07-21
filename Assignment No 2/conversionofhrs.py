#convert the time entered in hh,min and sec into seconds

hours= int(input("enter hours: "))
min= int(input("enter min: "))
seconds= int(input("enter seconds: "))

totalseconds= (hours*3600)+(min*60)+seconds
print("total seconds: ",totalseconds)

