#002 - Jogo de Adivinhação

import random

print("-------------------------------------")
print("Seja bem vindo ao jogo de adivinhação")
print("-------------------------------------")

digito_number = input("Digite um número: ")

# Digite um número
if digito_number.isdigit():
    num_int = int(digito_number)
else:
    print("Que pena, não é um número! Digite novamente!")

random_number = random.randint(0, num_int)

# Adivinhe um número
n_tentativa = 0

while True:
    resposta_usuario = input("Adivinhe um número: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)
    else:
        print("Não é número! Tente novamente!")
        continue

    n_tentativa = n_tentativa + 1
    if resposta_usuario == random_number:
        print("Parabéns, você acertou!")
        break
    elif resposta_usuario > random_number:
        print("Você chutou alto. O número aleatório é menor!")
    else:
        print("Você chutou baixo. O número aleatório é maior!")

print("Número de tentativas: " + str(n_tentativa))