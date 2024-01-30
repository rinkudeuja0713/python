import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamph = time.strftime('%H')
print(timestamph)
timestampm = time.strftime(':%M')
print(timestampm)

# create a program that says good morning/evening/afternoon according to the time
print("hello sir")
timestamp0 = time.strftime('%H:%M:%S')
timestamp1 = time.strftime('%H')
timestamp11 = int(timestamp1)

if 0 <= timestamp11 < 12 :
    print("Good Morning ! It is currently ", timestamp0)
elif 12 <= timestamp11 <= 18:
    print("Good Afternoon ! It is currently ", timestamp0)
elif 18 < timestamp11 <= 22:
    print("Good Evening ! It is currently ", timestamp0)
else:
    print("Good Night ! It is currently ", timestamp0)



