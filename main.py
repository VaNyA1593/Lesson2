import random

elements = "1234567890-=/*+qwertyuiopasdfghjklzxcvbnm,./<>?;[]QWERTYUIOPASDFGHJKLZXCVBNM"

len = int(input("Длина пароля..."))

password = ""

for i in range (len):
    password += random.choice(elements)

print(password)
