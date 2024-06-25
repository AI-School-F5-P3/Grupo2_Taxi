import streamlit as st
from servicio import Carrera, Tarifa
import datetime
import pytz

# Función para inicializar variables de sesión
def init_session_state():
    if 'carrera' not in st.session_state:
        st.session_state.carrera = Carrera(Carrera.ultima_carrera)
    if 'precio_total' not in st.session_state:
        st.session_state.precio_total = 0.0
    if 'ultimo_tiempo' not in st.session_state:
        st.session_state.ultimo_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))

# Función para actualizar el costo basado en el tiempo transcurrido
def actualizar_costo():
    tiempo_actual = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
    tiempo_transcurrido = (tiempo_actual - st.session_state.ultimo_tiempo).total_seconds()
    st.session_state.ultimo_tiempo = tiempo_actual

    costo = st.session_state.carrera.tarifa.calcular_costo(
        tiempo_transcurrido, st.session_state.carrera.estado, st.session_state.carrera.tiempo.es_nocturno()
    )
    st.session_state.precio_total += costo
    return costo

# Función principal de la aplicación
def main():
    st.title("Aplicación de Taxi")
    st.write("Bienvenido a la aplicación de taxi.")

    # Crear el menú en la barra lateral
    menu = ["Inicio", "Configuración", "Carrera", "Salir"]
    choice = st.sidebar.selectbox("Menú", menu)

    init_session_state()

    if choice == "Inicio":
        st.subheader("Inicio")
        st.write("Aquí puedes ver información general y novedades.")

    elif choice == "Configuración":
        st.subheader("Configuración")
        st.write("Aquí puedes cambiar las configuraciones del sistema.")
        
        precio_parada = st.number_input('Precio por parada (€/segundo)', min_value=0.0, value=0.02)
        precio_movimiento = st.number_input('Precio por movimiento (€/segundo)', min_value=0.0, value=0.05)
        
        st.session_state.carrera.tarifa = Tarifa(precio_parada, precio_movimiento)
        st.write(f"Tarifas actualizadas: Parada: {st.session_state.carrera.tarifa.precio_parada}€/seg, Movimiento: {st.session_state.carrera.tarifa.precio_movimiento}€/seg")

    elif choice == "Carrera":
        st.subheader("Carrera")
        st.write("Aquí puedes gestionar una carrera.")

        if st.button('Iniciar carrera'):
            st.session_state.carrera.tiempo.reiniciar()
            st.session_state.ultimo_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
            st.write(f"Carrera iniciada a las {st.session_state.carrera.tiempo.inicio_tiempo.strftime('%Y-%m-%d %H:%M:%S')}.")
            st.session_state.precio_total = 0.0

        if st.button('Parada'):
            if st.session_state.carrera.estado == 1:
                costo = actualizar_costo()
                st.session_state.carrera.parada()
                st.write(f"Costo por movimiento: {costo:.2f}€ (Total: {st.session_state.precio_total:.2f}€)")
            else:
                st.write("El taxi ya está parado. No puedes parar de nuevo.")

        if st.button('Mover'):
            if st.session_state.carrera.estado == 0:
                costo = actualizar_costo()
                st.session_state.carrera.movimiento()
                st.write(f"Costo por parada: {costo:.2f}€ (Total: {st.session_state.precio_total:.2f}€)")
            else:
                st.write("El taxi ya está en movimiento. No puedes mover de nuevo.")

        if st.button('Finalizar'):
            if st.session_state.carrera.estado in [0, 1]:
                costo = actualizar_costo()
                st.session_state.carrera.finalizar()
                st.write(f"Precio del último tramo: {costo:.2f}€")
                st.write(f"Carrera {Carrera.ultima_carrera - 1} finalizada.")
                st.write(f"Total a pagar: {st.session_state.precio_total:.2f}€")
            else:
                st.write("La carrera ya ha sido finalizada o cancelada.")

        if st.button('Cancelar'):
            st.session_state.carrera.cancelacion()
            st.session_state.precio_total = 0.0
            st.write(f"Carrera {Carrera.ultima_carrera - 1} cancelada. Total a pagar: 0€")

    elif choice == "Salir":
        st.subheader("Salir")
        st.write("Gracias por usar la aplicación de taxi. ¡Hasta pronto!")
        st.stop()

if __name__ == '__main__':
    main()
