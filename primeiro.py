print("Bem vindo no jogo de adivinhação!")

numero_secreto = 19

chute_str = input("Digite seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
   print("Você acertou!")
else:
   print("Você errou!")
