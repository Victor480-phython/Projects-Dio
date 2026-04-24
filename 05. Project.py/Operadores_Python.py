preco = 10
print(preco)
# >>>> 10

preco = float(preco)
print(preco)
# >>>> 10.0

preco = 10/2
print(preco)
# >>>> 5.0

preco = 10.30
print(preco)
# >>>> 10.30

preco = int(preco)
print(preco)
# >>>> 10

# Agora vamos analisar como seria uma variável inteira ou numerica geral sendo dividida

preco = 10
print(preco)
# >>> 10

# Float numeric - divisão com decimal
print(preco / 2)
# >>> 5.0

# Int numeric - divisão inteira
print(preco // 2)
# >>> 5

# Módulo
print(10 % 3)
# >>> 1

# Exponenciação
print(2 ** 3)
# >>> 8

saldo = 450
saque = 300

print(saldo == saque)
# >>> False
print(saldo != saque)
# >>> True

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo < saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo <= saque)

idade = 20
print(f"Eu tenho {idade} anos")

saldo = 200

saldo +=300

print(saldo)

saldo = 500
saldo %=480
# O resultado dessa operação é o resto da divisão que dá 20

saldo = 80
saldo **= 2
# Aqui é um caso de exponenciação que elevado ao quadrado resultará em 6400





# Identação em Python como funciona?
def sacar(self, valor: float) -> None: #inicio do bloco método
    if self.saldo >= valor: #inicio do bloco do if
        self.saldo -= valor
   
    # fim do bloco if

# fim do bloco do método

# esse def é para definir um método e o método é sacar algum valor
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro no caixa eletrônico") # esses dois prints fazem parte do if
    
    print("obrigado por ser nosso cliente, tenha um bom dia!") # Essa mensagem faz parte do método


# a identação precisa ser assim
def depositar(valor):
    saldo = 500
    saldo += valor

# JEITO ERRADO DE IDENTAÇÃO
#def depositar(valor):
#saldo = 500
#saldo += valor



sacar(100)



# CONDITIONAL STRUCTURE

# if/if-else/elif
saldo = 2000.0
saque = float(input("informe o valor do Saque: "))

if saldo >= saque:
    print("Realizando Saque")
else:
    print("Saldo Insuficiente!")

if saldo >= saque:
    print("Realizando Saque!")

if saldo<= saque:
    print("Saldo Insuficiente!")



opcao = int(input("Informe uma Opção: [1] Sacar \n[2] Extrato "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    SystemExit("Opção Inválida")



# if aninhado

# Variables in initial form to create a bank system
normal_account = True
balance = 2500
withdrawal = 500
overdraft = 450
university_account = False
special_account = True

# Main Logic
if normal_account:
    if balance >= withdrawal:
        print("Successfully Withdrawal!")
    elif withdrawal <= (balance + overdraft):
        print("Withdrawal Executed by Overdraft!")
    else:
        print("It wasn't possible to realize your Withdrawal!")
elif university_account:
    if balance >= withdrawal:
        print("Successfully Withdrawal!")
    else:
        print("Insuficient Balance!")
elif special_account:
    print("Special Account Selected")
else:
    print("The system didnt recognize your account type, please contact your manager")

#if ternário
balance = 2000
withdrawal = 500

status = "Successfully" if balance >= withdrawal else "Fail"
print(f"{status} to Realize the Withdrawal")
# This f in the function serves to put {} inside the function print() to concat this

# LOOPING STRUCTURES
# for//while

# Receive one number's keyboard and show the following numbers
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

text = input("Report a text: ")

VOWELS = "AEIOU" # Constant


# Exemple using looping iteraling
for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print() # Add a break line
    print("executes in the end of the loop")



# RANGE
# Range(stop) -> range object
# Range(start, stop[, step]) -> range object

list(range(4))
[0, 1, 2, 3]

for number in range(0, 11):
    print(number, end=" ")

#Exemple showing built-in range
# Exibindo a tabuada do 5
for number in range(0, 51, 5):
    print(number, end=" ") # Here forces a special character
# (0, 51, 5) --> 1 - start // 2 - end // 3 - step
    print(number) # Here brake lines



# WHILE
option = -1

while option != 0:
    option = int(input("[1] Withdrawal \n[2] Statement \n[0] Exit \n: "))
   
    if option == 1:
         print("Withdrawing...")
    elif option == 2:
         print("Showing the Statement...")
else:
    print("Thank you for using our bank system, it was a pleasure to have you as our client, See you next time")



option = -1

while option != 0:
    option = int(input("report a number: "))

    if option >= 10:
        break

    print(option)


while True:
    number = int(input("report a number: "))

    if number == 10:
        break # Stop the code here

    print(number)

for number in range(100):
    if number == 12:
        continue # Ignore the number 12 and continue the code
    print(number, end=" ")



# Strings Múltiplas

name = "Victor"

message = f"""
Hello, my name is {name} , 
and i'm learning Python
"""

# Preservação de espaços
name = "Victor"

message = f'''
  Hello, my name is {name}
I'm Learning Python
     This message has different recoil
'''
 
 
print(message)

print("""
      ============================= MENU =============================
      1 - Withdrawal
      2 - Deposit
      3 - Exit
      ================================================================

                      Thanks to use our system!
""")