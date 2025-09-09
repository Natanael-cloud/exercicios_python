nome = "Natanael Paiva Costa"

# 1. Acessando o primeiro caractere
print(nome[0])  
# Saída: 'N'

# 2. Pegando os primeiros 9 caracteres
print(nome[:9])  
# Saída: 'Natanael '

# 3. Pegando os caracteres após o índice 9
print(nome[10:])  
# Saída: 'Paiva Costa'

# 4. Pegando uma fatia específica (índices de 10 a 14)
print(nome[10:15])  
# Saída: 'Paiva'

# 5. Pegando uma fatia com passo de 2
print(nome[10:15:2])  
# Saída: 'Pia'

# 6. Pegando todos os caracteres de forma alternada
print(nome[::2])  
# Saída: 'NtaalPaaot'

# 7. Invertendo a string
print(nome[::-1])  
# Saída: 'atsoC aviaP lanehtaN'




