from copy import copy
from itertools import count

l_temperature: list[float] = []
temperature: float = 0
num_of_input: int = 0
while not temperature == -999:
    temperature: float = float(input("Enter temperature:"))
    num_of_input += 1
    if -50 < temperature < 50:
        l_temperature.append(temperature)
more_l_temperature: list[float] = [-20.0, 39.1, 18.5]
l_temperature.extend(more_l_temperature)
print(l_temperature)
list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]
list3 = list1 + list2  # list1 + list2
list4 = list1.extend(list2)  # None
print("the max temperature", max(l_temperature))
print("the max temperature", min(l_temperature))
if 18.5 in l_temperature:
    print(True)
else:
    print(False)
print(l_temperature.count(-20.0))  # עשיתי הדפסה כי רציתי לראות שזה עובד
for i in range(len(l_temperature)):
    print(f"for-each every temperature:{l_temperature[i]}", end="\n")
for i in range(len(l_temperature)):
    if l_temperature[i] == 39.1:
        print(i)
del l_temperature[0]
del l_temperature[::2]
if 18.5 in l_temperature:  # כדאי לבדוק כי אם הוא לא קיים הוא יעצור את התכנית
    l_temperature.remove(18.5)
temp_last: float = l_temperature.pop(-1)
print(l_temperature)
list11 = l_temperature.copy()
list11.sort()
list111 = list11.copy()
print(list111)
list111.sort(reverse=True)
print(list111)