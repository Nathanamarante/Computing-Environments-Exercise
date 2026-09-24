#Classes e objetos

class classe_racional:
    x=5

print(classe_racional)

obj1 = classe_racional()
print(obj1.x)

#Função construtora

class insulina:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

p1 = insulina ('insulina', 284)
print(p1.nome)
print(p1.tamanho)


class mioglobina:
    def __init__(eu, nome, tamanho): #alterando o self para "eu"
        eu.nome = nome
        eu.tamanho = tamanho

    def minhafuncao(eumesmo): #eumesmo vai representar o próprio objeto
        print('proteina: ' + eumesmo.nome)

p2 = mioglobina('Mioglobina', 154)

p2.minhafuncao()

#Adicionando tamanho ao print

class mioglobina:
    def __init__(eu, nome, tamanho): #alterando o self para "eu"
        eu.nome = nome
        eu.tamanho = tamanho

    def minhafuncao(eumesmo): #eumesmo vai representar o próprio objeto
        print('proteina: ' + eumesmo.nome, eumesmo.tamanho)

p2 = mioglobina('Mioglobina', 154)

p2.minhafuncao()

#Modificando parâmetros (tamanho) do objeto anterior

class mioglobina:
    def __init__(eu, nome, tamanho): #alterando o self para "eu"
        eu.nome = nome
        eu.tamanho = tamanho

    def minhafuncao(eumesmo): #eumesmo vai representar o próprio objeto
        print('proteina: ' + eumesmo.nome, eumesmo.tamanho)


p2 = mioglobina('Mioglobina', 154)
p2.tamanho= 334

p2.minhafuncao()

# Deletando objetos

del p1
del p2
print(p1.tamanho, p1.nome) #Antes do del é imprimido "284 insulina". Agora retorna erro 'p1' is not defined pois foi deletado

p2.minhafuncao() #Antes do del é imprimido "proteina: Mioglobina 334"

# Deletando parâmetros de objetos
del p1.tamanho #Como p1 já foi deletado anteriormente não será possível deletá-lo