try:#Usamos el bloque try para capturar cualquier error de tipo ValueError que pueda ocurrir en el caso de que el usuario no ingrese un valor numerico. 
    cantidad = int(input("Por favor ingrese la cantidad de elementos que van a tener los vectores: "))#Le pedimos al usuario la cantidad de elementos que van a tener los vectores
    vector1 = []
    vector2 = []
    
    for i in range(cantidad): #A traves de un ciclo for le pedimos al usuario todos los elementos que van a tener los vectores
        x = int(input("Por favor ingrese un elemento del primer vector: "))
        y = int(input("Por favor ingresa un elemento del segundo vector: "))
        vector1.append(x)
        vector2.append(y)
    
    productoPunto = 0 
    for i in range(cantidad): #A traves de un ciclo for sumamos los productos de los componentes correspondientes de los dos vectores.
        producto = vector1[i] * vector2[i]
        productoPunto += producto

    print(f"El producto punto de dos vectores es {productoPunto}")#Se imprime el resultado.

except ValueError:
    print("Por favor ingrese valores validos. ")
