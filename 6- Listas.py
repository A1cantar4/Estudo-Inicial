# Listas podem ser de inteiros, strings, mistos, etc.
bolas = [1,2,3,4,5,6,7,8,9,10] # a posição do 1º valor da lista é 0, o segundo é 1, e assim por diante
marca = ["omo", "ypê"] # essa regra se aplica a todos tipos de lista
baderna = ["assolan", 1, False, 9.44] # inclusive nessa malucona kkkk

# para acessar a lista deve-se utilizar a posição do item na lista, ex:
print(bolas[0])
print(marca[1])
print(baderna[3])

# já pra modificar os elementos da lista, deve-se escrever igual uma variável
# porém indicando qual item (pela posição) será substituido
marca[1] = "assolan"
print(marca) 
print(marca[1]) # esse se quiser ver o que foi alterado diretamente

# da pra adicionar, remover e saber qual tamanho da lista
# ".append()" adiciona um item
# ".remove()" remove o item
# "len()" exibe a quantidade de itens.

bolas.append(11)
print(bolas) # Agora a lista "bolas" tem 11 itens, quer ver?
quantidade = len(bolas)
print("Existem", quantidade, "Bolas na Lista")

# pode ser escrito diretamente, sem variável
print("Existem", len(bolas), "Bolas na Lista")


baderna.remove(False) # utilize o valor correspondente na lista
print(baderna)
print("Agora tem somente", len(baderna), "itens na lista")
