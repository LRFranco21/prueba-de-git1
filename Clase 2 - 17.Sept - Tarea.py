"""
Tarea practica Clase #2
"""

#Ejercicio 1
"""
Utilizando el str de multiple linea, asigne un texto de 3 lineas
y luego utilice el metodo correspondiente para que muestre
cuantos caracteres tiene el texto
"""

text_3_lines = """Este es una multi-line string,
Es muy util para a la hora de codificar en python,
recuerda siempre poner triple comillas al inicio y final."""
print("Esta es la cantidad de caracteres que contiene el texto multi-line string de 3 lineas: {}".format(len(text_3_lines)), "\n\n")

#Ejercicio 2
"""
Investigue mas metodos que se puedan aplicar a las cadenas
de texto y aplique por lo menos 5 a la siguiente str
Puede ayudarte:
https://www.w3schools.com/python/python_strings_methods.asp
"""
txt = "Soy un texto y puedes hacer muchas cosas conmigo"
method_1 = txt.isupper()
method_2 = txt.split(' ')
method_3 = txt.title()
method_4 = txt.index('y')
method_5 = txt.capitalize()
#--------------------------------------------------------------------------------------------
#                 AYUDA PARA LOS SIGUIENTES EJERCICIOS
#--------------------------------------------------------------------------------------------
"""
Para hacer un recorte en un texto hacemos txt[indice_inicial : indice_final]
Para hacer "saltos" en la impresion de los indices del str hacemos
txt[indice_inicial : indice_final : No_saltos]
Puede probar el siguiente ejemplo
"""
# para poder acceder a la ayuda debes hacer algo ;-)
""" 
print("\n\n :: Esta es una ayuda ::")

txt = "Aprobare la certificaion IT Specialist de Python"
i=0
for x in txt:
    print(i, " = ", x)
    i+=1

print(len(txt))
print(txt[::]) #Muestra toda la cadena
print(txt[::2]) #Muestra todo el txt, pero haciendo saltos cada dos indices
print(txt[::3]) #Muestra todo el txt, pero haciendo saltos cada tres indices

print(txt[5:25:2]) #Muestra el recorte, pero haciendo saltos cada dos indices
print(txt[25:45:5]) #Muestra el recorte, pero haciendo saltos cada cinco indices
"""
#--------------------------------------------------------------------------------------------
#                                    FINALIZA LA AYUDA
#--------------------------------------------------------------------------------------------


#Ejercicio 3
"""
*Hacer un programa que muestre una recorte de los caracteres de
un text pre definido y que muestre los indices positivos haciendo
"saltos" de dos posiciones(uno de por medio :D)
Ejm
txt = |H|O|L|A| |M|I| |L||A|P|T|O|P| |E|S| |N|U|E|V|A|
Recorte = |M|I| |L||A|P|T|O|P|
Indices pares del recorte = |I||L||P|O|
"""

txt_ej3 = "Don't Worry, Be Happy"
trim_txt3 = txt_ej3[13:]
even_index_trim = trim_txt3[1::2]
print(txt_ej3, "\n\n")
print(trim_txt3, "\n\n")
print(even_index_trim, "\n\n")


#Ejercicio 4
"""
Modifique el ejercicio 3 y que la seleccion se realice utilizando
indices negativos
"""
trim_negative = txt_ej3[-len(txt_ej3):-10]
print(trim_negative, "\n\n")
odd_index_trim = trim_negative[::2]
print(odd_index_trim, "\n\n")



#Ejercicio 5
"""
Modifique el ejercicio 3 el usuario debe ser quien elija entre usar
indices + o - y ademas el numero de saltos para mostrar los indices
"""
user_select = input("What da fuck do you want nigga? Negative index or Positive index? ")
if "positive" in user_select.lower() :
    print("\n\n", txt_ej3, "\n\n")
    print(trim_txt3, "\n\n")
    print(even_index_trim, "\n\n")

else:
    print("\n\n", trim_negative, "\n\n")
    print(odd_index_trim, "\n\n")