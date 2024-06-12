# ATIVIDADE 03
# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar. 
# Escreva um código que imprima todos os números exceto o número 13. Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'. 
# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

# Utilizando o while
numero_treze = 13
numero = 20

while numero >= 1:
  if numero == numero_treze:
    numero -= 1
    continue
  print(numero)
  numero -= 1

# Utilizando o for
numero_treze = 13

for i in range(20, 1 - 1, -1):
if i == numero_treze:
  continue
print(i)


