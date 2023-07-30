# Pedra, Papel, Tesoura

import random

print("********************************************")
print("Seja bem vindo ao jogo Pedra, Papel, Tesoura")
print("******************************************** \n")

user_points = 0
computer_points = 0

options = ["r", "t", "p"]

while True:
    print("Escolha:   R(Pedra)    T(Tesoura)    P(Papel)    Q(Sair do jogo)  \n")
    user_choice = input("Digite aqui: ").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    computer_choice = random.randint(0,2)
    # 0 => R(Pedra)     1 => T(Tesoura)     2 => P(Papel)
    computer_option = options[computer_choice]

    print(f"O computador escolheu: {computer_option} ")

    # Estruturas Condicionais destinadas ao Jogo
    if user_choice == computer_option:
        print("Empate")
    elif user_choice == "r" and computer_option == "t":
        print("Você ganhou! Parabéns!")
        user_points = user_points + 1
    elif user_choice == "t" and computer_option == "p":
        print("Você ganhou! Parabéns!")
        user_points = user_points + 1
    elif user_choice == "p" and computer_option == "r":
        print("Você ganhou! Parabéns!")
        user_points = user_points + 1
    else:
        print("Computador ganhou! Tente novamente!")
        computer_points = computer_points + 1

    print("*** Resultado Parcial ***")
    print(f"Pontos do usuário: {user_points}")
    print(f"Pontos do computador: {computer_points}")


# Resultados Finais
if user_points > computer_points:
    print(f"Você {user_points} x {computer_points} Computador")
    print("Resultado Final: Você venceu! Parabéns! \n")
elif user_points == computer_points:
    print(f"Você {user_points} x {computer_points} Computador")
    print("Resultado Final: Empate! \n")
else:
    print(f"Você {user_points} x {computer_points} Computador")
    print("Resultado Final: Você perdeu! Tente novamente! \n")

print("Final de Jogo!")
print("Até a próxima!")
