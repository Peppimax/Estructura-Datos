#****************************************************************************************************
#Ejercicio 1
#uno = input("Ingreasa un numero : ")
#dos = input("Dame el segundo numero : ")
#tres = input("Dame el tercer numero : ")


#uno = int(uno)
#dos = int(dos)
#tres = int(tres)

#if uno > dos and uno > tres:
    #print(f"El numero mayor es {uno}")
#elif dos > uno and dos > tres:
    #print(f"El numero mayor es {dos}")
#else:
    #print(f"El numero mayor es {tres}")


#if uno < dos and uno < tres:
    #print(f"El numero menor es {uno}")
#elif dos < uno and dos < tres:
    #print(f"El numero menor es {dos}")
#else:
    #print(f"El numero menor es {tres}")

#****************************************************************************************************
#Ejercicio 2

#numeropar= input("Ingresa un numero para determinar si es par : ")

#numeropar= int(numeropar)

#if numeropar % 2 == 0:
    #print(f"El numero {numeropar} es par")
#else:
    #print(f"El numero {numeropar} es impar")


#****************************************************************************************************
#Ejercicio 3

numerouno = input("Ingresa un numero : ")
numerodos = input("Ingresa otro numero : ")

numerouno = int(numerouno)
numerodos = int(numerodos)

calculo = input("Que deseas realizar, para una suma presiona ingresa el numero 1, para una resta presiona el numero 2, para una multiplicacion presiona el numero 3, para una division presiona el numero 4 : ")

calculo = int(calculo)

if calculo == 1:
    print(f"La suma de los numeros es {numerouno + numerodos}")
elif calculo == 2:
    print(f"La resta de los numeros es {numerouno - numerodos}")
elif calculo == 3:
    print(f"La multiplicacion de los numeros es {numerouno * numerodos}")
elif calculo == 4:
    print(f"La division de los numeros es {numerouno / numerodos}")
else:
    print("Ingresa un numero valido")

#****************************************************************************************************
#Ejercicio 4    

#peso = input("Ingresa tu peso : ")
#estatura = input("Ingresa tu estatura : ")

#peso = float(peso)
#estatura = float(estatura)

#imc = peso / (estatura ** 2)

#print(f"Tu indice de masa corporal es {imc}")

#if imc > 25:
    #print("Tienes sobrepeso")

#****************************************************************************************************