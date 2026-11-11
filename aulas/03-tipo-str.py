
# Aula 03 - Tipos de Dados: String (str)

"""
DOCSTRING

Python é uma linguagem de programação que possui tipagem dinâmica e forte.

Tipagem dinâmica:
O Python identifica automaticamente o tipo de dado de uma variável.
Não precisamos declarar previamente se ela será uma string, um inteiro,
um número decimal, etc.

Tipagem forte:
O Python não realiza conversões automáticas entre tipos incompatíveis
em determinadas operações. Por exemplo, não podemos somar diretamente
uma string com um número inteiro.

str -> string -> texto

Strings são sequências de caracteres utilizadas para representar textos.
Em Python, podem ser escritas utilizando aspas simples ou aspas duplas.
"""

# 1. Aspas simples

print('Utilizando aspas simples:')
print('Ing')

# Podemos utilizar aspas duplas dentro de uma string com aspas simples.
print('Hello "Kitty"')
print('\n')

# 2. Aspas duplas

print("Utilizando aspas duplas:")
print("Ing")

# Podemos utilizar aspas simples dentro de uma string com aspas duplas.
print("My 'Melody'")
print('\n')

# 3. Caractere de escape (\)

# A barra invertida (\) é utilizada como caractere de escape.
# Ela permite representar caracteres especiais dentro de uma string.

# \" permite exibir aspas duplas dentro de uma string delimitada
# também por aspas duplas.
print("Ing \"Ing\"")

# Outros exemplos de caracteres de escape:
print("Primeira linha\nSegunda linha")  # \n -> quebra de linha
print("Nome:\tIngrid")                  # \t -> tabulação
print("Caminho: C:\\Users\\Ingrid")     # \\ -> exibe uma barra invertida
print('\n')

# 4. Strings raw (r)

# O prefixo r antes das aspas cria uma raw string.
# Nela, as barras invertidas são interpretadas literalmente,
# em vez de funcionarem como caracteres de escape.

print(r"Hello \"Kitty\"")
print(r"C:\Users\Ingrid\Documents")