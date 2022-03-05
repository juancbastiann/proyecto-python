# ¿Qué es Python? 🐍  
Python es un lenguaje de programación de propósito general de alto nivel interpretado. Su filosofía de diseño enfatiza la legibilidad del código con el uso de una sangría significativa. Sus construcciones de lenguaje y su enfoque orientado a objetos tienen como objetivo ayudar a los programadores a escribir código claro y lógico para proyectos de pequeña y gran escala.  
Python es de tipado dinámico y recolección de elementos no utilizados. Admite múltiples paradigmas de programación, incluida la programación estructurada (en particular, procedimental), orientada a objetos y funcional. A menudo se describe como un lenguaje de "baterías incluidas" debido a su completa biblioteca estándar.
# ¿Qué es una variable? 📄
Una variable es donde se guarda (y se recupera) datos que se utilizan en un programa.
## Nombrando una variable 📑
```Python 
variable = 
#donde "variable" es el lugar donde se almacena una información e "=" nos indica cual es este valor
```
## Asignando valores a una variable 📑
```Python 
variable = 10
variable = "Hello world" 
#donde el valor precedido del "=" es el valor asignado a nuestra variable
```
## Operadores básicos 📑
```Python
suma : +  
resta : -  
multiplicación : *  
división : /  
división entera : //  
módulo : %  
potenciación : **
```
### Suma 🤖
```Python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador suma  
result = (a + b)  
result = 24  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Resta 🤖
```Python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador resta  
result = (a - b)  
result = 16  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Multiplicación 🤖
```Python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de multiplicación  
result = (a * b)  
result = 80    
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### División 🤖
```Python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de división  
result = (a / b)  
result = 5  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Módulo 🤖
```Python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 3  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de módulo  
result = (a % b)  
result = 20  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Potencia 🤖
```Python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de potencia  
result = (a ** b)  
result = 160000  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
# Tipos de datos en Python 📄
## Integer 📑
Los números enteros son aquellos que no contienen decimales, pueden ser positivos o negativos además del cero. En Python, además de otros lenguajes de programación, se les conoce como de tipo int (interger, entero) o tipo long (de largo). La diferencia entre ambos es que el long permite almacenar números más grandes, por lo que también ocupa más espacio en un programa, así que es recomendable usarlo sólo en caso de ser necesario.

ejemplo:  
```Python
x = 10  
y = 1000  
z = - 10
```
## Float 📑
Este tipo de dato se representa en lenguaje de programación como float (flotante). Puede, al igual que el entero, ser positivo o negativo, conteniendo uno o más decimales.

ejemplo:  
```Python
x = 1.10  
y = 10.0  
z = -40.45
```

La variable float también acepta números en notación científica, en los cuales se coloca una «e» para indicar el valor de la potencia base 10.

```Python
x = 30e2  
y = 45e1  
z = -50e4
```
## String 📑
Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.

ejemplo:  
```Python
print("Hello world")
```
## Casting en Python 📑
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.

Existen dos:  
Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciónes con dos tipos distintos.

```Python
a = 1   # <class 'int'>  
b = 2.3 # <class 'float'>  
a = a + b  
print(a)       # 3.3  
print(type(a)) # <class 'float'>
```

Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().

```Python
a = 3.5  
print(type(a)) # <class 'float'>  
a = str(a)  
print(type(a)) # <class 'str'>
```
## List 📑
Las listas (o ‘List’) en Python son un tipo de estructuras de datos muy flexible que guardan de forma ordenada un conjunto de datos que no tiene porque ser del mismo tipo. En otros lenguajes de programación una lista equivaldría a un array, aunque Python no exige que los elementos de la lista tenga que ser del mismo tipo (‘int’, ‘float’, ‘chr’, ‘str’, ‘bool’, ‘object’).

ejemplo:  
```Python
lista = [1, 3.1416, 'j']  
print(lista)

[salida]: [1, 3.1416, j]
```
## Tuple 📑
Las tuplas se utilizan para almacenar varios elementos en una sola variable.  
Tuple es uno de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos, los otros 3 son Lista, Conjunto y Diccionario, todos con diferentes calidades y usos.  
Una tupla es una colección ordenada e inmutable.  
Las tuplas se escriben con corchetes.

ejemplo:  
```Python
thistuple = ("apple", "banana", "cherry")  
print(thistuple)

[salida]: [apple, banana, cherry]
```
## Dictionary 📑
Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.  
Un diccionario es una colección ordenada*, modificable y que no admite duplicados.

ejemplo:  
```Python
thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}

print(thisdict)

[salida]: [Ford Mustang 1964]
```
# Tomando decisiones 📄
## Sentencia if 📑
Python admite las condiciones lógicas habituales de las matemáticas:

Es igual a: a == b  
No es igual a: a != b  
Menos que: a < b  
Menor o igual que: a <= b  
Mayor que: a > b  
Mayor o igual que: a >= b  

Estas condiciones se pueden usar de varias maneras, más comúnmente en "sentencias if" y bucles.  
Una "sentencia if" se escribe utilizando la palabra clave if.

ejemplo:  
```Python
a = 33  
b = 200  
si b > a:  
    print("b es mayor que a")
```

La palabra clave elif es la forma de Python de decir "si las condiciones anteriores no fueron ciertas, intente esta condición".

ejemplo: 
```Python 
a = 33  
b = 33  
si b > a:  
  print("b es mayor que a")  
elif a == b:  
  print("a y b son iguales")
  ```
## Ciclo For 📑
Un bucle for se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).  
Esto se parece menos a la palabra clave for en otros lenguajes de programación y funciona más como un método iterador como se encuentra en otros lenguajes de programación orientados a objetos.  
Con el bucle for podemos ejecutar un conjunto de sentencias, una vez por cada elemento de una lista, tupla, conjunto, etc.

ejemplo:  
```Python
frutas = ["manzanas", "bananas", "cerezas"]  
for x in frutas:  
  print(x)
  ```
## Ciclo While 📑
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.

ejemplo:  
```Python
i = 1  
while i < 6:  
  print(i)  
  i += 1
  ```
## Break 📑
Con la instrucción break podemos detener el bucle incluso si la condición while es verdadera:

ejemplo:  
```Python
i = 1  
while i < 6:  
  print(i)  
  if i == 3:  
    break  
  i += 1  
```
## Continue 📑
Con la instrucción continue podemos detener la iteración actual y continuar con la siguiente:

ejemplo:  
```Python
i = 0  
while i < 6:  
  i += 1  
  if i == 3:  
    continue  
  print(i)  
```