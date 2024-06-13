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

print(calculadora(10, 5, 1))  
print(calculadora(10, 5, 5))  
