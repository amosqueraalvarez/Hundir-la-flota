from nave import Nave
from casilla import Casilla

class Tablero:
    def __init__(self):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        por1 = Nave("Enterprise", "portaaviones", 5)
        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)
        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        self.casillero = [[Casilla() for _ in range(10)] for _ in range(10)]
        self.casillero[1][1].nave = por1
        self.casillero[1][2].nave = por1
        self.casillero[1][3].nave = por1


    def comprobar_impacto(self, x, y):
        casilla = self.casillero[x][y]
        return casilla.disparar()
