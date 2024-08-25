# Reto-10
## Punto 1
Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
try: #Se usa try y except por si el usuario llega a poner un valor que no es valido. 
    cantidad = int(input("Por favor ingrese la cantidad de elementos que va a tener el arreglo de reales: "))#Se le pide al usuario cuantos elementos va a tener la lista.
    i = 0
    vector: list = []
    suma: float = 0
    while i < cantidad:#A traves de un ciclo while se le piden al usuario los elementos que va a tener el vector y a traves del metodo append se insertan dentro del vector.
        elemento = float(input("Por favor ingrese uno por uno los elementos del arreglo:"))
        vector.append(elemento)
        suma += elemento # Se suman todos los elementos
        i += 1
    promedio = suma/cantidad #La suma se divide entre la cantidad de elementos. 
    print (f"el vector  es {vector}")
    print(f"El promedio es {promedio}")#Se imprime el resultado       
except ValueError: 
    print("Por favor ingrese un valor valido")
```

## Punto 2 
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de dos arreglos de numeros enteros(reales) de igual tamaño. 
```python
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
```
 ## Punto 3
 Hacer un algoritmo que deje al final de un arreglo de numeros todos los ceros que aparezcan en dicho arreglo. 
 ```python
try:#Se usa try por si el usuario llega a ingresar un valor que no es valido. 
    cantidad = int(input("Por favor ingrese cuantos elementos va a tener la lista: "))#Se le pide al usuario cuantos elementos va a tener la lista
    vector: list = []

    for i in range(cantidad):#A traves de un ciclo for se le piden al usuario los elementos que va a tener la lista.
        x = int(input("Por favor ingrese un numero entero: "))
        vector.append(x)#Se usa el metodo append para ingresar los valores dentro de la lista

    i = 0
    for i in range(cantidad):#Se verifica elemento por elemento si es igual a 0.
        if vector[i] == 0:
            vector.append(vector[i])#Si un elemento es igual a 0, se agrega un 0 al final de la lista y se borra la primera aparicion de 0 en la lista.
            vector.remove(0)
        else:
            i += 1
    print(vector)#Se imprime el resultado
except ValueError:
    print("Por favor ingrese un valor valido")
 ```
