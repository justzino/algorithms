dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0

a, b = map(int, input().split())

for i in range(a - 1):
    day = day + dayList[i]
day = (day + b) % 7

print(weekList[day])
