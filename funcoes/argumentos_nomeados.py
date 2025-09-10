def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro salvo: {marca} {modelo} {ano} {placa}')

# Chamando a função com argumentos nomeados
salvar_carro("Toyota", "Corolla", 2020, "ABC-1234")
salvar_carro(modelo="Civic", marca="Honda", placa="XYZ-5678", ano=2019)
salvar_carro(placa="DEF-4321", ano=2021, marca="Ford", modelo="Focus")

# Saída:
# Carro salvo: Toyota Corolla 2020 ABC-1234
# Carro salvo: Honda Civic 2019 XYZ-5678
# Carro salvo: Ford Focus 2021 DEF-4321