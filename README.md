# Proyecto: Sistema de Encuestas en Consola (POO)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## Descripción

Este proyecto es una aplicación de consola desarrollada en Python que implementa un sistema simple de encuestas. Fue creado como una actividad práctica para aplicar los conceptos básicos de la Programación Orientada a Objetos (POO). El programa permite a los usuarios agregar respuestas a una encuesta predefinida y visualizar todos los resultados recopilados de manera organizada.

## Características

- **Diseño Orientado a Objetos**: El núcleo del programa es la clase `Encuesta`, que encapsula los datos (preguntas y respuestas) y los comportamientos (agregar respuestas, mostrar resultados) del sistema.
- **Menú Interactivo**: El programa se ejecuta en la consola y presenta un menú simple para que el usuario elija las acciones a realizar.
- **Recolección de Datos**: Permite registrar múltiples respuestas de encuestados de forma secuencial.
- **Visualización de Resultados**: Ofrece una opción para mostrar todas las respuestas guardadas, presentadas de forma clara y legible.

## Tecnologías Utilizadas

- **Python 3**

No se requieren librerías externas para ejecutar este proyecto.

## Instalación y Uso

Para ejecutar este proyecto en tu máquina local, sigue estos sencillos pasos:

1.  **Clona el repositorio:**
    ```sh
    git clone <URL-de-tu-repositorio>
    ```

2.  **Navega al directorio del proyecto:**
    ```sh
    cd <nombre-del-directorio>
    ```

3.  **Ejecuta el script de Python:**
    ```sh
    python proyecto_encuesta.py
    ```

## Uso del Programa

Una vez que el script esté en ejecución, verás el siguiente menú en tu consola:

```
--- Menú Principal ---
1. Agregar una nueva respuesta
2. Mostrar todos los resultados
3. Salir
```

-   **Opción 1**: Te guiará a través de las preguntas de la encuesta para registrar una nueva respuesta.
-   **Opción 2**: Mostrará todas las respuestas que se han recopilado hasta el momento.
-   **Opción 3**: Finalizará la ejecución del programa.

## Contexto del Proyecto

Este software fue desarrollado como parte de una tarea académica con el objetivo de que los estudiantes aplicaran conceptos de POO en Python. Los requisitos principales de la tarea incluían:

-   **Diseño de Clases**:
    -   Crear una clase principal `Encuesta`.
    -   Definir atributos para las preguntas (`preguntas`) y las respuestas (`respuestas`).
    -   Implementar métodos como `agregar_respuesta()` y `mostrar_resultados()`.
-   **Reglas de Implementación**:
    -   La encuesta debía contener un mínimo de 3 preguntas.
    -   El objetivo era recolectar un mínimo de 10 respuestas.
-   **Entregables**:
    -   El código fuente en un archivo `.py`.
    -   Un reporte en PDF con los resultados y conclusiones.
