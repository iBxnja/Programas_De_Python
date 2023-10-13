productos = {
    'coca cola' : 400,
    'pepsi' : 400,
    'sprite' : 400,
    'sevenup' : 400,
    'doritos' : 600,
    'hamburguesa' : 800,
    'caramelos' : 100,
    'pizza' : 1000,
    'tacos' : 750,
    'ravioles' : 1200,
    'fideos' : 900,
}
carrito = []
print("--------------------------------------------------------------------------------------")
print('Bienvenido ¿que desea llevar?. Estos son los productos disponibles... ')
print("--------------------------------------------------------------------------------------\n")
for prod in productos:
    print(prod)
print("\n--------------------------------------------------------------------------------------")
while True:
    llevar = str(input('ingrese el nombre de su producto a llevar... O escriba "fin" retirarse de la tienda, \nTambien puedes escribir "ver" para ver los productos disponibles\n\n'))
    if(llevar == "ver"):
        for prod in productos:
            print(prod)
    if llevar == "fin":
        break
    if llevar in productos:
        carrito.append(llevar)
        print('\n\n¡¡Producto agregado con exito!!')
        print('Tu carrito se forma de la siguiente manera...\n')
        print("----------------------------------------------------")
        for compra in carrito:
            print(compra)
        print("----------------------------------------------------")
        print('\n')
    if llevar not in productos and llevar != "ver":
        print('no disponible, porfavor ingrese un producto que se encuentre en la lista.')
compra_final = sum(productos[producto] for producto in carrito)
print('---------------------------------------------------------------')
print('Resumen de compra:')
for item in carrito:
    print(f'{item}: ${productos[item]}')
print('---------------------------------------------------------------')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('Total del pedido: ${}'.format(compra_final))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

