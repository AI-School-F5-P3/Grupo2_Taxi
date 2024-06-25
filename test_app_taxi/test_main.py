import unittest
from unittest.mock import patch, MagicMock
import logging
import sys
import main 

class TestMiPrograma(unittest.TestCase):

    @patch("mi_programa.saludar.saludar")
    @patch("mi_programa.entrar_con_password.menu_principal")
    @patch("mi_programa.mostrar_menu.mostrar_menu")
    def test_program_flow(self, mock_mostrar_menu, mock_menu_principal, mock_saludar):
        # Simula la secuencia de llamadas en el flujo principal
        mock_menu_principal.side_effect = SystemExit  # Para evitar salir del test
        with self.assertRaises(SystemExit):
            main.saludar.saludar()
            main.entrar_con_password.menu_principal()
            main.mostrar_menu.mostrar_menu()

        mock_saludar.assert_called_once()
        mock_menu_principal.assert_called_once()
        mock_mostrar_menu.assert_called_once()

    @patch("mi_programa.logging.basicConfig")
    def test_logging_configuration(self, mock_basicConfig):
        # Verifica que la configuración del logging se establezca correctamente
        main.logging.basicConfig(level=logging.DEBUG, 
                                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                                        filename='log_taxi.log', 
                                        filemode='a')
        mock_basicConfig.assert_called_once_with(level=logging.DEBUG, 
                                                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                                                 datefmt='%Y-%m-%d %H:%M:%S',
                                                 filename='log_taxi.log', 
                                                 filemode='a')

    def test_handle_exception(self):
        # Verifica que el manejador de excepciones se configure correctamente
        logger = logging.getLogger('test_logger')
        exc_type, exc_value, exc_traceback = Exception, Exception("Test exception"), None
        with patch.object(logger, 'error') as mock_error:
            main.handle_exception(exc_type, exc_value, exc_traceback)
            mock_error.assert_called_once_with("excepcion no recogida", exc_info=(exc_type, exc_value, exc_traceback))

    @patch("sys.excepthook", new_callable=MagicMock)
    def test_sys_excepthook_set(self, mock_excepthook):
        # Verifica que sys.excepthook se establezca correctamente
        main.sys.excepthook = main.handle_exception
        self.assertEqual(sys.excepthook, main.handle_exception)

if __name__ == '__main__':
    unittest.main()