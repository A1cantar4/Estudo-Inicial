# FOR = Percorre toda Lista
# WHILE = Executa o Loop enquanto "algo" tiver "x" condição.
# BREAK = Encerra o Loop de vez
# CONTINUE = Pula a interação atual e vai para a próxima

# Crie Uma String com Lista para Iniciar Loop For
Árvore = ["Frutífera", "Sem Folhas", "Cortada"] # 3 Itens na String

# Crie o Looping usando a varíavel como condição
for Árvore in Árvore: # IN é utilizado para verificar a presença de algo na lista.
    if Árvore == "Sem Folhas":
        break # Dessa maneira o Loop executará somente o 1 item, o 2 e 3 serão inutilizados
    print("Observei no caminho uma Árvore", Árvore)
# Sem o Break, Irá gerar 3 Linhas com as possibilidades da Variável.
 
# Outro exemplo, só que com o Continue
Casa = 1

for Casa in range(10): # Range gera uma limitação de uma sequência
    if Casa == 5:
        continue # Pula valor quando chegar em 5
    print("Entrega de IFOOD na Casa", Casa)


# Loop usando While
Carros = 2 

# Vai ser um loop para contar quantos carros passaram na rua
# Iniciará em 2 e parará em 5
while Carros < 6:
    print("Passou apenas", Carros, "Carros")
    Carros += 1 # "+=" vai aumentar o número em 1 para toda vez que o loop contar
