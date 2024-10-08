# Valores para Variáveis denominados Operadores
L = 21
H = 22

# Operações Aritméticos
soma = L + H # Preciso comentar? kkkk
diferença = L - H # Subtração = -1
produto = L * H # Multiplicação = 462
divisão = L / H # Dá 0.95
divisão_inteira = L // H # Dividir arredondando = 0
resto = L % H # É o valor que ficaria no "resto" da divisão
potencia = L ** H # "L" elevado a "H"

# Exibição dos Calculos das Operações Aritméticas
print("Soma:", soma)
print("Diferença:", diferença)
print("Produto:", produto)
print("Divisão:", divisão)
print("Divisão Arredondada:", divisão_inteira)
print("Resto da Divisão: ", resto)
print("L elevado a H:", potencia)

# Operadores Comparativas
# "==" = Igual
# "!-" = Diferente
# "<" = Menor que
# ">" = Maior que
# "<=" = Menor ou Igual a
# ">=" = Maior ou Igual a

# Organizando as Variáveis
igual = L == H
diferente = L != H
maior_que = L > H
menor_que = L < H
menor_ou_igual = L <= H
maior_ou_igual = L >= H

#Personalizando Respostas (Aprendido no estudo das Variáveis)
if igual:
    Resposta = "Sim"
else:
    Resposta = "Não"
igual = Resposta

if diferente:
    Resposta = "Sim"
else:
    Resposta = "Não"
diferente = Resposta

if maior_que:   
    Resposta = "Sim"
else:
    Resposta = "Não"
maior_que = Resposta

if menor_que: 
    Resposta = "Sim"
else:
    Resposta = "Não"
menor_que = Resposta

if menor_ou_igual:
    Resposta = "Sim"
else:
    Resposta = "Não"
menor_ou_igual = Resposta

if maior_ou_igual:
    Resposta = "Sim"
else:
    Resposta = "Não"
maior_ou_igual = Resposta

# Exibição dos Calculos das Operações Comparativas
print("O valor de L é igual a H?", igual)
print("O valor de L é diferente de H?", diferente)
print("O valor de L é maior que H?", maior_que)
print("O valor de L é menor que H?", menor_que)
print("O valor de L é menor ou igual a H?", menor_ou_igual)
print("O valor de L é maior ou igual a H?", maior_ou_igual)

# Operadores Lógico (Lógica parecida com o Excel)
# AND = e
# OR = Ou
# NOT = Não é

# Criando Variável dos operadores lógicos
Calculo1 = L > 12 
Calculo2 = H < 12
Calculo3 = L < 12

# Personalização das Respostas
if Calculo1:
    Resposta = "Sim"
else:
    Resposta = "Não"
Calculo1 = Resposta

if Calculo2:
    Resposta = "Sim"
else:
    Resposta = "Não"
Calculo2 = Resposta

if Calculo3:
    Resposta = "Sim"
else:
    Resposta = "Não"
Calculo3 = Resposta

# Vou Personalizar "False" do "Not" para Sim ou Não.
Resultado = not L > 12 # dá False

if Resultado:
    Resposta = "Sim"
else:
    Resposta = "Não"
Resultado = Resposta

print("L é Maior do que 12 e H é menor do que 12?", Calculo1 and Calculo2) # Sim e Não, o que gera Resposta: "Não"
print("L é Menor do que 12 ou H é menor do que 12?", Calculo3 or Calculo2) # Não e Não, o que gera Resposta: "Não"
print("Não é verdade que L é maior do que 12?", Resultado) # É verdade, o que gera Resposta: "Falso" (Personalizado)
