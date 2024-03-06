import tkinter as tk
from tkinter import messagebox
import random

class JuegoMillonario:
    def __init__(self, master):
        self.master = master
        self.master.title("¿Quién quiere ser millonario?")

        self.jugadores = self.obtener_nombres_jugadores()
        self.banco_preguntas = self.cargar_preguntas()
        self.estaciones = random.sample(self.banco_preguntas, 10)
        self.respuestas_aleatorias()

        self.puntuaciones = {jugador: 0 for jugador in self.jugadores}
        self.jugador_actual = 0
        self.pregunta_actual = 0
        self.ayuda_50_50_usada = False
        self.ayuda_cambio_pregunta_usada = False
        self.premios = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

        self.mostrar_reglas_juego()
        self.crear_interfaz()

    def obtener_nombres_jugadores(self):
        jugadores = []
        for i in range(1, 3):
            nombre = input(f"Ingresa el nombre del jugador número {i}: ")
            jugadores.append(nombre)
        return jugadores

    def cargar_preguntas(self):
        preguntas = [
            {"pregunta": "¿Cuál es la capital de Francia?", "opciones": ["Londres", "Berlín", "París", "Madrid"], "respuesta_correcta": "París"},
            {"pregunta": "¿Cuántos planetas hay en nuestro sistema solar?", "opciones": ["8", "9", "10", "7"], "respuesta_correcta": "8"},
            {"pregunta": "¿Cuál es el río más largo del mundo?", "opciones": ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], "respuesta_correcta": "Nilo"},
            {"pregunta": "¿Quién pintó la obra maestra 'La Gioconda'?", "opciones": ["Picasso", "Van Gogh", "Leonardo da Vinci", "Rembrandt"], "respuesta_correcta": "Leonardo da Vinci"},
            {"pregunta": "¿Cuál es el animal más rápido del mundo?", "opciones": ["Guepardo", "Águila", "Halcón Peregrino", "Ciervo"], "respuesta_correcta": "Halcón Peregrino"},
            {"pregunta": "¿Cuál es el océano más grande del mundo?", "opciones": ["Océano Pacífico", "Océano Atlántico", "Océano Índico", "Océano Ártico"], "respuesta_correcta": "Océano Pacífico"},
            {"pregunta": "¿Cuál es el metal más caro del mundo?", "opciones": ["Oro", "Platino", "Rodio", "Paladio"], "respuesta_correcta": "Rodio"},
            {"pregunta": "¿Cuál es el país más pequeño del mundo?", "opciones": ["Mónaco", "Nauru", "Vaticano", "Tuvalu"], "respuesta_correcta": "Vaticano"},
            {"pregunta": "¿Cuál es el deporte más popular del mundo?", "opciones": ["Fútbol", "Básquetbol", "Tenis", "Cricket"], "respuesta_correcta": "Fútbol"},
            {"pregunta": "¿Cuál es el país más poblado del mundo?", "opciones": ["China", "India", "Estados Unidos", "Indonesia"], "respuesta_correcta": "China"},
            {"pregunta": "¿Cuál es la moneda oficial de Japón?", "opciones": ["Yen", "Dólar", "Euro", "Libra"], "respuesta_correcta": "Yen"},
            {"pregunta": "¿Cuál es el metal más ligero del mundo?", "opciones": ["Aluminio", "Hierro", "Cobre", "Plomo"], "respuesta_correcta": "Aluminio"},
            {"pregunta": "¿Cuál es el océano más profundo del mundo?", "opciones": ["Océano Pacífico", "Océano Atlántico", "Océano Índico", "Océano Ártico"], "respuesta_correcta": "Océano Pacífico"},
            {"pregunta": "¿Cuál es el desierto más grande del mundo?", "opciones": ["Sahara", "Gobi", "Antártico", "Árabe"], "respuesta_correcta": "Antártico"},
            {"pregunta": "¿Cuál es el río más caudaloso del mundo?", "opciones": ["Amazonas", "Nilo", "Congo", "Yangtsé"], "respuesta_correcta": "Amazonas"}
        ]
        return preguntas

    def respuestas_aleatorias(self):
        for pregunta in self.estaciones:
            random.shuffle(pregunta["opciones"])

    def mostrar_reglas_juego(self):
        mensaje_bienvenida = "¡Bienvenidos al juego ¿Quién quiere ser millonario?!\n\n"
        mensaje_bienvenida += "Reglas del juego:\n"
        mensaje_bienvenida += "- Tendrán acceso a dos ayudas: '50/50' y 'Cambio de Pregunta'.\n"
        mensaje_bienvenida += "- En las estaciones 5 y 7, podrán decidir si retirarse del juego o continuar.\n"
        mensaje_bienvenida += "- Si se retiran, se llevarán el puntaje acumulado hasta ese momento.\n"
        mensaje_bienvenida += "- Si responden incorrectamente en cualquier estación, perderán todo el puntaje acumulado.\n"
        mensaje_bienvenida += "- Para ganar el premio máximo, deberán responder correctamente todas las preguntas.\n\n"
        mensaje_bienvenida += "¡Buena suerte!\n\n"

        for jugador in self.jugadores:
            mensaje_bienvenida += f"Jugador: {jugador}\n"

        messagebox.showinfo("Bienvenida", mensaje_bienvenida)

    def crear_interfaz(self):
        self.label_pregunta = tk.Label(self.master, text="", font=("Arial", 16))
        self.label_pregunta.pack(pady=20)

        self.botones_opciones = []
        for i in range(4):
            btn = tk.Button(self.master, text="", font=("Arial", 12), command=lambda i=i: self.verificar_respuesta(i))
            btn.pack(pady=5)
            self.botones_opciones.append(btn)

        self.btn_50_50 = tk.Button(self.master, text="50/50", font=("Arial", 12), command=self.usar_50_50, state=tk.NORMAL)
        self.btn_50_50.pack(side=tk.LEFT, padx=10)

        self.btn_cambio_pregunta = tk.Button(self.master, text="Cambio de Pregunta", font=("Arial", 12), command=self.usar_cambio_pregunta, state=tk.NORMAL)
        self.btn_cambio_pregunta.pack(side=tk.RIGHT, padx=10)

        self.label_puntuaciones = tk.Label(self.master, text="", font=("Arial", 12))
        self.label_puntuaciones.pack(pady=10)

        self.actualizar_pregunta()
        self.actualizar_puntuaciones()

    def actualizar_pregunta(self):
        if self.pregunta_actual < len(self.estaciones):
            pregunta_actual = self.estaciones[self.pregunta_actual]
            self.label_pregunta.config(text=pregunta_actual["pregunta"])

            opciones = pregunta_actual["opciones"]
            for i in range(4):
                self.botones_opciones[i].config(text=f"{chr(65 + i)}. {opciones[i]}")

            self.habilitar_botones_ayuda()
        else:
            self.siguiente_jugador()

    def verificar_respuesta(self, opcion):
        respuesta_usuario = self.botones_opciones[opcion]["text"].split(". ")[1]
        jugador_actual = self.jugadores[self.jugador_actual]

        if respuesta_usuario == self.estaciones[self.pregunta_actual]["respuesta_correcta"]:
            self.puntuaciones[jugador_actual] = self.premios[self.pregunta_actual + 1]
            if self.pregunta_actual in [4, 6]:
                decision_retiro = self.preguntar_retiro()
                if decision_retiro:
                    self.siguiente_jugador()
                    return

            self.pregunta_actual += 1
            messagebox.showinfo("Correcto", f"¡Respuesta correcta, {jugador_actual}! Puntuación actual: {self.puntuaciones[jugador_actual]}")
            self.actualizar_puntuaciones()
            self.actualizar_pregunta()
        else:
            self.puntuaciones[jugador_actual] = 0
            messagebox.showinfo("Incorrecto", f"Respuesta incorrecta. Fin del juego para {jugador_actual}. Puntuación final: 0")
            self.siguiente_jugador()

    def actualizar_puntuaciones(self):
        puntuaciones_texto = ""
        for jugador, puntuacion in self.puntuaciones.items():
            puntuaciones_texto += f"{jugador}: {puntuacion}\n"
        self.label_puntuaciones.config(text=puntuaciones_texto)

    def habilitar_botones_ayuda(self):
        self.btn_50_50.config(state=tk.NORMAL if not self.ayuda_50_50_usada else tk.DISABLED, text="50/50" if not self.ayuda_50_50_usada else "Ayuda usada")
        self.btn_cambio_pregunta.config(state=tk.NORMAL if not self.ayuda_cambio_pregunta_usada else tk.DISABLED, text="Cambio de Pregunta" if not self.ayuda_cambio_pregunta_usada else "Ayuda usada")

    def usar_50_50(self):
        opciones = [btn.cget("text").split(". ")[1] for btn in self.botones_opciones]
        opciones_correctas = [opc for opc in opciones if opc == self.estaciones[self.pregunta_actual]["respuesta_correcta"]]
        opciones_falsas = [opc for opc in opciones if opc != self.estaciones[self.pregunta_actual]["respuesta_correcta"]]

        opciones_eliminar = random.sample(opciones_falsas, 2)

        for i in range(4):
            if self.botones_opciones[i]["text"].split(". ")[1] in opciones_eliminar:
                self.botones_opciones[i].config(state=tk.DISABLED)

        self.ayuda_50_50_usada = True
        self.btn_50_50.config(state=tk.DISABLED, text="Ayuda usada")

    def usar_cambio_pregunta(self):
        self.pregunta_actual += 1
        self.ayuda_cambio_pregunta_usada = True
        self.actualizar_pregunta()
        self.btn_cambio_pregunta.config(state=tk.DISABLED, text="Ayuda usada")

    def preguntar_retiro(self):
        jugador_actual = self.jugadores[self.jugador_actual]
        decision_retiro = messagebox.askyesno("Retiro", f"¿Deseas retirarte del juego con {self.puntuaciones[jugador_actual]} puntos?")
        return decision_retiro

    def siguiente_jugador(self):
        self.jugador_actual = (self.jugador_actual + 1) % len(self.jugadores)
        self.pregunta_actual = 0
        self.ayuda_50_50_usada = False
        self.ayuda_cambio_pregunta_usada = False
        self.actualizar_pregunta()
        self.actualizar_puntuaciones()

    def mostrar_resultado_final(self):
        mensaje_final = "Fin del juego.\n\n"
        for jugador, puntuacion in self.puntuaciones.items():
            mensaje_final += f"{jugador}: {puntuacion} puntos\n"
        mensaje_final += "\n¿Deseas volver a iniciar el juego?"
        decision = messagebox.askyesno("Resultados finales", mensaje_final)
        if decision:
            self.reiniciar_juego()
        else:
            self.guardar_resultados()
            self.master.quit()

    def reiniciar_juego(self):
        self.puntuaciones = {jugador: 0 for jugador in self.jugadores}
        self.jugador_actual = 0
        self.pregunta_actual = 0
        self.ayuda_50_50_usada = False
        self.ayuda_cambio_pregunta_usada = False
        self.estaciones = random.sample(self.banco_preguntas, 10)
        self.respuestas_aleatorias()
        self.actualizar_pregunta()
        self.actualizar_puntuaciones()

    def guardar_resultados(self):
        with open("resultados_millonario.txt", "a") as file:
            for jugador, puntuacion in self.puntuaciones.items():
                file.write(f"{jugador}: {puntuacion} puntos\n")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoMillonario(root)
    root.mainloop()
