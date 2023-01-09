# # Задана 4
import re
a = str(input("Введіть строку:"))
print(f"Було так:{a}")
def check (a:str)->str:
     char = "".join(re.split("[^a-z]*", a))
     return char

print("Стало так:",check(a))

# Задача 1
a = 5
b = 15
c = 10
def check (a:int, b:int, c:int)->int:
     if c > a and c < b:
          print("Число в діапозоні")
     else:
          print("Число не в діапозоні")
     return False

print(check(a,b,c))