class Entidad:
  def __init__(self, nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion):
    self.nombre = nombre
    self.salud = salud
    self.daño = daño
    self.fuerza = fuerza
    self.defensa = defensa
    self.energia = energia
    self.velocidad = velocidad
    self.posicion = posicion
    self.estado = "Alive"

  def moverse(self, x, y):
    pass

  def recibir_daño(self, cantidad):
    self.salud -= cantidad
    if self.salud <= 0:
      self.estado = "Dead"
      print(f"{self.nombre} ha muerto.")



class Heroe(Entidad):
  # Es controlado por el jugador
  def __init__(self, nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion, tipo):
    super().__init__(nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion)
    self.tipo = tipo

  def ataque(self, victima):
    if victima.estado == "Alive":
      victima.recibir_daño(self.daño)

  def ataque_especial(self, victima):
    if victima.estado == "Alive" and self.energia == 100:
      print(f"{self.nombre} lanza ataque especial a la victima")
      victima.recibir_daño(self.daño * 1.5)


class Caballero(Heroe):
  def __init__(self, nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion, tipo= "Caballero")



class Enemigo(Entidad):
  # Tiene movimientos preestablecidos
  def __init__(self, nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion)

class Murcielago(Enemigo):
  def __init__(self, salud, posicion):
    nombre= "Murcielago"
    daño= 20
    fuerza= 20
    defensa= 20
    energia= 100
    velocidad= 20
    super().__init__(nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion)