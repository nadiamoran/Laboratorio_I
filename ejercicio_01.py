'''
#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

'''
acumulador_jabon=0
flag_mayor_cantidad=True
fabricante_mas_caro=""
cantidad_mas_caro=0
barbijo_mas_caro=0
mayor_cantidad=0
flag_barbijo=True

for productos in range(2):
    tipo = input("Ingrese el tipo de producto: 'barbijo', 'jabon' 'alcohol ': \n")

    while (tipo!="barbijo" and tipo!="jabon" and tipo!= "alcohol"):
        tipo = input("Error. Reingrese tipo valido: ")

    precio = input("Ingrese precio entre 100 y 300: \n")
    precio = float(precio)
    while (precio<100 and precio >300):
        precio = input("Error. Reigrese precio valido: ")
        precio = float(precio)

    cantidad = input("Ingrese cantidad entre 1 y 1000: \n")
    cantidad = int(cantidad)
    while (cantidad<1 and cantidad > 1000):
        cantidad = input("Error. Reigrese precio valido: ")
        cantidad = int(cantidad)

    marca = input("Ingrese marca: \n")
    fabricante = input("Ingrese fabricante: \n")

    if(tipo =="barbijo"):
                
        if (barbijo_mas_caro>precio):
            barbijo_mas_caro=precio
            cantidad_mas_caro=cantidad
            fabricante_mas_caro=fabricante

        elif (flag_barbijo==True):
                barbijo_mas_caro=precio
                cantidad_mas_caro=cantidad
                fabricante_mas_caro=fabricante
                flag_barbijo = False
    
        if (mayor_cantidad>cantidad):
            mayor_cantidad=cantidad
            fabricante_mayor_cantidad=fabricante

        elif (flag_mayor_cantidad==True):
            mayor_cantidad=cantidad
            fabricante_mayor_cantidad=fabricante
            flag_mayor_cantidad = False


    if tipo=="jabon":
        acumulador_jabon += cantidad
        

print("Del mas caro de los barbijos las unidades y fabricante son: ", cantidad_mas_caro, "y", fabricante_mas_caro)
print("La cantidad de jabon es de:", acumulador_jabon)
print("El fabricante con mas cantidad es de: ", fabricante_mayor_cantidad)
