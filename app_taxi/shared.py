#shared.py
#Este modulo permite el envío de variables entre módulos
import logging

#Definir las variables a intercambiar entre módulos con un valor por defecto.
#El valor por defecto se necesita para que los otros modulos sean capaces de
#"ver" las variables.

usuario_activo = None
tarifa_parada = 0.02
tarifa_movimiento = 0.05
tarifa_parada_nocturna = tarifa_parada * 2
tarifa_movimiento_nocturna = tarifa_movimiento * 2