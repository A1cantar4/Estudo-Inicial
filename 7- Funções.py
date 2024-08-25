# Vou criar uma função de exibir um texto
# "DEF" literalmente define algo para ser utilizado quando "chamado"

def básico():
    print("Olá Mundo!")

#só chamar a função
básico()

# Aqui tem a função em que é um parâmetro, que são as variáveis "locais", 
# que só funcionam dentro da função apenas.
def mensagem(nome):       
    print(f"Olá, {nome}! Parabéns pelo seu Aniversário.")

mensagem("Lucas") # Aqui será o Argumento (nome) que será utilizado no parâmetro


# Funções de retorno
def soma(L, H): # Parâmetros
    return L + H # Quando a função for chamada, vai retornar essa soma

resultado = soma(21, 22) # Aqui sao os Argumentos passados para o parâmetro
print("Resultado da Soma", resultado) # Vai ser 43

# Pode ser escrita também com os argumentos sendo constantes
L = 21
H = 22
M = 12

def soma(L, H, M):
    return L + H + M

resultado = soma(L, H, M)
print("Resultado da Soma", resultado)

# Função com Argumento Padrão:
L = "Lucas"
A = "Alcântara"

def mensagem(nome="Camarada", sobrenome="Guerreiro"):
    print(f"Olá, {nome} {sobrenome}! Seja Bem-vindo a nossa taverna!")

mensagem()
# "mensagem(L, A)"
# Quando o argumento for nulo, será utilizado o padrão, do contrário, será o argumento chamado.
