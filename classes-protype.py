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
    pass

  def recibir_daño(self, cantidad):
    self.salud -= cantidad

class Heroe(Entidad):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo)
    self.tipo = tipo
  # Personaje principal
  # Controlado por el jugador
  def moverse(self, x, y):
    super().moverse(x, y)
    # implementar un sistema para que se mueva por eventos de teclado
    pass
  
  def habilidad_especial(self):
    # Varia depende la clase de heroe
    pass
    
  def ataque_especial(self):
    # Varia depende la clase de heroe y esta disponible con la energia al maximo
    # <------------
    pass

class Caballero(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Caballero")

class Ogro(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Ogro")

class Mago(Heroe):
  def __init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion):
    super().__init__(self, nombre, salud, ataque, fuerza, defensa, energia, velocidad, posicion, tipo= "Mago")