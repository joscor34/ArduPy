import os
import time
import sys

if sys.version_info.major < 3:
    print("ArduPy solo esta soportado para python3.")
    exit(0)


vx = 1
wl = 1
wh = 1
oh = 1

piness = []
varles = []


while oh == 1:

	nombre = str(input("Como se va a llamar tu programa: "))

	f = open("{}.ino".format(nombre), 'w')




	variables = int(input("Cuantas variables deseas generar?(escriba '0' si no desea generar ninguna):  "))

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
		varles.append(val)
		valor = str(input("valor de la variable (Si no quieres ningun valor dejalo en blanco): " ))
		
		if len(valor) == 0:
			print("\n")
			f.write(dat + " " + val + " " +valor+ ";" + "\n")


		elif len(valor) != 0:
			print("\n")
			f.write(dat + " " + val + " " + "=" + " " +valor+ ";" + "\n")


	print("Generando el setup")
	for i in range(3):
		print(".")
		time.sleep(1)

	f.write("""
	void setup(){

	""")

	while vx == 1:
		

		print("""

				
				1)configuar pines
				2)habilitar el puerto serial
				3)generar el loop

			""")

		accion = int(input("Que deseas hacer?: "))
		print("\n")

		if accion == 1:
			pins = int(input("Cuantos pines deseas habilitar?: "))

			for p in range(pins):
				Pn = str(input("Dame el numero del pin que deseas configuar: "))
				piness.append(Pn)

				print("""
					
					1)Entrada
					2)Salida

					""")
				Pv = int(input("En que estado deseas poner el pin?: "))
				
				if Pv == 1:
						valorpin = "INPUT"

				elif Pv == 2:
						valorpin = "OUTPUT"


				f.write("pinMode(" + Pn + "," + valorpin + ");" + "\n")	


		if accion == 2:

		 print("""

			1)300
			2)1200
			3)2400
			4)4800
			5)9600
			6)19200
			7)38400
			8)57600
			9)74880
			10)115200
			11)230400
			12)250000
			13)500000
			14)1000000 
			15)2000000

		 """)
		 baudRate = int(input("Selecciona el Buad-Rate por favor: "))

		 if baudRate == 1:
		 	baudR = 300


		 if baudRate == 2:
		 	baudR = 1200


		 if baudRate == 3:
		 	baudR = 2400


		 if baudRate == 4:
		 	baudR = 4800


		 if baudRate == 5:
		 	baudR = 9600


		 if baudRate == 6:
		 	baudR = 19200


		 if baudRate == 7:
		 	baudR = 38400


		 if baudRate == 8:
		 	baudR = 57600


		 if baudRate == 9:
		 	baudR = 74880


		 if baudRate == 10:
		 	baudR = 115200


		 if baudRate == 11:
		 	baudR = 230400


		 if baudRate == 12:
		 	baudR = 250000


		 if baudRate == 13:
		 	baudR = 500000


		 if baudRate == 14:
		 	baudR = 1000000


		 if baudRate == 15:
		 	baudR = 2000000


		 f.write("Serial.begin("+ str(baudR) +");"+"\n")

		if accion == 3:
			vx = vx + 1


	f.write("}")
	f.write("\n")


	print("Generando loop")
	for u in range(3):
		print(".")
		time.sleep(1) 

	f.write("""

	void loop(){

	""")

	print("""

	1)Hacer una escritura digital/analogica
	2)Hacer una lectura digital/analogica
	3)Colocar un delay
	4)Colocar un ciclo
	5)Colocar un if/else/else if
	6)Colocar un Switch
	7)Hacer un print/println
	8)Ingresar una nueva variable
	9)Otro

	""")

	respuestaL = int(input("Ingresa tu respuesta: "))


	if respuestaL == 1:

		while wh == 1:
			
			print("""

				1)analogico		
				2)digital

			""")

			Write = int(input("Selecciona la opcion: "))

			if Write == 1:

				print(piness)

				loop = "analog"
				pon = str(input("Selecciona el pin: "))
				if pon in piness: 
					rango = int(input("Seleccions un rango de 0 a 255"))

					if rango > 255:
						print("No se puede configurar ese rango")

					elif rango < 255:

						f.write(loop * "Write(" + pon + rango + ");")
				else:

					print("Ese pin NO esta declarado")	

			elif Write == 2:

				print(piness)

				loop = "digital"

				pon = str(input("Selecciona el pin: "))
				if pon in piness: 

					print("""

					1)HIGH
					2)LOW

					""")
					estados = int(input("En que estado quieres poner el pin: "))

					if estados > 2:
						print("Ingresa un valor valido")
							
				else:

					print("Ese pin NO esta declarado")

			elif Write > 3:
					print("selecciona una opcion valida")


	f.close
