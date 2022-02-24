"# proyecto-python" 
# Qué es Python?
Python es un lenguaje de programación de propósito general de alto nivel interpretado. Su filosofía de diseño enfatiza la legibilidad del código con el uso de una sangría significativa. Sus construcciones de lenguaje y su enfoque orientado a objetos tienen como objetivo ayudar a los programadores a escribir código claro y lógico para proyectos de pequeña y gran escala./n
Python es de tipado dinámico y recolección de elementos no utilizados. Admite múltiples paradigmas de programación, incluida la programación estructurada (en particular, procedimental), orientada a objetos y funcional. A menudo se describe como un lenguaje de "baterías incluidas" debido a su completa biblioteca estándar.
# Qué es una variable?
Una variable es donde se guarda (y se recupera) datos que se utilizan en un programa.
## Nombrando una variable
variable
## Asignando valores a una variable
variable = 10
## Operadores básicos
### Suma
"+"	Realiza Adición entre los operandos 12 + 8 = 20
### Resta
"-"	Realiza Substracción entre los operandos 12 - 10 = 2
### Multiplicación
"*" Realiza Multiplicación entre los operandos 12 * 4 = 48
### División
"/"	Realiza División entre los operandos 12 / 2 = 6
### Módulo
"%"	Realiza un módulo entre los operandos 16 % 3 = 1
### Potencia
"**"	Realiza la potencia de los operandos 12 ** 3 = 1728
# Tipos de datos en Python

## Integer
Los números enteros son aquellos que no contienen decimales, pueden ser positivos o negativos además del cero. En Python, además de otros lenguajes de programación, se les conoce como de tipo int (interger, entero) o tipo long (de largo). La diferencia entre ambos es que el long permite almacenar números más grandes, por lo que también ocupa más espacio en un programa, así que es recomendable usarlo sólo en caso de ser necesario./n/n

ejemplo:/n
x = 10/n
y = 1000/n
z = - 10
## Float
Este tipo de dato se representa en lenguaje de programación como float (flotante). Puede, al igual que el entero, ser positivo o negativo, conteniendo uno o más decimales./n/n

ejemplo:/n
x = 1.10/n
y = 10.0/n
z = -40.45/n/n

La variable float también acepta números en notación científica, en los cuales se coloca una «e» para indicar el valor de la potencia base 10./n

x = 30e2/n
y = 45e1/n
z = -50e4/n
## String
Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles./n/n

ejemplo:/n
print("Hello world")
## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro./n/n

Existen dos:/n
Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos./n/n

a = 1   # <class 'int'>/n
b = 2.3 # <class 'float'>/n
a = a + b/n
print(a)       # 3.3/n
print(type(a)) # <class 'float'>/n/n

Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str()./n/n

a = 3.5/n
print(type(a)) # <class 'float'>/n
a = str(a)/n
print(type(a)) # <class 'str'>/n
## List
Las listas (o ‘List’) en Python son un tipo de estructuras de datos muy flexible que guardan de forma ordenada un conjunto de datos que no tiene porque ser del mismo tipo. En otros lenguajes de programación una lista equivaldría a un array, aunque Python no exige que los elementos de la lista tenga que ser del mismo tipo (‘int’, ‘float’, ‘chr’, ‘str’, ‘bool’, ‘object’)./n/n

ejemplo:/n
lista = [1, 3.1416, 'j']
## Tuple
Las tuplas se utilizan para almacenar varios elementos en una sola variable. Tuple es uno de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos, los otros 3 son Lista, Conjunto y Diccionario, todos con diferentes calidades y usos. Una tupla es una colección ordenada e inmutable. Las tuplas se escriben con corchetes./n/n

ejemplo:/n
thistuple = ("apple", "banana", "cherry")/n
print(thistuple)
## Dictionary
Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor./n
Un diccionario es una colección ordenada*, modificable y que no admite duplicados./n/n

ejemplo:/n
thisdict = {/n
  "brand": "Ford",/n
  "model": "Mustang",/n
  "year": 1964/n
}/n/n

print(thisdict)
# Tomando decisiones

## Sentencia if
Python admite las condiciones lógicas habituales de las matemáticas:/n/n

Es igual a: a == b
No es igual a: a != b
Menos que: a < b
Menor o igual que: a <= b
Mayor que: a > b
Mayor o igual que: a >= b

Estas condiciones se pueden usar de varias maneras, más comúnmente en "sentencias if" y bucles.
Una "sentencia if" se escribe utilizando la palabra clave if.

ejemplo:
a = 33
b = 200
si b > a:
    print("b es mayor que a")

La palabra clave elif es la forma de Python de decir "si las condiciones anteriores no fueron ciertas, intente esta condición".

ejemplo:

a = 33
b = 33
si b > a:
   print("b es mayor que a")
elif a == b:
   imprimir("a y b son iguales")
## Ciclo For
Un bucle for se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).
Esto se parece menos a la palabra clave for en otros lenguajes de programación y funciona más como un método iterador como se encuentra en otros lenguajes de programación orientados a objetos.
Con el bucle for podemos ejecutar un conjunto de sentencias, una vez por cada elemento de una lista, tupla, conjunto, etc.

ejemplo:
frutas = ["manzanas", "bananas", "cerezas"]
for x in frutas:
  print(x)
## Ciclo While
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.

ejemplo:
i = 1
while i < 6:
  print(i)
  i += 1
## Break
Con la instrucción break podemos detener el bucle incluso si la condición while es verdadera:

ejemplo:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
## Continue
Con la instrucción continue podemos detener la iteración actual y continuar con la siguiente:

ejemplo:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)