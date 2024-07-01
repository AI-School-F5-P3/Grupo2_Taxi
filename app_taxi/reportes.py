#utilerías de generación de gráficos: matplotlib y seaborn
#utilería de generación de dataframe: pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

#Genera el dataframe df de pandas con los datos desde el fichero de carreras
df = pd.read_csv('datos.csv')

#Data Engineering: Formateo de datos y adición de columnas para ser utilizadas por los reportes
df['inicio_carrera'] = pd.to_datetime(df['inicio_carrera'])
df['fin_carrera'] = pd.to_datetime(df['fin_carrera'])
df['mes'] = df['inicio_carrera'].dt.month
df['hora'] = df['inicio_carrera'].dt.hour
df['franja_horaria'] = (df['hora'] // 3) * 3
df['duracion_minutos'] = (df['fin_carrera'] - df['inicio_carrera']).dt.total_seconds() / 60
df['bucket_minutos'] = (df['duracion_minutos'] // 2) * 2


# Carreras por conductor por mes
#1. Inicialización de gráfico
plt.figure(figsize=(12,8))
#2. Definición del tipo de gráfico
sns.countplot(data=df, x='mes', hue='conductor', palette='viridis')
#3. Títulos y etiquetas
plt.title('Carreras por conductor por mes')
plt.xlabel('Mes')
plt.ylabel('Número de carreras')
plt.legend(title='Conductor')
#4. Mostrar el gráfico
plt.show()

# viajes por franja horaria
# #1. Inicialización de gráfico
plt.figure(figsize=(12,8))
#2. Definición del tipo de gráfico
sns.countplot(data=df, x='hora', palette='viridis')
#3. Títulos y etiquetas
plt.title('Viajes por franja horaria')
plt.xlabel('hora')
plt.ylabel('Número de viajes')
#4. Mostrar el gráfico
plt.show()

#Ingresos por conductor por mes (Cálculo de agrupación necesario en el gráfico)
df_grouped = df.groupby(['mes', 'conductor'])['precio_total'].sum().reset_index()
# #1. Inicialización de gráfico
plt.figure(figsize=(12,8))
#2. Definición del tipo de gráfico
sns.barplot(data=df_grouped, x='mes', y='precio_total', hue='conductor', palette='viridis')
#3. Títulos y etiquetas
plt.title('Ingresos por conductor por mes')
plt.xlabel('Mes')
plt.ylabel('Ingresos')
plt.legend(title='Conductor')
#4. Mostrar el gráfico
plt.show()

#Viajes por duración
# #1. Inicialización de gráfico
plt.figure(figsize=(12,8))
#2. Definición del tipo de gráfico
sns.countplot(data=df, x='bucket_minutos', palette='viridis')
#3. Títulos y etiquetas
plt.title('Viajes por duración')
plt.xlabel('Duración (minutos)')
plt.ylabel('Número de viajes')
#4. Mostrar el gráfico
plt.show()


#Gráfico Circular
# Agrupamos los datos por conductor en todo el dataframe y sumamos los precios
ingresos_por_conductor = df.groupby("conductor")["precio_total"].sum()
#1. Inicialización de gráfico
plt.figure(figsize=(8, 6))
#2. Definición del tipo de gráfico
plt.pie(ingresos_por_conductor, labels=ingresos_por_conductor.index, autopct="%1.1f%%", startangle=90)
#3. Títulos y etiquetas
plt.title("Ingresos totales por conductor")
plt.axis("equal")  # Para que el gráfico sea un círculo perfecto
#4. Mostrar el gráfico
plt.show()