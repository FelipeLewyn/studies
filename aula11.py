nome = 'felipe c. bazolli'
altura = 1.71
peso = 70
imc = peso / altura ** 2

# a letra f permite que use variaveis dentro de strings 
# formataçao
linha_1 = f'{nome} tem {altura:.2f} de altura '# :.= casas decimais

linha_2 = f'pesa {peso} quilos seu imc e {imc:.1f}'

print(linha_1)
print(linha_2)