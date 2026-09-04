def sumar(a, b):
 # TODO: implementar suma
 pass
def restar(a, b):
    return a - b

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultado = restar(num1, num2)

print(f"La resta de {num1} - {num2} es {resultado}")

def multiplicar(a, b):
  return a * b
 
def dividir(a, b):
 # TODO: implementar división
 pass
def main():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    print("Resultado de la suma:", sumar(numero1, numero2))
    print("Resultado de la resta:", restar(numero1, numero2))
    print("Resultado de la multiplicación:", multiplicar(numero1, numero2))
    print("Resultado de la división:", dividir(numero1, numero2))
if __name__ == "__main__":
 main()