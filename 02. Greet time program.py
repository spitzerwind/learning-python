import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timesstamp = time.strftime('%H')
# timesstamp = (input("enter the leading hour of the day:"))

# if timesstamp >'5' and timesstamp < '12':
if  '5'  <= timesstamp < '12':
    print("good morning")
elif '12'<= timesstamp < '18':
    print("good afternoon") 
elif '18' <= timesstamp < '22':
    print("good evening")
else : print("good night")
