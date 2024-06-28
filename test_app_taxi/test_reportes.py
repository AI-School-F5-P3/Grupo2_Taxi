import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

class Reportes:
    @staticmethod
    def generar_grafica():
        # Cargar los datos
        df = pd.read_csv('datos.csv')
        df['inicio_carrera'] = pd.to_datetime(df['inicio_carrera'])
        df['fin_carrera'] = pd.to_datetime(df['fin_carrera'])
        df['mes'] = df['inicio_carrera'].dt.month
        df['hora'] = df['inicio_carrera'].dt.hour
        df['franja_horaria'] = (df['hora'] // 3) * 3
        df['duracion_minutos'] = (df['fin_carrera'] - df['inicio_carrera']).dt.total_seconds() / 60
        df['bucket_minutos'] = (df['duracion_minutos'] // 2) * 2

        plt.style.use('ggplot')  # Usar el estilo ggplot

        # Carreras por conductor por mes
        plt.figure(figsize=(12, 8))
        sns.countplot(data=df, x='mes', hue='conductor', palette='viridis')
        plt.title('Carreras por conductor por mes')
        plt.xlabel('Mes')
        plt.ylabel('Número de carreras')
        plt.legend(title='Conductor')
        plt.show()

        # Viajes por franja horaria
        plt.figure(figsize=(12, 8))
        sns.countplot(data=df, x='hora', palette='viridis')
        plt.title('Viajes por franja horaria')
        plt.xlabel('Hora')
        plt.ylabel('Número de viajes')
        plt.show()

        # Ingresos por conductor por mes
        df_grouped = df.groupby(['mes', 'conductor'])['precio_total'].sum().reset_index()
        plt.figure(figsize=(12, 8))
        sns.barplot(data=df_grouped, x='mes', y='precio_total', hue='conductor', palette='viridis')
        plt.title('Ingresos por conductor por mes')
        plt.xlabel('Mes')
        plt.ylabel('Ingresos')
        plt.legend(title='Conductor')
        plt.show()

        # Viajes por duración
        plt.figure(figsize=(12, 8))
        sns.countplot(data=df, x='bucket_minutos', palette='viridis')
        plt.title('Viajes por duración')
        plt.xlabel('Duración (minutos)')
        plt.ylabel('Número de viajes')
        plt.show()

class TestReportes(unittest.TestCase):

    @patch('pandas.read_csv')
    @patch('matplotlib.pyplot.show')
    def test_generar_grafica(self, mock_show, mock_read_csv):
        # Datos de prueba
        data = StringIO("""carrera,conductor,inicio_carrera,fin_carrera,precio_total
1,Nathaly,2023-01-01 12:00:00,2023-01-01 12:30:00,6.00
2,Carolina,2023-01-02 13:00:00,2023-01-02 13:45:00,9.00
3,Sergio,2023-01-03 14:00:00,2023-01-03 14:20:00,4.00
4,Angel,2023-01-04 15:00:00,2023-01-04 15:50:00,10.00
5,Jorge,2023-01-05 16:00:00,2023-01-05 16:10:00,2.00
""")
        df = pd.read_csv(data)
        mock_read_csv.return_value = df

        # Llamar al método
        Reportes.generar_grafica()

        # Verificar que se llamó a plt.show() cuatro veces
        self.assertEqual(mock_show.call_count, 4)

        # Verificar que las columnas se procesan correctamente
        df['inicio_carrera'] = pd.to_datetime(df['inicio_carrera'])
        df['fin_carrera'] = pd.to_datetime(df['fin_carrera'])
        df['mes'] = df['inicio_carrera'].dt.month
        df['hora'] = df['inicio_carrera'].dt.hour
        df['franja_horaria'] = (df['hora'] // 3) * 3
        df['duracion_minutos'] = (df['fin_carrera'] - df['inicio_carrera']).dt.total_seconds() / 60
        df['bucket_minutos'] = (df['duracion_minutos'] // 2) * 2

        self.assertIn('mes', df.columns)
        self.assertIn('hora', df.columns)
        self.assertIn('franja_horaria', df.columns)
        self.assertIn('duracion_minutos', df.columns)
        self.assertIn('bucket_minutos', df.columns)

if __name__ == '__main__':
    unittest.main()