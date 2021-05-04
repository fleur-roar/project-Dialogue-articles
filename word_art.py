import pyfiglet
name = input('Введите, пожалуйста, слово, которое вы бы хотели нарисовать: ')
result = pyfiglet.figlet_format(name) # рисуем
print(result)
