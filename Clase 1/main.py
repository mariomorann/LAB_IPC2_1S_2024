# DECLARACIÓN DE VARIABLES

cadena = "hola" + ' mundo'

print(cadena)
x = 4
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) # modulo = residuo de la division ( x/y )

# Tipos de datos numéricos
entero = 1
decimal = 5.2
# n = complex(i , re)

print("--------")
# fuciones de python
x = -5
y = 5.66 # 6
print(abs(x))
print(float(x))
print(int(y))
print(pow(3, 2)) # 3 * 3
print(9**(1/2))
print("--------")

# Cadena de texto
text = " fdasffadsf "
text2 = ' HOLA MUNDO '
text3 = """ Hola 

Mundo  """
text4 = ''' Hola mundo 
:') '''
print(text2)
print(text3)
print(text4)

num = 2
num2 = '200'
variable = str(num) + text2
print(variable)
print(int(num2) + 100)

print("--------")
# Tipo de dato booleano
expresion = True
num = 3
if expresion:
    print("es verdadero")


if not expresion:
    print("es falso")
else:
    print("es vedadero")

expresion2 = num == 2
if expresion and expresion2:
    print("verdadero")
else:
    print("falso")


expresion2 = num == 2
if (expresion2) or (not expresion):
    print("verdadero")
else:
    print("falso")

num = 3
if (num == 1):
    print("hola")
elif (num == 0):
    print("adios")
else:
    print("hasta nunca")

estaFeliz = False
estado = "Esta feliz" if estaFeliz else "Esta triste"
print(estado)


print("-----------")
lista1 = [1, 2, 3, 4, 5]
print(lista1)
lista1.append(6)
print(lista1)

print("-----------")
# Ciclos
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end=' ')
    print("")

cadena = "hola mundo"
for caracter in cadena:
    print(caracter)


print("--------")
# while
num = 100
while num <= 106:
    if num == 104:
        num += 1
        break
    print(num)
    num += 1

print("---------")
# Funcion
def funcion1():
    print("hola mundo")
funcion1()

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

resutado = suma(2, 3)
print(resutado)