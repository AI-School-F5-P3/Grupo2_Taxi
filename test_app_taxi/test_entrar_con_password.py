import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import os
import app_taxi.entrar_con_password as entrar_con_password



class TestMiModulo(unittest.TestCase):

    @patch("entrar_con_password.open", new_callable=mock_open, read_data='[{"usuario": "user1", "contraseña": "pass1"}]')
    def test_cargar_usuarios(self, mock_file):
        usuarios= entrar_con_password.cargar_usuarios()
        mock_file.assert_called_once_with('usuarios.json', 'r', encoding='utf-8')
        self.assertEqual(usuarios, [{"usuario": "user1", "contraseña": "pass1"}])

    @patch("entrar_con_password.open", new_callable=mock_open)
    def test_guardar_usuarios(self, mock_file):
        usuarios = [{"usuario": "user1", "contraseña": "pass1"}]
        entrar_con_password.guardar_usuarios(usuarios)
        mock_file.assert_called_once_with('usuarios.json', 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with(json.dumps(usuarios, indent=4))

    @patch("entrar_con_password.cargar_usuarios", return_value=[{"usuario": "user1", "contraseña": "pass1"}])
    @patch("builtins.print")
    def test_verificar_contraseña_correcta(self, mock_print, mock_cargar_usuarios):
        resultado = entrar_con_password.verificar_contraseña("user1", "pass1")
        self.assertTrue(resultado)
        mock_print.assert_called_once_with('Contraseña correcta')

    @patch("entrar_con_password.cargar_usuarios", return_value=[{"usuario": "user1", "contraseña": "pass1"}])
    @patch("builtins.print")
    def test_verificar_contraseña_incorrecta(self, mock_print, mock_cargar_usuarios):
        resultado = entrar_con_password.verificar_contraseña("user1", "wrongpass")
        self.assertFalse(resultado)
        mock_print.assert_called_once_with('¡La contraseña no es correcta!')

    @patch("entrar_con_password.cargar_usuarios", return_value=[{"usuario": "user1", "contraseña": "pass1"}])
    @patch("builtins.print")
    def test_verificar_contraseña_usuario_no_encontrado(self, mock_print, mock_cargar_usuarios):
        resultado = entrar_con_password.verificar_contraseña("user2", "pass2")
        self.assertFalse(resultado)
        mock_print.assert_called_once_with('Usuario no encontrado.')

    @patch("entrar_con_password.verificar_contraseña", return_value=True)
    @patch("entrar_con_password.mostrar_menu.mostrar_menu")
    @patch("builtins.input", side_effect=["1", "user1", "pass1"])
    @patch("builtins.print")
    def test_menu_principal_iniciar_sesion(self, mock_print, mock_input, mock_verificar_contraseña, mock_mostrar_menu):
        with self.assertRaises(SystemExit):  # Simulate os._exit
            entrar_con_password.menu_principal()
        mock_verificar_contraseña.assert_called_once_with("user1", "pass1")
        mock_mostrar_menu.assert_called_once()

    @patch("os._exit")
    @patch("builtins.input", side_effect=["2"])
    @patch("builtins.print")
    def test_menu_principal_salir(self, mock_print, mock_input, mock_exit):
        entrar_con_password.menu_principal()
        mock_exit.assert_called_once_with(0)
        mock_print.assert_any_call("Saliendo...")
        mock_print.assert_any_call('Sales de la aplicación. Hasta pronto')

    @patch("builtins.input", side_effect=["3", "2"])
    @patch("builtins.print")
    def test_menu_principal_opcion_no_valida(self, mock_print, mock_input):
        with patch('os._exit') as mock_exit:  # To prevent the test from exiting
            entrar_con_password.menu_principal()
        mock_print.assert_any_call("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == '__main__':
    unittest.main()