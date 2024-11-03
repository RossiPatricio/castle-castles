class Entidad:
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    self.nombre = nombre
    self.salud = salud
    self.ataque = ataque
    self.fuerza = fuerza
    self.defensa = defensa
    self.energia = energia
    self.velocidad = velocidad
    self.posicion = posicion

  def moverse(self, x, y):
    ...

  def recibir_daño(self, cantidad):
    self.salud -= cantidad

class Heroe(Entidad):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion)
    self.tipo = tipo
  # Personaje principal
  # Controlado por el jugador
  def moverse(self, x, y):
    super().moverse(x, y)
    # implementar un sistema para que se mueva por eventos de teclado
    ...
  
  def habilidad_especial(self):
    # Varia depende la clase de heroe
    ...
    
  def ataque_especial(self):
    # Varia depende la clase de heroe y esta disponible con la energia al maximo
    # <------------
    ...

class Caballero(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Caballero")

class Ogro(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Ogro")

class Mago(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Mago")