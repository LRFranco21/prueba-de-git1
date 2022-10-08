from datetime import date
"""
Esta tarea esta diseñada para poner a prueba los conocimientos
adquiridos en la primera clase de la Certificacion de Python
Son 6 ejercicios, resuelvalos en un solo archivo
:: Debera separarlos por comentarios e impresiones ::
>Puede reutilizar los valores de las variables< :D
"""

#Ejercicio 1
"""
Obtenga el valor resultante de la siguiente ecuacion
((a + b) - c) / 2
"""
# recibiendo datos para los tres valores 
a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))
c = int(input("Ingrese un valor para c: "))

#imprimiendo el resultado en la variable d
d = ((a + b) - c ) / 2# siempre ponemos segur el orden de operacion haciendo primero la suma 
print("El valor resultante es: ", d)


#Ejercicio 2
"""
Ordene la siguiente formula aplicando parentesis siguiendo el orden de
prioridad de los signos y muestre el valor de la respuesta
a * b - c / 1 + a^2 // 2 
"""

d = (a * b) - (c / 1) + (a**2 // 2) 
print("El valor resultante es: ", d)

#Ejercicio 3
"""
Elabora un programa que muestre los resultados de aplicar las siguientes
operaciones
n / 2
n // 2
n % 2
Observe las diferencias
"""
n=int(input("Ingrese un valor para n: "))# se recibe el dato o valor para la variable n 

print(n,"/ 2 = ", n/2, "\n", # con la coma se separa la operacion del texto y de las demas operaciones para la variable n
      n," // 2 = ", n//2, "\n",   
      n," % 2 = ", n%2, "\n")    

#Ejercicio 4
"""
Obtenga el valor resultante El cuadrado de la suma de 2 numeros positivos
(a + b)^2 = a^2 + 2ab + b^2
"""
d = a**2 + 2*a*b + b**2 #los dos "**" se utilizan para elevar un valor a una potencia, ejemplo los valores estan al cuadrado
print("(",a,"^ 2 +",b,"^ 2 ) =", d)#mostrando el valor de a,b,c siendo elevados al cuadrado y seguido de una "," para imprimir valor resultante ",d"


#Ejercicio 5
"""
Escriba un programa que reciba el nombre y DUI de un persona, luego que
solicite la horas trabajadas y que mueste el salario de la persona
Teniendo en cuenta que cada hora trabajada se paga a $2.25
"""
name_user = str(input("Ingrese su nombre porfavor: "))# el nombre de usuario sera de tipo caracter igual que el DUI
dui_user = str(input("Ingrese su numero de DUI porfavor: "))
hours = int(input("Cuantas horas ha trabajado?: "))# las horas trabajadas seran tomadas de tipo entero
#
salary = hours*2.25# se hace la operacion de la multiplicacion de cantidad de horas por $2.25
print("{}, con numero de DUI: {}, recibira un salario de: ${}".format(name_user, dui_user, salary))


#Ejercicio 6
"""
Escriba un programa que reciba el nombre y el año de
nacimiento de la persona, l programa debe mostrar al
usuario cuantos dias ha vivido desde su nacimiento
"""
data = input("Ingrese su fecha de nacimiento de la siguiente forma ---> dia, mes, year ---> 31, 12, 1999: ")
data = data.replace(',', '').split(' ')
date_birth = date(int(data[-1]), int(data[1]), int(data[0]))
days_alive = date.today() - date_birth

print("Tu haz vivido esta cantidad de dias: {}".format(days_alive.days))









