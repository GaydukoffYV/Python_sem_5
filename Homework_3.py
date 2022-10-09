# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв"

txt = input("Введите текст через пробел:\n")
cont_txt = "абв"
lst = [i for i in txt.split() if cont_txt not in i]
print(f'Результат: {" ".join(lst)}')