# Cree un bucle For de Python.

frutas = ["manzanas", "peras", "fresas"]
for x in frutas:
    print(x)

    
#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(a, b, c):
    x = a + b + c
    return x
print(suma(1, 2, 3))


# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

x = lambda a, b, c: a + b + c
print(x(1, 2, 3))


# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for x in lista_nombre:
    if x == nombre:
        print('sì')
    else:
        print('no')
