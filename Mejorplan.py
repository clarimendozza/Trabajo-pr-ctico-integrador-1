#funciones

def A(x):
    return 40*x + 200

def B(x):
    return 70*x + 50

def C(x):
    return -2*x**2 + 80*x + 100


#horas elegidas por el cliente

x = int(input("Ingrese cantidad de horas (0 a 50): "))

if x < 0 or x > 50:
    print("Valor fuera del dominio")
else:

    a = A(x)
    b = B(x)
    c = C(x)

    print("\nCostos:")
    print("A(x) =", a)
    print("B(x) =", b)
    print("C(x) =", c)

   #plan más apropiado
    
    menor = a
    plan = "A"

    if b < menor:
        menor = b
        plan = "B"

    if c < menor:
        menor = c
        plan = "C"

    print("\nMejor plan:", plan)
    print("Costo mínimo:", menor)
