import calculadora_binaria
from functools import reduce

bin_calculator = calculadora_binaria.CalculadoraBinaria()

abcfilename = 'C:/Users/rafae/PycharmProjects/checksum/abc.txt'
with open(abcfilename, 'rb') as open_file:
    content = list(map(lambda x: bin(ord(chr(x))), list(open_file.read())))

abc_sequencias_binarias = bin_calculator.converte_bits_sequencia_binaria(content)
abc_soma = reduce(lambda x, y: bin_calculator.prepara_soma(x, y), abc_sequencias_binarias)
abc_complemento_1 = bin_calculator.complemento_1(abc_soma)


cbafilename = 'C:/Users/rafae/PycharmProjects/checksum/cba.txt'
with open(cbafilename, 'rb') as open_file:
    content = list(map(lambda x: bin(ord(chr(x))), list(open_file.read())))

cba_sequencias_binarias = bin_calculator.converte_bits_sequencia_binaria(content)
cba_soma = reduce(lambda x, y: bin_calculator.prepara_soma(x, y), cba_sequencias_binarias)
cba_complemento_1 = bin_calculator.complemento_1(cba_soma)


dddfilename = 'C:/Users/rafae/PycharmProjects/checksum/ddd.txt'
with open(dddfilename, 'rb') as open_file:
    content = list(map(lambda x: bin(ord(chr(x))), list(open_file.read())))

ddd_sequencias_binarias = bin_calculator.converte_bits_sequencia_binaria(content)
ddd_soma = reduce(lambda x, y: bin_calculator.prepara_soma(x, y), ddd_sequencias_binarias)
ddd_complemento_1 = bin_calculator.complemento_1(ddd_soma)


txtGrandefilename = 'C:/Users/rafae/PycharmProjects/checksum/txtGrande.txt'
with open(txtGrandefilename, 'rb') as open_file:
    content = list(map(lambda x: bin(ord(chr(x))), list(open_file.read())))

txt_sequencias_binarias = bin_calculator.converte_bits_sequencia_binaria(content)
txt_soma = reduce(lambda x, y: bin_calculator.prepara_soma(x, y), txt_sequencias_binarias)
txt_complemento_1 = bin_calculator.complemento_1(txt_soma)


print(' === abc === ')
print('Soma dos valores: \t\t ', abc_soma)
print('Complemento dos valores: ', bin_calculator.complemento_1(abc_soma))

print('\n === cba === ')
print('Soma dos valores: \t\t ', cba_soma)
print('Complemento dos valores: ', bin_calculator.complemento_1(cba_soma))

print('\n === ddd === ')
print('Soma dos valores: \t\t ', ddd_soma)
print('Complemento dos valores: ', bin_calculator.complemento_1(ddd_soma))

print('\n === txtGrande === ')
print('Soma dos valores: \t\t ', txt_soma)
print('Complemento dos valores: ', bin_calculator.complemento_1(txt_soma))

print('\n === Comparações booleanas === ')
print('Checksum de abc.txt é diferente do checksum de cba.txt?\n\t', abc_soma != cba_soma)
print('\nChecksum de abc.txt é diferente do checksum de ddd.txt E de txtGrande.txt?\n\t', (abc_soma != ddd_soma
                                                                                           and abc_soma != txt_soma))
print('\nChecksum de ddd.txt e de txtGrande.txt são diferentes?\n\t', ddd_soma != txt_soma)

abc_soma_mais_complemento = bin_calculator.prepara_soma(abc_soma, abc_complemento_1)
cba_soma_mais_complemento = bin_calculator.prepara_soma(cba_soma, cba_complemento_1)
ddd_soma_mais_complemento = bin_calculator.prepara_soma(ddd_soma, ddd_complemento_1)
txtGrande_soma_mais_complemento = bin_calculator.prepara_soma(txt_soma, txt_complemento_1)
print('\nValor da soma com seu respectivo complemento de qualquer um dos quatro arquivos .txt'
      ' contém apenas dígitos 1?\n\t', (all(bit == '1' for bit in abc_soma_mais_complemento)
                                        and all(bit == '1' for bit in cba_soma_mais_complemento)
                                        and all(bit == '1' for bit in ddd_soma_mais_complemento)
                                        and all(bit == '1' for bit in txtGrande_soma_mais_complemento)))