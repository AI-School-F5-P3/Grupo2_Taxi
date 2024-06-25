import unittest
from unittest.mock import patch, MagicMock
import datetime
import pytz


from app_taxi.servicio import Tiempo, Tarifa, Carrera

class TestTiempo(unittest.TestCase):

    @patch('datetime.datetime')
    def test_reiniciar(self, mock_datetime):
        mock_now = datetime.datetime(2024, 6, 25, 15, 30, tzinfo=pytz.timezone('Europe/Madrid'))
        mock_datetime.now.return_value = mock_now
        tiempo = Tiempo()
        self.assertEqual(tiempo.inicio_tiempo, mock_now)

        new_mock_now = datetime.datetime(2024, 6, 25, 16, 30, tzinfo=pytz.timezone('Europe/Madrid'))
        mock_datetime.now.return_value = new_mock_now
        tiempo.reiniciar()
        self.assertEqual(tiempo.inicio_tiempo, new_mock_now)

    @patch('datetime.datetime')
    def test_tiempo_transcurrido(self, mock_datetime):
        inicio_tiempo = datetime.datetime(2024, 6, 25, 15, 30, tzinfo=pytz.timezone('Europe/Madrid'))
        mock_datetime.now.return_value = inicio_tiempo
        tiempo = Tiempo()
        
        later_tiempo = datetime.datetime(2024, 6, 25, 15, 35, tzinfo=pytz.timezone('Europe/Madrid'))
        mock_datetime.now.return_value = later_tiempo
        self.assertEqual(tiempo.tiempo_transcurrido(), 300)

    @patch('datetime.datetime')
    def test_es_nocturno(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2024, 6, 25, 23, 0, tzinfo=pytz.timezone('Europe/Madrid'))
        tiempo = Tiempo()
        self.assertTrue(tiempo.es_nocturno())
        
        mock_datetime.now.return_value = datetime.datetime(2024, 6, 25, 14, 0, tzinfo=pytz.timezone('Europe/Madrid'))
        tiempo = Tiempo()
        self.assertFalse(tiempo.es_nocturno())

class TestTarifa(unittest.TestCase):

    def test_calcular_costo(self):
        tarifa = Tarifa()
        self.assertEqual(tarifa.calcular_costo(100, 0, False), 2)
        self.assertEqual(tarifa.calcular_costo(100, 1, False), 5)
        self.assertEqual(tarifa.calcular_costo(100, 0, True), 4)
        self.assertEqual(tarifa.calcular_costo(100, 1, True), 10)

class TestCarrera(unittest.TestCase):

    @patch('tu_archivo.Tiempo')
    def test_actualizar_costo(self, MockTiempo):
        mock_tiempo = MockTiempo.return_value
        mock_tiempo.tiempo_transcurrido.return_value = 100
        mock_tiempo.es_nocturno.return_value = False
        
        carrera = Carrera(1)
        carrera.estado = 0
        self.assertEqual(carrera.actualizar_costo(), 2)
        self.assertEqual(carrera.precio_total, 2)
        self.assertEqual(carrera.tiempo_acumulado_parado, 100)
        
        mock_tiempo.tiempo_transcurrido.return_value = 200
        carrera.estado = 1
        self.assertEqual(carrera.actualizar_costo(), 10)
        self.assertEqual(carrera.precio_total, 12)
        self.assertEqual(carrera.tiempo_acumulado_movimiento, 200)

    @patch('tu_archivo.Tiempo')
    def test_parada(self, MockTiempo):
        mock_tiempo = MockTiempo.return_value
        carrera = Carrera(1)
        carrera.estado = 1
        with patch('builtins.print'):
            carrera.parada()
        self.assertEqual(carrera.estado, 0)
        mock_tiempo.reiniciar.assert_called_once()

    @patch('tu_archivo.Tiempo')
    def test_movimiento(self, MockTiempo):
        mock_tiempo = MockTiempo.return_value
        carrera = Carrera(1)
        carrera.estado = 0
        with patch('builtins.print'):
            carrera.movimiento()
        self.assertEqual(carrera.estado, 1)
        mock_tiempo.reiniciar.assert_called_once()

    @patch('tu_archivo.Tiempo')
    def test_finalizar(self, MockTiempo):
        mock_tiempo = MockTiempo.return_value
        carrera = Carrera(1)
        carrera.estado = 0
        with patch('builtins.print'):
            with patch('builtins.input', return_value=''):
                carrera.finalizar()
        self.assertEqual(carrera.estado, 2)

    @patch('tu_archivo.Tiempo')
    def test_cancelacion(self, MockTiempo):
        carrera = Carrera(1)
        with patch('builtins.print'):
            with patch('builtins.input', return_value=''):
                carrera.cancelacion()
        self.assertEqual(carrera.estado, 3)

if __name__ == '__main__':
    unittest.main()