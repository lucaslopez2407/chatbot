nombre = "Lucas"
años = "2007"
edad = 18
frutas = ["frutilla" , "sandia"]
user = {"nombre" : "lucas"}
user = {"edad": 18}
print(años)
print("Hola soy:" + "lucas")
print(f"Hola soy {nombre} y tengo {edad} me gusta la {frutas}")






frutas = ["manzanas" , "peras" , "uvas"]
frutas[2] = "naranja"
frutas.sort(reverse=True)
print(frutas)
del frutas[1]
print(frutas)
#range
#un valor
numero = range(20)
# print(list(numero))
numero = range (20,40)
print(list(numero))


# 10 -> 0,1,2,3,4,5,6,7,8,9,10
def marcar_pares(n):
    for i in range (n + 1):
         if i % 2 == 0:
            print(f'{i} : par')
         else:
             print(f'{i} : impar')
    return"fin"

while True:
    a = int(input('ingrese numero entero positivo'))
    if a < 0:
        print(f'Que el valor es negativo, y necesito un valor positivo, intentalo otra vez')
    else:
        print(marcar_pares(a))
        break