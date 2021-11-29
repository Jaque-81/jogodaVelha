import os
import random
from colorama import Fore, Back, Style


#primeira coisa é declarar variáveis globais
jogar_novamente = "s"
jogadas=0
quem_jogada = 2 #um é o pc e o outro o usuário
max_jogadas = 9
vit = "n" #verificar vitóriia e pode ser do tipo boolean
velha=[
  [" "," "," "],
  [" "," "," "],
  [" "," "," "]
]
def tela ():
  global velha #indica que eu vou usar a variavel global declarada à cima. 
  global jogadas
  os.system("cls")
  print("    0   1   2")
  print("0:  "+velha[0][0]+ " | "+velha[0][1]+ " | "+velha[0][2]) 
  print("   ","-"*11)
  print("1:  "+velha[1][0]+ " | "+velha[1][1]+ " | "+velha[1][2]) 
  print("   ","-"*11)
  print("2:  "+velha[2][0]+ " | "+velha[2][1]+ " | "+velha[2][2]) 
  print("   ","-"*11)
  print("Jogadas " + Fore.BLUE + str(jogadas) + Fore.RESET)

tela()