    VAR
      fumantes_animais, area_alocacao : caractere
      numero_pessoas : inteiro

    INICIO
      ESCREVA("Quantas pessoas estão em um grupo? ")
      LEIA(numero_pessoas)
    
      SE numero_pessoas >= 5 ENTAO
         area_alocacao = "1° Andar"
         ESCREVA("O grupo deve ser alocado na ", area_alocacao)
      SENAO
          ESCREVA("O grupo possui fumantes ou animais de estimação? (Sim/não) ")
          LEIA(fumantes_animais)
        
          SE fumantes_animais = "sim" ENTAO
            area_alocacao = "Área Externa"
            ESCREVA("O grupo deve ser alocado na ", area_alocacao)
          SENAO
             area_alocacao = "Térreo"
          FIMSE
        FIMSE
      ESCREVA("O grupo deve ser alocado na ", area_alocacao)
    FIMALGORITMO


