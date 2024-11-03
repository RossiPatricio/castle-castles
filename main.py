from classes import *


lancelot = Caballero("Sir Lancelot", 100, 20, 20, 20, 100, 20, (0, 0))
shrek = Ogro("Shrek", 100, 20, 20, 20, 100, 20, (0, 0))

murcielago1 = Enemigo("Rick", 20, 5, 5, 5, 5, 10, (0, 0))

murcielago2 = Murcielago(20, (0, 0))

lancelot.ataque_especial(murcielago2)

