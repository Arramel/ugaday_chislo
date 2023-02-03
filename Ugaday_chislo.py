import random
print("Добро пожаловать в игру!")
nums = int(input("Введите число от 1 до 5: "))
nums2 = int(input("Введите число от 1 до 5: "))
sop = random.randint(1, 5)
if nums <= 5 and nums2 <= 5:
    print("Начинаем игру! Ваше число:", nums)
    print("Правильное число:", sop)
else:
    print("Вы ввели неверное число!")

if nums == sop:
    print("игрок 1 победил!")
elif nums2 == sop:
    print("игрок 2 победил!")
elif nums == sop and nums2 == sop:
    print("все победили!")
else:
    print("Вы проебали!")







