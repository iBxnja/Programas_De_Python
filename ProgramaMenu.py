nombre = str(input('-------------------------------------------\nBienvenido. Por favor ingresa tu nombre...\n-------------------------------------------\nMi nombre es: '))
print('\n========================================')
print('Bienvenido' , nombre )
print('========================================\n')
lProducto = ["asado", "pastas", "ensalada"]
print('========================================')
print("Esta es la lista de comidas\n" , lProducto)
print('========================================')
numero = input('\nSi deseas agregar una nueva comida a la carta coloca "agregar". \nSi deseas finalizar el programa coloca "cerrar".\n')
if(numero == "agregar"):
    contador = 100
    while(contador == 100):
        print('\n=====================================================================================================================')
        nuevaComida = input('Agrega una nueva comida al menu... O coloca "cerrar" para finalizar la edición del menu: \n=====================================================================================================================\n\n')
        if(nuevaComida == "cerrar"):
            contador+1    
            print('=======================')
            print("Menu finalizado.")   
            print('=======================\n')
            break
        else:
            lProducto.append(nuevaComida)
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
            print("\n¡Perfecto!, nueva comida agregada.")
            print("El menu ahora es asi: " , lProducto , "\n")
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
            continue
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Esta es su nueva carta de comida" , lProducto)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print('\n============================================')
    print("\n\nPrograma finalizado. ¡Hasta luego!.\n\n")
    print('\n============================================')