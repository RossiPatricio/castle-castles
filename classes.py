class Entidad:
    def __init__(self, nombre, salud, daño, fuerza, energia, velocidad, posicion):
        self.nombre = nombre
        self.salud = salud
        self.daño = daño
        self.fuerza = fuerza
        self.energia = energia
        self.velocidad = velocidad
        self.posicion = posicion  # Posición ahora es una tupla (x, y, z)
        self.estado = "Alive"

    def moverse(self, x, y, z):
        # Actualiza la posición en los tres ejes
        self.posicion = (self.posicion[0] + x, self.posicion[1] + y, self.posicion[2] + z)
        print(f"{self.nombre} se ha movido a la posición {self.posicion}")

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        if self.salud <= 0:
            self.estado = "Dead"
            print(f"{self.nombre} ha muerto.")


class Heroe(Entidad):
    # Controlado por el jugador
    def __init__(self, nombre, salud, daño, fuerza, energia, velocidad, posicion, tipo):
        super().__init__(nombre, salud, daño, fuerza, energia, velocidad, posicion)
        self.tipo = tipo

    def accion(self):
        # Interactuar con el entorno
        pass

    def curarse(self):
        # Curar al héroe
        pass

    def moverse(self, direccion):
        # Movimiento con teclas W, A, S, D para el plano X-Y y Space/Ctrl para subir/bajar en el eje Z
        movimientos = {
            'W': (0, 1, 0),   # Adelante en el eje Y
            'A': (-1, 0, 0),  # Izquierda en el eje X
            'S': (0, -1, 0),  # Atrás en el eje Y
            'D': (1, 0, 0),   # Derecha en el eje X
            'Space': (0, 0, 1),  # Subir en el eje Z
            'Ctrl': (0, 0, -1)   # Bajar en el eje Z
        }
        if direccion in movimientos:
            desplazamiento = movimientos[direccion]
            super().moverse(*desplazamiento)
        else:
            print(f"Dirección {direccion} no válida.")

    def ataque(self, victima):
        if victima.estado == "Alive":
            victima.recibir_daño(self.daño)
            self.energia -= 10

    def ataque_especial(self, victima):
        if victima.estado == "Alive" and self.energia >= 100:
            print(f"{self.nombre} lanza ataque especial a {victima.nombre}")
            victima.recibir_daño(self.daño * 1.5)
            self.energia -= 100  # Usa toda la energía


class Caballero(Heroe):
    def __init__(self, nombre, salud, daño, fuerza, energia, velocidad, posicion):
        super().__init__(nombre, salud, daño, fuerza, energia, velocidad, posicion, tipo="Caballero")


class Enemigo(Entidad):
    # Movimientos preestablecidos
    def __init__(self, nombre, salud, daño, fuerza, energia, velocidad, posicion):
        super().__init__(nombre, salud, daño, fuerza, energia, velocidad, posicion)

    def moverse_hacia(self, objetivo):
        # Moverse hacia una posición objetivo en el espacio 3D
        if self.estado == "Alive":
            dx = objetivo.posicion[0] - self.posicion[0]
            dy = objetivo.posicion[1] - self.posicion[1]
            dz = objetivo.posicion[2] - self.posicion[2]
            # Priorizar movimiento en el eje más distante
            if abs(dx) > abs(dy) and abs(dx) > abs(dz):
                paso_x = 1 if dx > 0 else -1
                self.moverse(paso_x, 0, 0)
            elif abs(dy) > abs(dz):
                paso_y = 1 if dy > 0 else -1
                self.moverse(0, paso_y, 0)
            else:
                paso_z = 1 if dz > 0 else -1
                self.moverse(0, 0, paso_z)


class Murcielago(Enemigo):
    def __init__(self, salud, posicion):
        nombre = "Murcielago"
        daño = 20
        fuerza = 20
        energia = 100
        velocidad = 20
        super().__init__(nombre, salud, daño, fuerza, energia, velocidad, posicion)

    def patrullar(self, heroe):
        # Perseguir al héroe si está cerca (por ejemplo, a menos de 10 unidades en 3D)
        distancia = ((heroe.posicion[0] - self.posicion[0]) ** 2 + (heroe.posicion[1] - self.posicion[1]) ** 2 + (heroe.posicion[2] - self.posicion[2]) ** 2) ** 0.5
        if distancia < 10:
            print(f"{self.nombre} está persiguiendo al héroe.")
            self.moverse_hacia(heroe)
        else:
            print(f"{self.nombre} está patrullando.")

