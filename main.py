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