# ATIVIDADE 4

def calculadora(num1, num2, operador):
  if operador == 1:
    return num1 + num2
  elif operador == 2:
    return num1 - num2
  elif operador == 3:
    return num1 * num2
  elif operador == 4:
    if num2 != 0:
      return num1 / num2 
    else:
      'Erro: Divisão por zero'
    else:
      return 0
      
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Escolha a operação:")
print("1: Soma")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")
operador = int(input("Digite o número da operação: "))

resultado = calculadora(num1, num2, operador)
print(f"O resultado é: {resultado}")
