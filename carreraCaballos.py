import random
import time

c1 = 1
c2 = 2
c3 = 3

contadorC1 = 0
contadorC2 = 0
contadorC3 = 0
contador = 19
g1 = []
g2 = []
g3 = []


while contadorC1 != contador or contadorC2 != contador or contadorC3 != contador:
    numero_random = random.randint(1, 3)
    print("----------------------------------------------------------")
    print(f"- {' '.join(g1)} Caballo1")
    print("- -")
    print(f"- {' '.join(g2)} Caballo2")
    print("- -")
    print(f"- {' '.join(g3)} Caballo3")
    print("----------------------------------------------------------")
    if(contadorC1 == contador):
            print("Ganador el caballo numero 1")
    if(contadorC2 == contador):
            print("Ganador el caballo numero 2")
    if(contadorC3 == contador):
            print("Ganador el caballo numero 3")
    if contadorC1 == contador or contadorC2 == contador or contadorC3 == contador:
        break
    elif numero_random == c1:
        contadorC1 += 1
        g1.append(" *")
    elif numero_random == c2:
        contadorC2 += 1
        g2.append(" *")
    elif numero_random == c3:
        contadorC3 += 1
        g3.append(" *")

    time.sleep(0.5)





# print("fin:", contadorC1, contadorC2, contadorC3)
