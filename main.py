from classes import *


lancelot = Caballero("Sir Lancelot", 100, 20, 20, 20, 50, 20, (0, 0))
murcielago = Enemigo("Rick", 20, 5, 5, 5, 5, 10, (0, 0))

print(murcielago.salud)
lancelot.ataque(murcielago)
print(murcielago.salud)

