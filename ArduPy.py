import os

nombre = str(input("Como se va a llamar tu programa: "))

f = open("{}.ino".format(nombre), 'w')

variables = int(input("Cuantas varables deseas generar? "))

for var in range (variables):
	print("""

		1)byte
		2)int
		3)bool
		4)char(ingresar el valor entre comillas)
		5)String(ingresar el valor entre comillas)
		6)float


		""")
	dato = int(input("Ingrese el tipo de variable: "))


	if dato == 1:
		dat = "byte"

	if dato == 2:
		dat = "int"


	if dato == 3:
		dat = "bool"


	if dato == 4:
		dat = "char"


	if dato == 5:
		dat = "String"


	if dato == 6:
		dat = "float"

	val = str(input("nombre de la variable: "))
	print("\n")
	valor = str(input("valor de la variable (Si no quieres ningun valor dejalo en blanco): " ))
	print("\n")
	f.write(dat + " " + val + " " + "=" + " " +valor + ";" + "\n")




f.close
