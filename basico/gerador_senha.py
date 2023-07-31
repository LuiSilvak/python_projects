# Gerador de Senha em Python

import random
import string
def gerador_de_senha(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    senha_usuario = ""
    for i in range(0, len_pass):
        digit = random.choice(options)
        senha_usuario = senha_usuario + digit

    return senha_usuario

choice_user = input("Quantos dígitos na senha? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()

response = gerador_de_senha(len_pass = choice_user)
print(f"Senha gerada:\n{response}")