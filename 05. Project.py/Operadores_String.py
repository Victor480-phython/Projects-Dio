
# Maiúscula, Minúscula e título
curso = "pYtHon"
# Maiúscula
print(curso.upper())
# Minúscula
print(curso.lower())
# Título
print(curso.title())


# -------------------------------------------------------

# Eliminando Espaços
curso = "      Python "

# Elimina os espaços em branco da direita e da Esquerda(both)
print(curso.strip())

# Elimina os espaços em branco da Esquerda(left)
print(curso.lstrip())

# Elimina os espaços em branco da direita(right)
print(curso.rstrip())


# --------------------------------------------------------

# Junções e centralizações

curso = "Python"
# Centraliza concatenando o # e preservando os 10 caracteres
print(curso.center(10, "#"))
# "." String é iterável, logo o "." vai entre as letras
print(".".join(curso))

# Interpolação de variáveis Old style %
name = "Victor"
age = 20
job = "Data Scientist"
language = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (name, age, job, language))
print("Name: %s Age: %d" % (name, age))


# New style - Méthod format
people = {
    "name": "Victor",
    "age": 20,
    "job": "Data Scientist",
    "language": "Python"
}
print("Hello, I'm {}. I'm 20 years old, i work as {} and i'm enrolled at {} course.".format(name, age, job, language))

print("Hello, I'm {3}. I'm {2} years old, i work as {1} and i'm enrolled at {0} course.".format(language, job, age, name))

print("Hello, I'm {name}. I'm {age} years old, i work as {job} and i'm enrolled at {language}.".format(name=name, age=age, job=job, language=language))

# pessoa = {"name": "Victor", "Age": 20, "job": "Data Scientist", "language": "Python"}
print("Hello, I'm {name}. I'm {age} years old, i work as {job} and i enrolled at {language}.".format(**people))

# f-string method (Best method in my opinion)
print(f"Hello, I'm {name}. I'm {age} years old, i work as {job} and i'm enrolled at {language} course.")

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")

print(f"Valor de PI: {PI:10.2f}")

name = "Victor Nicolas Mateus dos Santos"

name[0]

# Ele conta até o 6 e faz menos 1 começando do 0
# Não informei o Start mas informei o end
name[:6]

# Não informei o End mas informei o Start
name[6:]

# Start and End
name[8:7]

# O Step serve como se fosse a razão de uma P.A ou P.G
name[8:7:2]

# Nome completo
name[:]

# Inverte o nome
name[::-1]
