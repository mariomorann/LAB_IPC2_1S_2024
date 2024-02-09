# Tipos de Datos
# Hay tres tipos numéricos distintos: integers, floating point numbers y complex numbers.
x = 3.5
y = -4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) # devuelve el residuo de la division
print(-y)

print("------------")

# funciones de python
entero = -5
x = -11
y = 5.66
print(abs(entero))
print(float(x))
print(int(y))

print(pow(5, 2))
print(25**(1/2))

print("------------")
# cadenas de texto
text = "Hola Mundo"
text2 = '200'
text3 = """Hola
Mundo"""
text4 = '''Hola
Mundo'''
print(str(2) + text)
print(int(text2) + 100)

print("Nombre : %d, Apellido : %s" % (3001, "Moran")) 
print(text, text2, 50) 


# Condicionales
print("------------")
# Datos Booleanos
verdadero = True
falso = False
numero1 = 10
numero2 = 11

if (verdadero):
    print("es verdadero")

if not verdadero:
    print("1")
else:
    print("2")

if verdadero and numero1 == 11:
    print("1")
else:
    print("2")

if falso or numero1 == 11:
    print("12")
else:
    print("22")

if numero1 == 1:
    print("1")
elif numero1 == 2:
    print("2")
elif numero1 == 3:
    print("1")
else:
    print("resultado")

es_bonito = True
estado = "Es bonito" if es_bonito else "No es bonito"

print("----------")
# Ciclos
# For in
lista_ejemplo = []
lista = [1, 2, 3, 4, 5]
lst = ["hola", 2, True]
for val in lst:
    print(val)

print("")
for i in range(0, 5):
    print(lista[i])

print("")
for i in range(1, 4): 
    for j in range(1, 4): 
        print(i, j, end="")
    print("")

print("")
cadena = "hola"
for c in cadena: 
    print(c)


print("-------------")
# While
num = 100
while num < 106:
    if num == 104:
        num+=1
        continue
    elif num == 105:
        break
    else:
        print(num)
    num+=1
#print("Final de Ciclo: ",num)

print("-------")
# Funciones
def myFuncion():
    print("Hola Mundo")
myFuncion()

def suma(a, b):
    return a + b
print(suma(4, 6))

# Diccionarios


