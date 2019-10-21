#Inventario
import os
os.system("cls")

cantidad = int(input("¿Cuántos productos va a registrar?:"))
lista = []

for i in range(cantidad):
    num = str(i + 1)
    nombre = input("Ingrese el nombre del producto " + num + ":")
    precio = float(input("Ingrese el precio del producto " + num + ":"))
    categoria = input("Ingrese la categoría del producto " + num + ":")

    producto = [nombre, precio, categoria]
    lista.append(producto)

#Cantidad de productos en el catálogo
print(len(lista))  # print(cantidad)

#Precio  promedio del catálogo
suma =  0
for producto in lista:
    suma = suma + producto[1]
promedio = suma / cantidad
print("El precio promedio es:", promedio)

#Cantidad de productos que superan el precio promedio del catálogo
contador = 0
for producto in lista:
    if producto[1] > promedio:
        contador += 1
print("Cantidad de productos que superan el precio promedio:", contador)

#Producto más caro
mas_caro = lista[0]

for producto in lista:
    if producto[1] > mas_caro[1]:
        mas_caro = producto
print("El producto más caro es:", mas_caro)

#Producto más barato
mas_barato = lista[0]

for producto in lista:
    if producto[1] < mas_barato[1]:
        mas_caro = producto
print("El producto más barato es:", mas_barato)

#Categoría con más productos
categorias = []
c = []  #Contador de categorías

for producto in lista:
    categoria = producto[2]
    if categorias.count(categoria) == 0:
        categorias.append(categoria)
        c.append(0)
    else:
        pos = categorias.index(categoria)
        c[pos] += 1
num_mas_alto = max(c) 
pos_num_mas_alto = c.index(num_mas_alto)
categoria_con_mas_productos = categorias[pos_num_mas_alto]
print("Categoría con más productos:", categoria_con_mas_productos)