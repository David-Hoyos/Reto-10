try: #Se usa try y except por si el usuario llega a poner un valor que no es valido. 
    cantidad = int(input("Por favor ingrese la cantidad de elementos que va a tener el arreglo de reales: "))#Se le pide al usuario cuantos elementos va a tener la lista.
    i = 0
    vector: list = []
    suma: float = 0
    while i < cantidad:#A traves de un ciclo while se le piden al usuario los elementos que va a tener el vector y a traves del metodo append se insertan dentro del vector.
        elemento = float(input("Por favor ingrese uno por uno los elementos del arreglo:"))
        vector.append(elemento)
        suma += elemento
        i += 1
    promedio = suma/cantidad
    print (f"el vector  es {vector}")
    print(f"El promedio es {promedio}")       
except ValueError: 
    print("Por favor ingrese un valor valido")