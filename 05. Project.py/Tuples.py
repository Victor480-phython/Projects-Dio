# What is Tuples
fruits = ("Orange", "Apple", "Grapes",)

letters = tuple("python")

numbers = tuple([1, 2, 3, 4])

country = ("Brasil",)


# Eliminar duplicidade de uma lista
# Não confiar na ordem que o set for passar
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("Pinneaple") # {"i, n, a, p, l, e"}

set(("Palio", "Gol", "celta", "Palio")) # {"Gol", "Celta", "Palio"}

Languages = {"Python", "Java", "Python"}
print(Languages)

# Union
conjunt_a = {1, 2}
conjunt_b = {3, 4}
conjunt_a.union(conjunt_b) # {1, 2, 3, 4}


# Intersection
conjunt_a = {1, 2}
conjunt_b = {3, 4}
conjunt_a.intersection(conjunt_b) # {2, 3}

# Difference
conjunt_a = {1, 2}
conjunt_b = {3, 4}
conjunt_a.difference(conjunt_b) # {1}
conjunt_b.difference(conjunt_a) # {4}

# symmetric_difference
conjunt_a = {1, 2}
conjunt_b = {3, 4}
conjunt_a.symmetric_difference(conjunt_b) # {1, 4}

# Issubset
conjunt_a = {1, 2, 3}
conjunt_b = {4, 1, 2, 5, 6, 3}

conjunt_a.issubset(conjunt_b) # True
conjunt_b.issubset(conjunt_a) # False

# Issuperset
conjunt_a = {1, 2, 3}
conjunt_b = {4, 1, 2, 5, 6, 3}

conjunt_a.issuperset(conjunt_b) # False
conjunt_b.issuperset(conjunt_a) # True


# Isdisjoint
conjunt_a = {1, 2, 3, 4, 5}
conjunt_b = {6, 7, 8, 9}
conjunt_c = {1, 0}

conjunt_a.isdisjoint(conjunt_b) # True
conjunt_a.isdisjoint(conjunt_c) # False


# Element add --------> if doesn't exist, add a new element
Group = {1, 23}
Group.add(25)
Group.add(25)
Group.add(27)

# Clear
Group = {1, 23}
Group.clear()

# Copy
Group = {1, 23}
Group.copy()

# Discard
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numbers # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numbers.discard(1)
numbers.discard(45)
numbers # {2, 3, 4, 5, 6, 7, 8, 9, 0}

# pop
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numbers # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numbers.pop() # 0
numbers.pop() # 1
numbers # {2, 3, 4, 5, 6, 7, 8, 9}

# Remove
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numbers # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numbers.remove(0) # 0
numbers # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# Dicionário é um conjunto não ordenado de pares, chaves e valor, onde as chaves são únicas dado em uma dada instância
# Dicionários são delimitados por {}, e contém uma lista de pares chave: valor separada por vírgulas
telephone = {"333-1234"}

People = {"name": "Victor", "Age": 20}

People = dict(name="Victor", age=20)

People[telephone] = "333-1234"

data = {"name": "Victor", "Age": 20, "Telephone": "333-1234"}

data["name"]
data["Age"]
data["Telephone"]

data["name"] = "Maysa"

data["Age"] = 21

data["Telephone"] = "429981781"

data


# Dicionário aninhado

contacts = {
    "supergamers7777@gmail.com": {"name": "Victor", "Telephone": "42998666260"},
    "May123@gmail.com": {"name": "Maysa", "Telephone": "42998265240"},
    "Bianca123@gmail.com": {"name": "Bianca", "Telephone": "42998226261"},

}

contacts["Bianca123@gmail.com"]["Telephone"]

for key in contacts:
    print(key, contacts[key])

for key, value in contacts.items():
    print(key, value)

copy = contacts.copy()

copy["supergamers7777@gmail.com"] = {"name": "Victor"}

contacts["Bianca123@gmail.com"] # {"name": "Victor", "Telephone": "42998666260"}

copy["supergamers7777@gmail.com"] # {"name": "Victor"}

# Quando você quiser criar um dicionário e não adicionar nada

dict.fromkeys(["name","Telephone"])

# Cria chave e coloca um valor padrão nela
dict.fromkeys(["name","Telephone"],"vazio")



# Get serve para muitas coisas, entre elas, saber se uma chave existe dentro do dicionário

contacts.get("chave")
# Aqui diz, tenta buscar a chave, se não me retorna dicionário vazio
contacts.get("chave", {})
contacts.get("supergamers7777@gmail.com", {})

# Items retorna uma lista de tuplas
# quando quer fazer for e iterar sobre os valores do dicionário
contacts.items()

# keys retorna só as chaves
contacts.keys()

# o setdefault serve para caso se a chave não exista ele defina um valor para ela por exemplo

contact = {"name": "Victor", "Telephone": "3333-1234"}

contact.setdefault("name", "Victor")
print(contact)

contact.setdefault("Idade", 28)
print(contact)

contact = {"name": "Victor", "Telephone": "3333-1234"}
# Update
contact =  {  
    {"name": "Victor", "Telephone": "3333-1234"}
}

contact.update({"May123@gmail.com": {"name": "May"}})

contact.update({"May123@gmail.com": {"name": "May", "Telephone": "12232242113"}})

lista_chaves: list = contacts.keys()



def exibir_mensagem():
    print("Hello World")

#Aqui está recebendo um argumento e como ele não existe ainda, foi definido isso lá em baixo
def exibir_mensagem_2(name):
    print(f"Welcome {name}!")

def exibir_mensagem_3(name="Victor"):
    print(f"Welcome {name}!")

exibir_mensagem()
exibir_mensagem_2(name="Victor")
exibir_mensagem_3()



# New function
def calcular_total(numbers):
    return sum(numbers)

def retorna_antecessor_e_sucessor(number):
    antecessor = number - 1
    sucessor = number + 1
    return antecessor, sucessor

calcular_total([10, 20, 34])

retorna_antecessor_e_sucessor(10)

def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# os astericos dizem que eu to criando um dicionário para armazenar na função
salvar_carro(**{"marca": "Fiat", "modelo":"Palio", "ano":1999, "placa": "ABC-1234"})

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beatiful is better than ugly.", autor="Tim Peters", ano=1999)

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)
