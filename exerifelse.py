import time

timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
hour = int(time.strftime("%H", time.localtime()))

if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"
elif 17 <= hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

print("当前时间：", timestamp)
print(greeting)