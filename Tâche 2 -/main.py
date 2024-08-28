# Python
x = int(input("Entrer un nombre : "))
y = int(input("Entrer une puissance : "))

def puissance(x,y):
  return x**y

print(f"{x} à la puissance {y} est egal à : {puissance(x,y)}")