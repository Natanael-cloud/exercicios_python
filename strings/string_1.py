nome = "NaTaNael"


print(nome.lower())  # todas as letras minúsculas
print(nome.upper())  # todas as letras maiúsculas
print(nome.title())  # primeira letra maiúscula


texto = "   Olá, Mundo!   "
print(texto)
print(texto.strip())  # remove espaços no início e no fim
print(texto.lstrip())  # remove espaços no início
print(texto.rstrip())  # remove espaços no fim

menu = "Python"
print(menu.center(20, "-"))  # centraliza o texto em uma largura de 20, preenchendo com '-'
print(menu.ljust(20, "-"))  # alinha o texto à esquerda em uma largura de 20, preenchendo com '-'
print(menu.rjust(20, "-"))  # alinha o texto à direita em uma largura de 20, preenchendo com '-'

# o run de cada um desses exemplos acima 
# Saída:
""""
natanael
NATANAEL
Natanael
   Olá, Mundo!
Olá, Mundo!
Olá, Mundo!
-------Python-------
Python---------------
---------------Python   
"""