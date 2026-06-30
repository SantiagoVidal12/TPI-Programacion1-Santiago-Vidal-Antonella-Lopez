# TPI-Programacion1-Santiago-Vidal-Antonella-Lopez
# TPI - Programación 1: Sistema de Gestión de Países

Este proyecto es el Trabajo Práctico Integrador (TPI) desarrollado para la materia Programación 1. Consiste en una aplicación de consola en Python que permite administrar de forma dinámica, organizada y persistente un registro global de países, sus poblaciones, superficies y continentes.

# Estructura del Proyecto

El programa se encuentra modularizado en diferentes archivos especializados para facilitar su mantenimiento y escalabilidad:
* `main.py`: Punto de entrada del programa con el menú interactivo principal.
* `Funciones_Generales.py`: Operaciones básicas del sistema y lectura de archivos.
* `Agregar_paises.py` y `Actualizar_paises.py`: Módulos para insertar nuevos registros y modificar los existentes.
* `Buscar_Paises.py` y `Filtrado.py`: Herramientas de consulta y segmentación de datos.
* `Ordenamiento.py`: Algoritmo multifunción basado en el método de ordenamiento de burbuja (Bubble Sort).
* `Estadisticas.py`: Procesamiento de métricas y análisis de datos globales.
* `paises.csv`: Archivo de texto plano que actúa como base de datos persistente.

---

## Instrucciones de Uso

### Prerrequisitos
Tener instalado **Python 3.x** en tu sistema. No se requieren librerías externas ya que utiliza módulos nativos del lenguaje.

### Ejecución
1. Descargá o cloná este repositorio en tu máquina local.
2. Abrí una terminal o consola de comandos en la carpeta raíz del proyecto.
3. Ejecutá el programa principal con el siguiente comando:
   ```bash
   python main.py
   ```
   Si usas vscode: Simplemente ejecuta main.py

---

## Ejemplos de Entradas y Salidas

### 1. Carga inicial desde el archivo (`paises.csv`)
Al iniciar, el sistema lee de forma automática el archivo de texto y convierte cada fila estructurada en un diccionario dentro de una lista dinámica.

**Entrada interna (Estructura del CSV):**
```csv
nombre,población,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

### 2. Buscar un país (Ejemplo de Salida por Pantalla)
```text
=== BUSCAR PAÍS ===
Ingrese el nombre del país que desea buscar: Argentina

[Resultado Encontrado]
Nombre: Argentina
Población: 45,376,763 hab.
Superficie: 2,780,400 km²
Continente: América
```

### 3. Reporte Estadístico (Ejemplo de Salida por Pantalla)
```text
=== REPORTE ESTADÍSTICO GLOBAL ===
Cantidad total de países registrados: 2
Suma total de población analizada: 171.176.763 hab.
Promedio de población por país: 85,588,381 hab.
```

---

## Integrantes y Participación

El desarrollo del proyecto se realizó de manera conjunta y equitativa entre los miembros del equipo, distribuyendo las responsabilidades técnicas de la siguiente manera:

* **Santiago Vidal** 
  * Diseño de la arquitectura modular y del flujo principal del sistema (`main.py`).
  * Implementación de operaciones básicas del sistema y persistencia de datos (`Funciones_Generales.py`).
  * Desarrollo del algoritmo multifunción basado en ordenamiento de burbuja (`Ordenamiento.py`).
  * Programación de las herramientas de consulta por criterios y segmentación (`Filtrado.py`).
  * Desarrollo del módulo de cálculo matemático, métricas y reportes descriptivos (`Estadisticas.py`).

* **Antonella Lopez** 
  * Desarrollo de la lógica de consulta y localización exacta de registros (`Buscar_Paises.py`).
  * Diseño e implementación del formulario para la inserción de nuevos países (`Agregar_paises.py`).
  * Programación del módulo para la edición y modificación de datos existentes (`Actualizar_paises.py`).
  * Control de excepciones y validación de entradas de datos para asegurar la consistencia del archivo CSV.

## Link del Video Explicativo
* https://www.youtube.com/watch?v=TBkGksDxPw4