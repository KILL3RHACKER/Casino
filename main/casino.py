import random
import time

ishod = ['МЕНЬШЕ', 'РАВНО', 'БОЛЬШЕ']

A = 1

print("Version: 2.0.3rel \n Сделал @OxWorldik1337 \n Данное приложение поможет вам обмануть казино. Подождите пока оно загрузится.")

time.sleep(random.randint(5,10))

userID = input("Введите ваш Telegram ID, чтобы его получить перейдите в бота: @getmyid_bot:  ")
print("Ваш ID:", userID, "Переходим к сути")

print("Отлично. Выбирайте игру ЧИСЛА. Теперь пишите ИСХОД")


while A == 1:
    random_ishod = random.choice(ishod)
    chance = input()
    print(  )
    if chance == "ИСХОД":
        print(random_ishod, "\n\nВы можете еще раз написать ИСХОД или СТОП для выхода из приложения")
    elif chance == "СТОП":
        A = 0
        exit

