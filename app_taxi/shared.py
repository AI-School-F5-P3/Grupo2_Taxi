#shared.py
import logging

usuario_activo = None

tarifa_parada = 0.02
tarifa_movimiento = 0.05
tarifa_parada_nocturna = tarifa_parada * 2
tarifa_movimiento_nocturna = tarifa_movimiento * 2