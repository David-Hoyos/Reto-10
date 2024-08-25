try:
    cantidad = int(input("Por favor ingrese cuantos elementos va a tener la lista: "))
    vector: list = []

    for i in range(cantidad):
        x = int(input("Por favor ingrese un numero entero: "))
        vector.append(x)

    i = 0
    for i in range(cantidad):
        if vector[i] == 0:
            vector.append(vector[i])
            vector.remove(0)
        else:
            i += 1
    print(vector)
except ValueError:
    print("Por favor ingrese un valor valido")