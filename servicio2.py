import datetime
import pytz
import streamlit as st


class Tiempo():
    def __init__(self):
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))

    def reiniciar(self):
        self.inicio_tiempo = datetime.datetime.now(pytz.timezone('Europe/Madrid'))  # Actualiza el inicio_tiempo al momento actual
        
    def tiempo_transcurrido(self):
        return (datetime.datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()

    def es_nocturno(self):
        hora = self.inicio_tiempo.hour
        return 22 <= hora or hora < 6
        

class Tarifa():
    def __init__(self, precio_parada=0.02, precio_movimiento=0.05):
        self.precio_parada = precio_parada
        self.precio_movimiento = precio_movimiento
        self.precio_parada_nocturno = precio_parada * 2
        self.precio_movimiento_nocturno = precio_movimiento * 2

    def calcular_costo(self, tiempo_transcurrido, estado, es_nocturno):
        #if estado == 0:  # parado
        if es_nocturno:
            return tiempo_transcurrido * self.precio_parada_nocturno
        else:
            return tiempo_transcurrido * self.precio_parada
        #elif estado == 1:  # movimiento
            #if es_nocturno:
                #return tiempo_transcurrido * self.precio_movimiento_nocturno
            #else:
                #return tiempo_transcurrido * self.precio_movimiento
        #return 0

class Carrera():
    ultima_carrera = 100 
    
    def __init__(self, id):
        self._id = id
        self.tiempo = Tiempo()
        self.tarifa = Tarifa()
        self.estado = 0
        self.precio_total = 0
        self.tiempo_acumulado_parado = 0
        self.tiempo_acumulado_movimiento = 0

    def actualizar_costo(self):
        tiempo_transcurrido = self.tiempo.tiempo_transcurrido()
        es_nocturno = self.tiempo.es_nocturno()
        costo = self.tarifa.calcular_costo(tiempo_transcurrido, self.estado, es_nocturno)
        self.precio_total += costo
        #if self.estado == 0:
        self.tiempo_acumulado_parado += tiempo_transcurrido
        #elif self.estado == 1:
        self.tiempo_acumulado_movimiento += tiempo_transcurrido
        return costo

    def parada(self):
        if self.estado == 1:  # Si estaba en movimiento, calcular el costo del movimiento
            costo = self.actualizar_costo()
            print(f"Costo por movimiento: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 0  # Cambiar el estado a parado
        self.tiempo.reiniciar()  # Reiniciar el tiempo al momento actual
        print("Taxi parado.")

    def movimiento(self):
        if self.estado == 0:  # Si estaba parado, calcular el costo de la parada
            costo = self.actualizar_costo()
            print(f"Costo por parada: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 1  # Cambiar el estado a movimiento
        self.tiempo.reiniciar()  # Reiniciar el tiempo al momento actual
        print("Taxi en movimiento.")

    def finalizar(self):
        costo = self.actualizar_costo()
        print(f"Precio del último tramo: {costo:.2f}€ (Total: {self.precio_total:.2f}€)")
        self.estado = 2
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print(f"Carrera {Carrera.ultima_carrera} finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Total a pagar: {self.precio_total:.2f}€")
        Carrera.ultima_carrera +=1
        input('Presione intro para volver al menú')
        
    def cancelacion(self):
        print(f"Trayecto cancelado")
        self.estado = 3
        fecha_final = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        print(f"Carrera {Carrera.ultima_carrera} finalizada a las {fecha_final.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Total a pagar: 0€")
        Carrera.ultima_carrera +=1
        input('Presione intro para volver al menú')
        

######

    
import streamlit as st

def main():
    st.title("Taxi Meter")
    menu_options = ["Configuración", "Comenzar carrera", "Salir de la aplicación"]
    selected_option = st.selectbox("Seleccione una opción", menu_options)
    usuarios={"Carolina": "000",
    "Angel": "111",
     "Sergio": "222",
     "Nathaly": "333",
     "Jorge": "444"}
    if selected_option == "Configuración":
        st.write('has seleccionado confi')
    elif selected_option == "Comenzar carrera":
        nombre = st.text_input("Ingresa tu Usuario:").capitalize()
        credencial=st.text_input("Ingresa tu password:")
        if nombre in usuarios:
            tu_pass=usuarios[nombre]
        
            if tu_pass==credencial:
                if nombre:
                    st.header(f"Hola, {nombre}!")
                    st.write("Bienvenido al taxi meter")
                st.session_state.tiempo_inicio=Tiempo() #En el estado de la sesión, se establece tiempo_incio
            
                
                #Se verifica si la carrera ya ha sido iniciada anteriormente
                if "carrera_iniciada" not in st.session_state: #Si sucede que NO
                    st.session_state.carrera_iniciada = False #Entonces en el estado de la sesión, se establece carrera_iniciada y se le asigna False
                    st.session_state.nueva_carrera=Carrera(Carrera.ultima_carrera)
                    #st.session_state.tarifa = Tarifa()
                    st.session_state.tiempo_inicio=Tiempo()
                    st.session_state.pausa = False

                if not st.session_state.carrera_iniciada:#Evalúa si NO se da st.session_state.carrera_iniciada
                    st.write("Presiona el botón 'Iniciar' para comenzar la carrera") #Si No se da, escribe
                    iniciar_button = st.button("Iniciar")
                    if iniciar_button: #Si has pulsado el botón "iniciar"
                        #st.session_state.nueva_carrera.tiempo.reiniciar()
                        st.write(f"Carrera iniciada a las {st.session_state.nueva_carrera.tiempo.inicio_tiempo.strftime('%Y-%m-%d %H:%M:%S')}.")
                        st.session_state.carrera_iniciada = True #Y cambia el estado de st.session_state.carrera_iniciada
                        
                else:
                    st.write("Presiona el botón 'Pausa' para pausar la carrera")
                    pausa_button = st.button("Pausa")
                    if pausa_button:
                        st.session_state.pausa = True
                        st.write("Carrera pausada.")
                        #st.session_state.nueva_carrera.tiempo.pausar()
                    
                    #st.write("Presiona el botón 'Iniciar' para reanudar la carrera")
                    #reanudar_button = st.button("ReiIniciar")
                    
                     
                        #if reanudar_button:
                        #st.session_state.pausa = False
                        #st.write("Carrera reanudada.")
                        #st.session_state.nueva_carrera.tiempo.reanudar()
                    if st.session_state.pausa:
                        st.write("Presiona el botón 'Reanudar' para reanudar la carrera")
                        reanudar_button = st.button("Reanudar")
                        if reanudar_button:
                            st.session_state.pausa = False
                            st.write("Carrera reanudada.")
                    #st.session_state.nueva_carrera.tiempo.reanudar()    
                        
                    
                    st.write("Presiona el botón 'Finalizar' para finalizar la carrera")
                    finalizar_button = st.button("Finalizar")
                    
                    if finalizar_button:
                        #st.session_state.nueva_carrera.finalizar()
                        st.write("Carrera finalizada.")
                        
                        tiempo_transcurrido = st.session_state.nueva_carrera.tiempo.tiempo_transcurrido()

                        es_nocturno = st.session_state.tiempo_inicio.es_nocturno()
                        costo = tiempo_transcurrido*0.05#st.session_state.tarifa.calcular_costo(tiempo_transcurrido, st.session_state.nueva_carrera.estado, es_nocturno)
                                
                        st.write(f"Tiempo transcurrido: {st.session_state.tiempo_inicio.tiempo_transcurrido()}")
                        #st.write(f"Costo de la carrera: ${costo:.2f}")
                        st.metric("Precio final", f"${costo:.2f}")  
                        st.success(f"Precio final: ${costo:.2f}")
                        
                        #st.session_state.nueva_carrera.precio_total
                        #st.write(f"Costo de la carrera: ${st.session_state.tarifa.calcular_costo()}")
                        #st.metric("Precio final", f"${st.session_state.nueva_carrera.precio_total:.2f}")  #
                        st.success(f"Precio final: ${tiempo_transcurrido*0.05:.2f}")
                        st.session_state.carrera_iniciada = False
        
        else:
            st.write('No se encuentra tu usuario')
        
    elif selected_option == "Salir de la aplicación":
        if st.button("Salir"):
            st.write("Sales de la aplicación. Hasta pronto")
    
    
    


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
