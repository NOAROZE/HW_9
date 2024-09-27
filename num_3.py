numbers: list[int] = []
SENTINEL: int = -999
calculation: int = 0
new_numbers: list[int] = []
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
while calculation < 10:
    new_numbers.append(numbers.count(calculation))
    calculation += 1
print(new_numbers)
# האם תוכל לפתור עבור טווח של 0-100?
# כן אבל אם הקלטים היו גם בין 0-100 גם עכשיו היה אפשר אבל מ -10 הכל היה ריק
