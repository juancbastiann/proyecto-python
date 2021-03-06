# 驴Qu茅 es Python? 馃悕  
Python es un lenguaje de programaci贸n de prop贸sito general de alto nivel interpretado. Su filosof铆a de dise帽o enfatiza la legibilidad del c贸digo con el uso de una sangr铆a significativa. Sus construcciones de lenguaje y su enfoque orientado a objetos tienen como objetivo ayudar a los programadores a escribir c贸digo claro y l贸gico para proyectos de peque帽a y gran escala.  
Python es de tipado din谩mico y recolecci贸n de elementos no utilizados. Admite m煤ltiples paradigmas de programaci贸n, incluida la programaci贸n estructurada (en particular, procedimental), orientada a objetos y funcional. A menudo se describe como un lenguaje de "bater铆as incluidas" debido a su completa biblioteca est谩ndar.
# 驴Qu茅 es una variable? 馃搫
Una variable es donde se guarda (y se recupera) datos que se utilizan en un programa.
## Nombrando una variable 馃搼
```Python 
variable = 
#donde "variable" es el lugar donde se almacena una informaci贸n e "=" nos indica cual es este valor
```
## Asignando valores a una variable 馃搼
```Python 
variable = 10
variable = "Hello world" 
#donde el valor precedido del "=" es el valor asignado a nuestra variable
```
## Operadores b谩sicos 馃搼
```Python
suma : +  
resta : -  
multiplicaci贸n : *  
divisi贸n : /  
divisi贸n entera : //  
m贸dulo : %  
potenciaci贸n : **
```
### Suma 馃
```Python
#creamos dos variables para poder realizar la operaci贸n  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operaci贸n  
result = 0  
#presentamos las dos variables acompa帽adas del operador suma  
result = (a + b)  
result = 24  
#presentamos un print para demostrar que nuestra operaci贸n sea correcta  
print (result)
```
### Resta 馃
```Python
#creamos dos variables para poder realizar la operaci贸n  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operaci贸n  
result = 0  
#presentamos las dos variables acompa帽adas del operador resta  
result = (a - b)  
result = 16  
#presentamos un print para demostrar que nuestra operaci贸n sea correcta  
print (result)
```
### Multiplicaci贸n 馃
```Python
#creamos dos variables para poder realizar la operaci贸n  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operaci贸n  
result = 0  
#presentamos las dos variables acompa帽adas del operador de multiplicaci贸n  
result = (a * b)  
result = 80    
#presentamos un print para demostrar que nuestra operaci贸n sea correcta  
print (result)
```
### Divisi贸n 馃
```Python
#creamos dos variables para poder realizar la operaci贸n  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operaci贸n  
result = 0  
#presentamos las dos variables acompa帽adas del operador de divisi贸n  
result = (a / b)  
result = 5  
#presentamos un print para demostrar que nuestra operaci贸n sea correcta  
print (result)
```
### M贸dulo 馃
```Python
#creamos dos variables para poder realizar la operaci贸n  
a = 20  
b = 3  
#creamos una variable donde almacenaremos nuestra operaci贸n  
result = 0  
#presentamos las dos variables acompa帽adas del operador de m贸dulo  
result = (a % b)  
result = 20  
#presentamos un print para demostrar que nuestra operaci贸n sea correcta  
print (result)
```
### Potencia 馃
```Python
#creamos dos variables para poder realizar la operaci贸n  
a = 20  
b = 4  
#creamos una variable donde almacenaremos nuestra operaci贸n  
result = 0  
#presentamos las dos variables acompa帽adas del operador de potencia  
result = (a ** b)  
result = 160000  
#presentamos un print para demostrar que nuestra operaci贸n sea correcta  
print (result)
```
# Tipos de datos en Python 馃搫
## Integer 馃搼
Los n煤meros enteros son aquellos que no contienen decimales, pueden ser positivos o negativos adem谩s del cero. En Python, adem谩s de otros lenguajes de programaci贸n, se les conoce como de tipo int (interger, entero) o tipo long (de largo). La diferencia entre ambos es que el long permite almacenar n煤meros m谩s grandes, por lo que tambi茅n ocupa m谩s espacio en un programa, as铆 que es recomendable usarlo s贸lo en caso de ser necesario.

ejemplo:  
```Python
x = 10  
y = 1000  
z = - 10
```
## Float 馃搼
Este tipo de dato se representa en lenguaje de programaci贸n como float (flotante). Puede, al igual que el entero, ser positivo o negativo, conteniendo uno o m谩s decimales.

