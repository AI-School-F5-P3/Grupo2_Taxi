import datetime

class Carrera:
    precio_parada = 0.02
    precio_movimiento = 0,.05
    precio_parada_nocturno = precio_parada * 2
    precio_movimiento_nocturno = precio_movimiento * 2
    hora_inicio = 0
    hora_final =  0
    ID = 0
    tiempo_acumulado_parado = 0
    tiempo_acumulado_moviento = 0


    def __init__(self, tiempo, ID):
        self._ID = ID
        self.tiempo = tiempo