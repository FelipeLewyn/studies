a = 'A'
b = 'b'
c = 1.1 
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c)
# erro out of range = buscando coisa que ja acabou 
# indice = tudo que tem uma ordem começa do 0 a={0} b={1}

print(formato)
