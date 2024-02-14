
print("Please enter the time.")
print("Hour?")
hour=int(input())
while hour > 12:
   break
print("Minutes?")
minutes=int(input())
print("AM or PM?")
answer=str(input())
if answer=="AM":
   hour=hour+0
   print(hour,":",minutes)
else:
   hour=hour+12
   print("Your time in 24-hour system is",hour,minutes)


   



