#EQUIPO 5 - COMPONENTES SIMETRICAS
#Para ejecutar el codigo se requiere instalar librerias adicionales "Numpy" y "Matplotlib"
#Se puede descargar Numpy siguiendo el siguiente manual: https://phoenixnap.com/kb/install-numpy
#Se puede descargar Matplotlib siguiendo el siguiente manual: https://www.tutorialspoint.com/how-to-install-matplotlib-in-python

import cmath
import math
import numpy as np
import matplotlib.pyplot as plt


def mult_matriz(A, B): #Multiplicacion de matrices
	resultado= []
	var_suma=0
	for i in range(len(A)):
		for j in range(len(B)):
			var_suma += A[i][j]*B[j]
		resultado.append(var_suma) 
		var_suma = 0
	return resultado


def SimetricalComp(Iabc, B = True):#Obtiene las componentes simetricas
	corriente_rect = []
	magnitud= []
	angulo = []
	re = []
	I012= []

	for val in range(len(Iabc)):
		magnitud.append(Iabc[val][0])
		angulo.append(Iabc[val][1]*math.pi/180)
	for i in range(len(magnitud)):
		corriente_rect.append(complex(magnitud[i]*math.cos(angulo[i]), magnitud[i]*math.sin(angulo[i])));

	a = complex(math.cos(2*math.pi/3), math.sin(2*math.pi/3))
	A=[[1, 1, 1], [1, a**2, a], [1, a, a**2]]

	if B:
		A = np.linalg.inv(A)
	
	re = mult_matriz(A, corriente_rect)
	for i in range(len(re)):
		I012.append([abs(re[i]), cmath.phase(re[i])])
	return I012



def p_r(rect):#convierte de coordenadas polares a rectangulares
	r= []
	for i in range(len(rect)):
		com=cmath.rect(rect[i][0], rect[i][1])
		r.append([com.real, com.imag])
	return r



def gf(t, v, s ):# Graficas
	v=np.array(v)
	o = np.array([[0, 0, 0], [0, 0, 0]])
	plt.subplot(t)
	plt.quiver(*o, v[:, 0], v[:, 1], color=['green', 'blue', 'red'], angles='xy', scale_units='xy', scale = 1)
	plt.ylim(-2, 2)
	plt.xlim(-2, 2)
	plt.title(s)
	plt.grid(True)

def graficar(val, B = True):# Graficas
	
	if B:
		I012 = SimetricalComp(val)
		I012 = np.array(I012)
		Iabc = []
		I0 = []
		I1 = []
		I2 = []

		#fig 1
		for i in range(len(val)):
			Iabc.append([val[i][0], (val[i][1]*math.pi)/180])
		Iabc = p_r(Iabc)
		gf(221, Iabc, "Desbalanceado")

		#fig 2
		I0=[list(I012[0,:]), list(I012[0,:]), list(I012[0,:])]
		I0=p_r(I0)
		gf(222, I0, "Secuencia 0")

		#fig 3
		I1 =[list(I012[1,:]), list(I012[1,:]), list(I012[1,:])]
		I1 =[[I1[0][0], I1[0][1]], 
			[I1[1][0], I1[1][1]+(math.pi*2)/3], 
			[I1[2][0], I1[2][1]+(math.pi*4)/3]]
		I1=p_r(I1)
		gf(223, I1, "Secuencia 1")

		#fig 4
		I2 = [list(I012[2,:]), list(I012[2,:]), list(I012[2,:])]
		I2 =[[I2[0][0], I2[0][1]], 
			[I2[1][0], I2[1][1]+(math.pi*2)/3], 
			[I2[2][0], I2[2][1]+(math.pi*4)/3]]
		I2=p_r(I2)
		gf(224, I2, "Secuencia 2")
	
	else:

		I012 = []
		for i in range(len(val)):
			I012.append([val[i][0], (val[i][1]*math.pi)/180])
		
		I012 = np.array(I012)
		Iabc = []
		I0 = []
		I1 = []
		I2 = []

		#fig 1
		Iabc = SimetricalComp(val)
		Iabc = p_r(Iabc)
	
		gf(221, Iabc, "Desbalanceado")

		#fig 2
		I0=[list(I012[0,:]), list(I012[0,:]), list(I012[0,:])]
		I0=p_r(I0)
		gf(222, I0, "Secuencia 0")

		#fig 3
		I1 =[list(I012[1,:]), list(I012[1,:]), list(I012[1,:])]
		I1 =[[I1[0][0], I1[0][1]], 
			[I1[1][0], I1[1][1]+(math.pi*2)/3], 
			[I1[2][0], I1[2][1]+(math.pi*4)/3]]
		I1=p_r(I1)
		gf(223, I1, "Secuencia 1")

		#fig 4
		I2 = [list(I012[2,:]), list(I012[2,:]), list(I012[2,:])]
		I2 =[[I2[0][0], I2[0][1]], 
			[I2[1][0], I2[1][1]+(math.pi*2)/3], 
			[I2[2][0], I2[2][1]+(math.pi*4)/3]]
		I2=p_r(I2)
		gf(224, I2, "Secuencia 1")
		pass
	
	plt.tight_layout()
	plt.show()

def obtenerValor():# obtener los valores
	cA =  float(input("Magnitud A: "))
	mA = float(input('Angulo A: '))
	cB = float(input("Magnitud B: "))
	mB = float(input('Angulo B: '))
	cC = float(input('Magnitud C: '))
	mC = float(input('Angulo C: '))
	Componente = [[cA, mA], [cB, mB], [cC, mC]]
	return Componente

l = 's'
while l == 's' or l=='S':
	print('')
	valor_VI = [] 
	print("1. Calcular.")
	print('2. Salir.')
	val = input()
	if val == '1':
		valor_VI = obtenerValor()
		print("1. Componentes simetricas.")
		print('2. Corriente desbalanceada.')
		val = input()
		if val == '1':
			r = SimetricalComp(valor_VI)
			resultado=[] 
			for i in range(len(r)):
				resultado.append([round(r[i][0], 3), round((r[i][1]*180)/3.1415, 2)])
			print("Resultado: ")
			print(resultado)
			graficar(valor_VI)
		elif val == '2':
			print("Resultado: ")
			r = SimetricalComp(valor_VI, False);
			resultado=[]
			for i in range(len(r)):
				resultado.append([round(r[i][0], 3), round((r[i][1]*180)/3.1415, 2)])
			print("Resultado: ")
			print(resultado)
	else:
	   l = 'd'
