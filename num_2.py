numbers: list[int] = []
SENTINEL: int = -999
while True:
    num: int = int(input("enter a number between 1-10:"))
    if num == SENTINEL:
        break
    if not 0 <= num < 10:
        continue
    numbers.append(num)
    for i in range(0, 10):
        if i in numbers:
            print("statistic",[i]," = ",numbers.count(i))
