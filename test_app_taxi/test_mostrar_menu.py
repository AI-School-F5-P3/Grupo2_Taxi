import unittest
from unittest.mock import patch, call, MagicMock
import os

import mostrar_menu  

class TestMiPrograma(unittest.TestCase):

    @patch("os.system")
    def test_limpiar_consola_windows(self, mock_system):
        with patch("os.name", 'nt'):
            mostrar_menu.limpiar_consola()
            mock_system.assert_called_once_with('cls')

    @patch("os.system")
    def test_limpiar_consola_unix(self, mock_system):
        with patch("os.name", 'posix'):
            mostrar_menu.limpiar_consola()
            mock_system.assert_called_once_with('clear')

    @patch("builtins.input", side_effect=["4", "abc", "2"])
    @patch("builtins.print")
    def test_solicitar_opcion(self, mock_print, mock_input):
        option = mostrar_menu.solicitar_opcion()
        self.assertEqual(option, 2)
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call('Por favor, elija un número entre 1 y 3.')
        mock_print.assert_any_call('Entrada no válida. Por favor, introduzca un número entero del 1 al 3.')

    @patch("mi_programa.entrar_con_password.menu_principal", side_effect=SystemExit)
    @patch("mi_programa.limpiar_consola")
    @patch("mi_programa.solicitar_opcion", side_effect=[1, 3])
    @patch("builtins.print")
    def test_mostrar_menu_config(self, mock_print, mock_solicitar_opcion, mock_limpiar_consola, mock_menu_principal):
        with self.assertRaises(SystemExit):
            mostrar_menu.mostrar_menu_config()
        
        mock_print.assert_any_call('Cambiar conductor')
        mock_menu_principal.assert_called_once()
        self.assertEqual(mock_limpiar_consola.call_count, 4)

    @patch("mi_programa.servicio.iniciar")
    @patch("mi_programa.mostrar_menu_config")
    @patch("mi_programa.limpiar_consola")
    @patch("mi_programa.solicitar_opcion", side_effect=[1, 2, 3])
    @patch("builtins.input", side_effect=["2", "3"])
    @patch("builtins.print")
    def test_mostrar_menu(self, mock_print, mock_input, mock_solicitar_opcion, mock_limpiar_consola, mock_mostrar_menu_config, mock_servicio_iniciar):
        with patch("os._exit") as mock_exit:
            with self.assertRaises(SystemExit):
                mostrar_menu.test_mostrar_menu()
            
            self.assertEqual(mock_limpiar_consola.call_count, 6)  # Llamado al inicio y tras cada opción
            mock_mostrar_menu_config.assert_called_once()
            mock_servicio_iniciar.assert_called_once()
            mock_exit.assert_called_once_with(0)
            mock_print.assert_any_call('Vas a salir de la aplicación')
            mock_print.assert_any_call('Sales de la aplicación. Hasta pronto')

if __name__ == '__main__':
    unittest.main()
