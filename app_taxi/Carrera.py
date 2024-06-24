import datetime

class Carrera:
    precio_parada = 0.02
    precio_movimiento = 0.05
    precio_parada_nocturno = precio_parada * 2
    precio_movimiento_nocturno = precio_movimiento * 2
    hora_inicio = 0
    hora_final =  0
    ID = 0
    tiempo_acumulado_parado = 0
    tiempo_acumulado_moviento = 0
    tipo_estado = {0: "parado", 1: "movimiento", 2:"otro"}
    estado = 0 
    tiempo_total = 0

    def __init__(self, tiempo, nombre_usuario, estado):
        self.ID = nombre_usuario
        self.tiempo = tiempo
        self.estado = estado
