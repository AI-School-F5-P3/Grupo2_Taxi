import unittest
from unittest.mock import mock_open, patch
import os

def generar_numero_carrera(nombre_fichero) -> int:
    ubicacion = os.path.join(os.path.dirname(__file__), nombre_fichero)
    try:
        with open(ubicacion, 'r') as file:
            ultima_carrera = int(file.read().strip())
    except FileNotFoundError:
        print("El archivo no existe.")
        ultima_carrera = 0
    except IOError:
        ultima_carrera = 0
    ultima_carrera += 1
    try:
        with open(ubicacion, 'w') as file:
            file.write(str(ultima_carrera))
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Error al leer el archivo.")
    return ultima_carrera

class TestGenerarNumeroCarrera(unittest.TestCase):

    @patch('os.path.join', return_value='mocked_path')
    @patch('builtins.open', new_callable=mock_open, read_data='100')
    def test_generar_numero_carrera_increment(self, mock_open, mock_path_join):
        resultado = generar_numero_carrera('test_file.txt')
        self.assertEqual(resultado, 101)
        mock_open.assert_called_with('mocked_path', 'w')
        mock_open().write.assert_called_once_with('101')

    @patch('os.path.join', return_value='mocked_path')
    @patch('builtins.open', new_callable=mock_open)
    def test_generar_numero_carrera_file_not_found(self, mock_open, mock_path_join):
        mock_open.side_effect = [FileNotFoundError, mock_open.return_value]
        resultado = generar_numero_carrera('test_file.txt')
        self.assertEqual(resultado, 1)
        mock_open.assert_called_with('mocked_path', 'w')
        mock_open().write.assert_called_once_with('1')

    @patch('os.path.join', return_value='mocked_path')
    @patch('builtins.open', new_callable=mock_open)
    def test_generar_numero_carrera_io_error(self, mock_open, mock_path_join):
        mock_open.side_effect = [IOError, mock_open.return_value]
        resultado = generar_numero_carrera('test_file.txt')
        self.assertEqual(resultado, 1)
        mock_open.assert_called_with('mocked_path', 'w')
        mock_open().write.assert_called_once_with('1')

if __name__ == '__main__':
    unittest.main()