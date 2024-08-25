# Vou criar uma String para Aplicar as Condicionais
Valor = 15

# IF = "Se" (Assim como Excel)
# ELIF = Caso IF for False, ele verifica o ELIF.
# ELSE = Caso todas condições forem False, executa o ELSE.

# Condicional para Verificar qual tipo de número inteiro o string é!
if Valor > 0:
    print("O Valor é Positivo!")
elif Valor == 0:
    print("O Valor é Nulo!")
else:
    print("O Valor é Negativo!")
# Aqui ele verifica somente o IF, pois é TRUE!

# Condicional para Verificar a Grandeza do Valor!
if Valor < 0:
    print("O Valor é Menor do que zero!")
elif Valor == 0:
    print("O Valor é Igual do que zero")
else:
    print("O Valor é Maior do que zero!")
# Aqui ele verifica tanto o IF, quanto o ELIF e da false, então ele executa a mensagem do ELSE.
