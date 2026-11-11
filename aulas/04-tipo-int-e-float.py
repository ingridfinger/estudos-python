
# Aula 04 - Tipos de Dados: int e float

"""
TIPOS DE DADOS: int e float

int -> Número inteiro
O tipo int representa números inteiros, positivos, negativos ou zero.
Não possui casas decimais.
Exemplos: 10, -5, 0, 100


float -> Número de ponto flutuante
O tipo float representa números de ponto flutuante.
Pode representar valores com casas decimais, positivos, negativos ou zero.
Em Python, utilizamos ponto (.) como separador decimal,
e não vírgula.
Exemplos: 1.5, -2.7, 0.0, 10.0
"""

# 1. Utilizando o tipo int

print("Utilizando o tipo int:")
print(11)    # int positivo
print(-11)   # int negativo
print(0)     # int zero
print("\n")


# 2. Utilizando o tipo float

print("Utilizando o tipo float:")
print(1.1, 10.11)  # float positivo
print(0.0, -1.5)   # float zero e negativo
print("\n")


# 3. Utilizando a função type()

# A função type() mostra o tipo de dado de um valor ou variável.

print("Utilizando a função type():")
print(type("Ing"))  # str
print(type(0))      # int
print(type(11))     # int
print(type(-11))    # int
print(type(1.1))    # float
print(type(-1.1))   # float
print(type(0.0))    # float
print("\n")


# 4. Diferença entre int e float

# Mesmo que o valor seja matematicamente inteiro,
# se tiver o ponto decimal, será considerado float.

print("Comparando int e float:")
print(type(10))    # int
print(type(10.0))  # float