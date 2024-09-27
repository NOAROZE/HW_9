numbers: list[int] = []
SENTINEL: int = -999
while True:
    num: int = int(input("enter a number between 1-10:"))
    if num == SENTINEL:
        break
    if not 1 < num < 10:
        continue
    numbers.append(num)
    for i in range(1, 10):
        if i in numbers:
            print(i," = ",numbers.count(i))
