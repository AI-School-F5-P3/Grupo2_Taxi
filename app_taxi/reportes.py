import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
def gererar_grafica():
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
    plt.figure(figsize=(12,8))
    sns.countplot(data=df, x='mes', hue='conductor', palette='viridis')
    plt.title('Carreras por conductor por mes')
    plt.xlabel('Mes')
    plt.ylabel('Número de carreras')
    plt.legend(title='Conductor')
    plt.show()

    # viajes por franja horaria
    plt.figure(figsize=(12,8))
    sns.countplot(data=df, x='hora', palette='viridis')
    plt.title('Viajes por franja horaria')
    plt.xlabel('hora')
    plt.ylabel('Número de viajes')
    plt.show()

    #Ingresos por conductor por mes
    df_grouped = df.groupby(['mes', 'conductor'])['precio_total'].sum().reset_index()
    plt.figure(figsize=(12,8))
    sns.barplot(data=df_grouped, x='mes', y='precio_total', hue='conductor', palette='viridis')
    plt.title('Ingresos por conductor por mes')
    plt.xlabel('Mes')
    plt.ylabel('Ingresos')
    plt.legend(title='Conductor')
    plt.show()

    #Viajes por duración
    plt.figure(figsize=(12,8))
    sns.countplot(data=df, x='bucket_minutos', palette='viridis')
    plt.title('Viajes por duración')
    plt.xlabel('Duración (minutos)')
    plt.ylabel('Número de viajes')
    plt.show()
