# Temporizador

import time

print("========================================")
print("Seja bem vindo ao Temporizador em Python")
print("========================================")

tempo = input("Digite o tempo que deseja (em segundos): ")

# Condicional para confirmar se é ou não é um número:
if tempo.isdigit():
    t_int = int(tempo)

    # Utilizando import e while para criação do temporizador
    while t_int != 0:
        minutos, segundos = divmod(t_int, 60)
        tempo = f"{minutos:02d}:{segundos:02d}"
        print(f'\r{tempo}', end='')
        time.sleep(1)
        t_int = t_int - 1

else:
    print("Você não digitou um número. Tente novamente!")
    quit()

print("\n")
print("Tempo Encerrado!")



"""
Conversão de tempo de segundos para minutos (Modo Normal)

t_min = t_int / 60
print(f"O tempo em minutos é igual a {t_min} minutos")

t_hora = t_min / 60
print(f"O tempo em horas é igual a {t_hora} hora(s)")
"""



