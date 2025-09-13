class Encuesta:
    """
    Clase principal para gestionar la encuesta sobre ideas de proyecto.
    Contiene las preguntas y almacena las respuestas de los participantes.
    """
    
    def __init__(self):
        """
        Constructor de la clase Encuesta.
        Define las preguntas e inicializa la lista para guardar respuestas.
        """
        # Atributo con la lista de preguntas a realizar
        self.preguntas = [
            "¿Cuál es tu nombre?",
            "¿Qué idea de proyecto te interesa más (Ej: Juego, Web, Análisis de Datos)?",
            "¿Con qué librería de Python te gustaría trabajar (Ej: Pygame, Flask, Pandas)?"
        ]
        
        # Atributo para almacenar las respuestas de cada estudiante
        self.respuestas = []

    def agregar_respuesta(self):
        """
        Guarda la respuesta completa de un estudiante.
        Realiza todas las preguntas y añade las respuestas a la lista principal.
        """
        print("\n--- Iniciando nueva encuesta ---")
        respuestas_estudiante = []
        
        for pregunta in self.preguntas:
            respuesta = input(f"{pregunta} ")
            respuestas_estudiante.append(respuesta.strip())
            
        self.respuestas.append(respuestas_estudiante)
        print("¡Gracias! Tu respuesta ha sido guardada con éxito.")

    def mostrar_resultados(self):
        """
        Imprime las respuestas de todos los estudiantes de forma organizada.
        """
        print("\n--- Resultados Completos de la Encuesta ---")
        
        if not self.respuestas:
            print("Aún no se han registrado respuestas.")
            return

        for i, respuesta_estudiante in enumerate(self.respuestas):
            nombre_estudiante = respuesta_estudiante[0]
            print(f"\n✅ Respuesta #{i + 1} (De: {nombre_estudiante})")
            
            for j in range(1, len(self.preguntas)):
                pregunta_texto = self.preguntas[j]
                respuesta_texto = respuesta_estudiante[j]
                print(f"   - {pregunta_texto}: {respuesta_texto}")


# --- Bloque principal para ejecutar el programa ---
def main():
    """
    Función principal que crea el menú interactivo para el usuario.
    """
    encuesta_proyectos = Encuesta()
    
    print("Bienvenido al sistema de encuestas para ideas de proyecto.")
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar una nueva respuesta")
        print("2. Mostrar todos los resultados")
        print("3. Salir")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == '1':
            encuesta_proyectos.agregar_respuesta()
        elif opcion == '2':
            encuesta_proyectos.mostrar_resultados()
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    main()
