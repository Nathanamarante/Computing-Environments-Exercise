#Tratamento de exceções

try:
    print(x)
except NameError:
    print('Variável não definida.')

try:
    print(y)
except:
    print('Uma exceção ocorreu')

#Exceção na abertura de arquivo

try:
    f = open ('arquivo_teste.txt')
    f.write('Teste escrita no arquivo')
except:
    print('Algo deu errado com o arquivo')