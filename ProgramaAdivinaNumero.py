import random

numero_random = random.randint(1, 100)
print(numero_random)

while True:
    numero_persona = int(input('¿Qué número crees que es? '))

    if numero_persona == numero_random:
        print('¡FELICIDADES!. Ese es el número correcto, bien hecho.')
        break
    elif numero_persona < numero_random:
        print("El número que enviaste es Menor al número secreto.")
    else:
        print("El número que enviaste es Mayor al número secreto.")
