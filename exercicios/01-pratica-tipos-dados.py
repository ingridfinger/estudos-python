# EXERCÍCIO 01 - PRATICANDO TIPOS DE DADOS

"""
Objetivo:
Praticar os conceitos aprendidos nas aulas sobre os tipos
de dados String (str), Inteiro (int), Ponto Flutuante (float)
e Booleano (bool).

DESAFIO:

1. Crie variáveis para armazenar as seguintes informações:
   - Seu nome;
   - Sua cidade;
   - Sua idade;
   - Sua altura;
   - Se você está estudando Python atualmente.

2. Utilize a função print() para exibir todas as informações
   de forma organizada.

3. Utilize a função type() para descobrir e exibir o tipo
   de dado de cada variável.

4. Crie pelo menos duas comparações utilizando operadores
   relacionais (como ==, !=, >, <, >= ou <=).

5. Exiba os resultados das comparações e observe os valores
   booleanos retornados pelo Python (True ou False).

✨ Desafio extra:
Organize a saída do programa para que as informações
sejam exibidas de maneira bonita e fácil de entender.
"""

# 1. Variáveis para armazenamento de informações
nome = "Ing"
cidade = "São Paulo"
idade = 23
altura = 1.74
estudaPython = True

# 2. print() para exibir todas as informações
# print("Nome: ", nome)
# print("Cidade: ", cidade)
# print("Idade: ", idade)
# print("Altura: ", altura)
# print("Estuda Python? ", estudaPython)

print("Nome: ", nome,"\n", "Cidade: ", cidade, "\n", "Idade: ", idade, "\n", "Altura: ", altura, "\n", "Estuda Python?", estudaPython)
print("\n")

# 3. Utilizando a função type()
print(type(nome), type(cidade), type(idade), type(altura), type(estudaPython))
print("\n")

# 4. Crie pelo menos duas comparações utilizando operadores relacionais (como ==, !=, >, <, >= ou <=).
maioridade = idade > 18
alta = altura >= 1.80

# 5. Exiba os resultados das comparações e observe os valores booleanos retornados pelo Python (True ou False)
print("É maior de idade?", maioridade)
print("Tem mais de 1,80m?", alta)
