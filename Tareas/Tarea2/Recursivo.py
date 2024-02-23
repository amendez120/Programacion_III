

def binario(num):
    if(num == 0):
        return ""
    else:
        return binario(num//2) + str(num%2)

  

    
def contar_digitos(num):
    if num == 0:
        return 0
    else:
        return 1 + contar_digitos(num // 10)



def raiz_cuadrada_entera(num):
    return calcular_raiz_cuadrada(num, 1)

def calcular_raiz_cuadrada(num, guess):
    if guess * guess <= num < (guess + 1) * (guess + 1):
        return guess
    else:
        return calcular_raiz_cuadrada(num, guess + 1)



def convertir_a_decimal(romano):
    valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if romano == '':
        return 0
    elif len(romano) == 1:
        return valores_romanos[romano]
    else:
        if valores_romanos[romano[0]] < valores_romanos[romano[1]]:
            return convertir_a_decimal(romano[1:]) - valores_romanos[romano[0]]
        else:
            return valores_romanos[romano[0]] + convertir_a_decimal(romano[1:])


def suma_numeros_enteros(num):
    if num == 0:
        return 0
    else:
        return num + suma_numeros_enteros(num - 1)




def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            num = int(input("Introduce un número entero: "))
            print("Binario:", binario(num))
        elif opcion == '2':
            num = int(input("Introduce un número entero: "))
            print("Cantidad de dígitos:", contar_digitos(num))
        elif opcion == '3':
            num = int(input("Introduce un número entero: "))
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(num))
        elif opcion == '4':
            romano = input("Introduce un número romano: ")
            print("Decimal:", convertir_a_decimal(romano))
        elif opcion == '5':
            num = int(input("Introduce un número entero positivo: "))
            print("Suma de números enteros hasta", num, ":", suma_numeros_enteros(num))
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")



if __name__ == "__main__":
    menu()