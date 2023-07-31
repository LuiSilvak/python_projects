#001 - Quiz

print("Seja muito bem vindo ao Quiz!")

digito = input("Quer começar o quiz? (S/N) ")

if digito == "S":
    print("Prazer, estamos começando o quiz!")

    print("Questão_1 - Quem desenvolveu o jogo Gran Theft Auto (GTA)? \n"
          "(A) Rockstar Games \n"
          "(B) Ubisoft \n"
          "(C) Activision \n"
          "(D) EA \n")
    questao_1 = input("Digite sua resposta: ")
    if questao_1 == "A":
        print("Resposta correta!")
    else:
        print("Resposta incorreta!")

    print("Questão 2 - Qual o nome do protagonista do Jogo GTA San Andreas \n"
          "(A) Carlos John \n"
          "(B) Carl Jonhson \n"
          "(C) Carl Jaqueline \n"
          "(D) Carlos Jonhson")
    questao_2 = input("Digite sua resposta: ")
    if questao_2 == "B":
        print("Resposta correta!")
    else:
        print("Resposta incorreta!")

elif digito == "N":
    print("Obrigado por acessar, até logo!")
    quit()
else:
    print("Não entendi, tente novamente!")
