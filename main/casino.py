import random
import time

ishod = ['МЕНЬШЕ', 'РАВНО', 'БОЛЬШЕ']

print("В данное приложение поможет вам обмануть казино. Подождите пока оно загрузится.")
time.sleep(random.randint(5,10))
userID = input("Введите ваш Telegram ID, чтобы его получить перейдите в бота: @getmyid_bot:  ")
print("Ваш ID:", userID)

print("Отлично. Выбирайте игру ЧИСЛА. Теперь пишите ИСХОД")
chance = input()
if chance == "ИСХОД":
    random_ishod = random.choice(ishod)
    print(random_ishod)
    print("Введи СТОП или ИСХОД")

