import unittest
from unittest.mock import patch
import saludar 


class TestSaludar(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input', return_value='')  # Mock para input
    def test_saludar(self, mock_input, mock_print):
        saludar()
        
        # Verificar que se llamaron las funciones print e input
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_input.called)

        # Verificar que la salida es la esperada
        mock_print.assert_called_with(
            '¡Bienvenido a taxi-metrónomo!: \n'
            'Inicia sesión con tu usuario y contraseña para acceder a la aplicación. \n'
            'En el MENÚ podrás iniciar una carrera, cambiar de usuario o incluso modificar las tarifas. \n'
            'Con la carrera iniciada el taxi está arrancado, así que cobrará 0.02 céntimos por segundo.\n'
            'Si pones el coche en movimiento, se cobrará a 0.05 céntimos por segundo. \n'
            'Pararás y entrarás en movimiento las veces que necesites hasta finalizar la carrera. \n'
        )

if __name__ == '__main__':
    unittest.main()
