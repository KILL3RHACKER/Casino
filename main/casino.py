import random
import time

ishod = ['МЕНЬШЕ', 'РАВНО', 'БОЛЬШЕ']
random_ishod = random.choice(ishod)

print("В данное приложение поможет вам обмануть казино. Подождите пока оно загрузится.")
time.sleep(random.randint(5,10))
userID = input("Введите ваш Telegram ID, чтобы его получить перейдите в бота: @getmyid_bot:  ")
print("Ваш ID:", userID, "Все верно? Для ответа напишите ДА или НЕТ")

Type = input()

if Type == "ДА":
    print("Отлично. Выбирайте игру ЧИСЛА. Теперь пишите ИСХОД")
    chance = input()
    if chance == "ИСХОД":
        print(random_ishod)
