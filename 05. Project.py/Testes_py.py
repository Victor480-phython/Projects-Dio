# Transformar número para String
preco = 10.50
idade = 28

print(str(preco))
# >>> 10.5
print(str(idade))
# >>> 28

# o f ta dizendo que vai inserir variáveis na dentro da string 
# pra concatenar define a string, coloca o f no começo e coloca entre chaves o nome da variável a se concatenar
texto = f"idade {idade} preco {preco}"
print(texto)
# idade 28 preco 10.50

# Dá para inverter também
preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

# Esse type pergunta o tipo da classe do objeto
print(type(str(10.10)))
# Inserção de Input
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
# caractere para quebra de linha é: \n


print(nome, idade)
print(nome, idade, end="...\n")


# Fórmula com Espaço
print("1" " " "guilherme")

# Inteiro
print(1 + 10)

# Float
print(1.5 + 1.5)

# booleano
print(True)
print(False)

#Tipos numéricos
int()

float()

str()

bool()
# Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento,
# Retorna uma lista de atributos válidos para o objeto
age = 23
name = 'Victor'
print(f'Meu nome é {name} e eu tenho {age} anos de idade')


STATES = [
   'SP',
   'RJ',
   'MG',
]