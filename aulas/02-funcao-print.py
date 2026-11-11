# Aula 02 - Função Print

# A função print() é utilizada para imprimir informações na tela.
# Por padrão, ela utiliza um espaço entre os argumentos
# e realiza uma quebra de linha ao final.

print(12, 34)
print(56, 78)


# É possível adicionar separadores utilizando o parâmetro sep.
# Podemos utilizar aspas simples ou duplas.

# O padrão do sep é um espaço (' ').
print(12, 34, sep=' ')

# Podemos remover o espaço entre os argumentos:
print(12, 34, sep="")

# Ou utilizar outro separador, como um traço:
print(56, 78, sep='-')


# CRLF / LF --> formas de representar uma quebra de linha.

# CRLF (Carriage Return + Line Feed) --> \r\n --> Windows
# LF (Line Feed) --> \n --> macOS e Linux

# \r --> retorna o cursor ao início da linha atual.
# \n --> avança o cursor para a próxima linha.


# END --> define o que será colocado ao final da impressão.
# Por padrão, seu valor é '\n', que realiza a quebra de linha.

# Com aspas vazias, não adicionamos nenhum caractere ao final.
# Assim, a próxima impressão continuará na mesma linha.

print(12, 34, end='')
print(56, 78)


# Podemos definir outro caractere para finalizar a impressão.
# Nesse caso, o símbolo # aparecerá entre as impressões.

print(12, 34, end="#")
print(56, 78)