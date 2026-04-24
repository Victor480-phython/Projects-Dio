# List

fruits = ["Orange", "Strawberry", "Apple", "Grapes"]

fruit = []

letters = list("python")

numbers = list(range(10))

car = ["Ferrari", 
       "F8",
         4200000,
           2020,
             2900,
               "São Paulo",
                 True
                 ]
fruits[0] # Orange
fruits[1] # Strawberry
fruits[2] # Apple
fruits[-1] # Grapes
fruits[-3] # Strawberry

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2] first line
matriz[0][0] # 1 first line and first element
matriz[0][-1] # 2 first line and last element
matriz[-1][-1] # "c", last line and last element

# Other exemples

lista = ["p", "y", "t", "h", "o", "n"]
#  Always remember, that the final position every less 1 for instance 2:3, the position 3 is "h" but less 1 is "t"
lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"] 


cars = ["Gol", "Fiesta", "bmw"]

for car in cars:
    print(car)


numbers = [1,20, 21, 2, 9, 65, 34]
pairs = []

# filter version 1
for number in numbers:
    if number % 2 == 0:
        pairs.append(number)
# filter version 2 comprehension
numbers = [1,20, 21, 2, 9, 65, 34]
pairs = [number for number in numbers if number % 2 == 0]

# modifiyng the values
numbers = [1,20, 21, 2, 9, 65, 34]
quarter = []
for number in numbers:
    quarter.append(number ** 2)


# Inserting more element inside the list
lista = []

lista.append(1)
lista.append("Python")
lista.append([10, 120, 124])

print(lista)
l2 = lista.copy()

# Comand clear
lista.append([10, 120, 124])
lista.clear()
print(lista)    # []

# Return the same list, but with a different instance
lista.copy()
# For instance, we've this
# To show the List's ID
print(id(l2), 
      print(id(lista))
      )

# To alternate something inside the list and to show how this happen, look this
l2[0] = 2
print(l2)
print(lista)
# String, int, float and boolean





# Function count
# ---------------------------------------------------------------------------------------------------------
colors = ["Red", "Red", "Red", "Red", "Blue", "Green", "White", "Gray", "Black"]

colors.count("Red")
colors.count("Green")
colors.count("Blue")
colors.count("White")
colors.count("Gray")
colors.count("Black")
# ---------------------------------------------------------------------------------------------------------

# Append insert only one element, but we've other side to do the same thing easily
# .extend // for Instance

language = ["Python", "R", "C#"]

language.extend(["js", "Rust", "Java", "Powershell", "SQL", "Julia"])
print(language)

# If you've more than one occurence//object, the function will captch the first occurence
# If you know what is the object's index, you'll use the function .index
print(language.index("Python")) # 0
print(language.index("Powershell")) # 6
print(language.index("R")) # 1
print(language.index("SQL")) # 7



# The python behave like a stake of dishes the last is the first and the first is the last, look this
# Return to the other example, .extend

print(language.pop()) # Julia
print(language.pop()) # SQL
print(language.pop()) # Powershell
print(language.pop()) # Java
print(language.pop(0)) # Python ------> because i put 0 to the instance to catch the first


#----------------------------------------------------------------------------------------------------------
# Function .remove
# Instead of the object's index, you need to use the object
print(language.remove("Julia"))

# list Transposition
print(language.reverse())

# To order by alphabetic form A-Z
print(language.sort())

# To order by alphabetic form Z-A
print(language.sort(reverse=True))

# Order by word's lenght
# The lambda is a anonymous function
# For each item, execute the nex code ------> len(x)
# The function len() transform in a int
# The little to the big word, ordered by the lenght, transformed in a int number
print(language.sort(key=lambda x: len(x)))

# This happen to reverse form
print(language.sort(key=lambda x: len(x)), reverse=True )

# To discover the lenght of the list we've use the function len(x)
print(len(language))


# function to order iterables
sorted(language, key=lambda x: len(x))

sorted(language, key=lambda x: len(x), reverse=True)

# ---------------------------------------------------------------------------------------------------------
