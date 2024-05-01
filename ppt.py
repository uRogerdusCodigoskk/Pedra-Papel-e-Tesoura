import random

#TITULO
print ("FAÇA SUA ESCOLHA!!")
print ("1=papel, 2=tesoura, 3=pedra")

#JOGADOR ESCOLHENDO
numero_jogador = int (input("Qual sua escolha?:  "))
print (numero_jogador)

#ALEATORIZADOR
numero_sistema = (random.randint(1,3))

#ESCOLHA JOGADOR
if numero_jogador == 1: print ("você escolheu papel")
elif numero_jogador == 2: print("você escolheu tesoura")
elif numero_jogador == 3: print("você escolheu pedra")

#ESCOLHA SISTEMA
if numero_sistema == 1: print ("sistema escolheu papel")
elif numero_sistema == 2: print("sistema escolheu tesoura")
elif numero_sistema == 3: print("sistema escolheu pedra")

#VITORIAS/DERROTAS/EMPATES
if numero_sistema == numero_jogador: print ("Empate!")
elif numero_sistema == 1 and numero_jogador == 2: print ("Você Ganhou!")
elif numero_sistema == 1 and numero_jogador == 3: print ("Você Perdeu!")
elif numero_sistema == 2 and numero_jogador == 3: print ("Você Ganhou!")
if numero_jogador == 1 and numero_sistema == 2: print ("Você Perdeu!")
elif numero_jogador == 1 and numero_sistema == 3: print ("Você Ganhou!")
elif numero_jogador == 2 and numero_sistema == 3: print ("Você Perdeu!")

print()