ejemplo:  
```Python
x = 1.10  
y = 10.0  
z = -40.45
```

La variable float tambi茅n acepta n煤meros en notaci贸n cient铆fica, en los cuales se coloca una 芦e禄 para indicar el valor de la potencia base 10.

```Python
x = 30e2  
y = 45e1  
z = -50e4
```
## String 馃搼
Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.

ejemplo:  
```Python
print("Hello world")
```
## Casting en Python 馃搼
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.

Existen dos:  
Conversi贸n impl铆cita: Es realizada autom谩ticamente por Python. Sucede cuando realizamos ciertas operaci贸nes con dos tipos distintos.

```Python
a = 1   # <class 'int'>  
b = 2.3 # <class 'float'>  
a = a + b  
print(a)       # 3.3  
print(type(a)) # <class 'float'>
```

Conversi贸n expl铆cita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().

```Python
a = 3.5  
print(type(a)) # <class 'float'>  
a = str(a)  
print(type(a)) # <class 'str'>
```
## List 馃搼
Las listas (o 鈥楲ist鈥?) en Python son un tipo de estructuras de datos muy flexible que guardan de forma ordenada un conjunto de datos que no tiene porque ser del mismo tipo. En otros lenguajes de programaci贸n una lista equivaldr铆a a un array, aunque Python no exige que los elementos de la lista tenga que ser del mismo tipo (鈥榠nt鈥?, 鈥榝loat鈥?, 鈥榗hr鈥?, 鈥榮tr鈥?, 鈥榖ool鈥?, 鈥榦bject鈥?).

ejemplo:  
```Python
lista = [1, 3.1416, 'j']  
print(lista)

[salida]: [1, 3.1416, j]
```
## Tuple 馃搼
Las tuplas se utilizan para almacenar varios elementos en una sola variable.  
Tuple es uno de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos, los otros 3 son Lista, Conjunto y Diccionario, todos con diferentes calidades y usos.  
Una tupla es una colecci贸n ordenada e inmutable.  
Las tuplas se escriben con corchetes.

ejemplo:  
```Python
thistuple = ("apple", "banana", "cherry")  
print(thistuple)

[salida]: [apple, banana, cherry]
```
## Dictionary 馃搼
Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.  
Un diccionario es una colecci贸n ordenada*, modificable y que no admite duplicados.

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
# Tomando decisiones 馃搫
## Sentencia if 馃搼
Python admite las condiciones l贸gicas habituales de las matem谩ticas:

Es igual a: a == b  
No es igual a: a != b  
Menos que: a < b  
Menor o igual que: a <= b  
Mayor que: a > b  
Mayor o igual que: a >= b  

Estas condiciones se pueden usar de varias maneras, m谩s com煤nmente en "sentencias if" y bucles.  
Una "sentencia if" se escribe utilizando la palabra clave if.

ejemplo:  
```Python
a = 33  
b = 200  
si b > a:  
    print("b es mayor que a")
```

La palabra clave elif es la forma de Python de decir "si las condiciones anteriores no fueron ciertas, intente esta condici贸n".

ejemplo: 
```Python 
a = 33  
b = 33  
si b > a:  
  print("b es mayor que a")  
elif a == b:  
  print("a y b son iguales")
  ```
## Ciclo For 馃搼
Un bucle for se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).  
Esto se parece menos a la palabra clave for en otros lenguajes de programaci贸n y funciona m谩s como un m茅todo iterador como se encuentra en otros lenguajes de programaci贸n orientados a objetos.  
Con el bucle for podemos ejecutar un conjunto de sentencias, una vez por cada elemento de una lista, tupla, conjunto, etc.

ejemplo:  
```Python
frutas = ["manzanas", "bananas", "cerezas"]  
for x in frutas:  
  print(x)
  ```
## Ciclo While 馃搼
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condici贸n sea verdadera.

ejemplo:  
```Python
i = 1  
while i < 6:  
  print(i)  
  i += 1
  ```
## Break 馃搼
Con la instrucci贸n break podemos detener el bucle incluso si la condici贸n while es verdadera:

ejemplo:  
```Python
i = 1  
while i < 6:  
  print(i)  
  if i == 3:  
    break  
  i += 1  
```
## Continue 馃搼
Con la instrucci贸n continue podemos detener la iteraci贸n actual y continuar con la siguiente:

ejemplo:  
```Python
i = 0  
while i < 6:  
  i += 1  
  if i == 3:  
    continue  
  print(i)  
```