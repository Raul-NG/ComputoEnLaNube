import sys
import math

def create_arr():
    #Se crea una lista de los números enteros desde 1 hasta el argumento dado por consola.
    return list(range(1,int(sys.argv[1])+1)) #Se le suma 1 al argumento para que sí incluya a ese último número
    
def primos_func(arr):
    primos = [] 
    for num in arr: #Revisamos cada número del arreglo
        if num != 1: #Si el número es uno, por definición, no es primo. Así que no hace nada
            n = math.floor(math.sqrt(num)) #Solo basta revisar los factores que sean menor a la raíz cuadrada del número
            is_prime = True #Bandera para saber si es primo
            for i in range(2,n+1): #Revisamos los factores
                if num % i == 0: #Si el módulo es cero, entonces el número a revisar es múltiplo del factor.
                    is_prime = False #Así que la bandera se coloca en falso.
                    break #Termina el ciclo de revisión de factores.
            if is_prime:#Si fue primo, se agrega a la lista
                primos.append(num)
    return primos #Regresamos la lista de primos
    
input_arr = create_arr() #Creamos el arreglo de números
# print(input_arr) #Mostramos el arreglo completo
print(len(primos_func(input_arr))) #Mostramos el arreglo que tiene solamente a los primos.


    
    