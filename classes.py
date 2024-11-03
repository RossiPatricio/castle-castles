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
    ...

  def recibir_daño(self, cantidad):
    self.salud -= cantidad
    if self.salud <= 0:
      self.estado = "Dead"

class Heroe(Entidad):
  # Personaje principal
  def __init__(self, nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion, tipo):
    super().__init__(nombre, salud, daño, fuerza, defensa, energia, velocidad, posicion)
    self.tipo = tipo

  # Controlado por el jugador
  def moverse(self, x, y):
    super().moverse(x, y)
    # implementar un sistema para que se mueva por eventos de teclado
    ...

  def ataque(self, victima):
    if victima.estado == "Alive":
      victima.recibir_daño(self.daño)
  
class Caballero(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Caballero")


class Ogro(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Ogro")

class Mago(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Mago")



class Enemigo(Entidad):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion)
