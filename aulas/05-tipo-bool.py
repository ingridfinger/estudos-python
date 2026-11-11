
# Aula 05 - Tipo de Dado: bool (boolean)

"""
TIPO DE DADO: bool (boolean)

O tipo bool representa valores booleanos, ou seja,
valores que possuem apenas duas possibilidades:

True  -> Verdadeiro
False -> Falso

Em programação, utilizamos valores booleanos para representar
respostas de condições e perguntas feitas pelo programa.

Existem vários operadores que permitem fazer essas comparações.

Um deles é o == (igualdade), que verifica se um valor
é igual a outro.

O resultado de uma comparação será sempre True ou False.
"""

# 1. Operador de igualdade (==)

# Verifica se os dois valores são iguais.

print("Utilizando o operador de igualdade:")

print(10 == 10)  # True -> Os valores são iguais.
print(10 == 11)  # False -> Os valores são diferentes.
print("\n")


# 2. Valores booleanos

# True e False são valores do tipo bool.
# Atenção: em Python, devem começar com letra maiúscula.

print("Valores booleanos:")

print(True)
print(False)
print("\n")


# 3. Utilizando a função type()

# A função type() mostra o tipo de dado de um valor.

print("Verificando o tipo bool:")

print(type(True))       # bool
print(type(False))      # bool
print(type(10 == 10))   # bool
print(type(10 == 11))   # bool
print("\n")


# 4. Outros operadores de comparação

# Além do ==, existem outros operadores que permitem
# comparar valores.

print("Outros operadores de comparação:")

print(10 != 5)  # Diferente de -> True
print(10 > 5)   # Maior que -> True
print(10 < 5)   # Menor que -> False
print(10 >= 10) # Maior ou igual a -> True
print(5 <= 3)   # Menor ou igual a -> False