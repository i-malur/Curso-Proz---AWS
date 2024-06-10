# Atividade 06

* Num torneio de e-sports é necessário que todos os integrantes da mesma equipe tenham etiquetas que os identifiquem. Por exemplo, se o nome da equipe é “Os Lutadores”, o primeiro membro deve ter uma etiqueta “Os Lutadores – 1", o segundo membro “Os Lutadores – 2", e assim pela frente. Elabore um algoritmo que permita ao usuário inserir o nome da equipe, e imprime etiquetas para os 5 membros da equipe seguindo o exemplo mostrado acima.

    VAR
      nome_equipe : caractere
      contador : inteiro
    INICIO
	   ESCREVA(“Digite nome de equipe: “)
	   LEIA(nome_equipe)
	   PARA contador <- 1 ATE 5 FACA
		   ESCREVA(nome_equipe, “ - ” ,contador)
	   FIMPARA
   FIMALGORITMO
