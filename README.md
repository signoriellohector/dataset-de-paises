# Sistema de Gestión de Datos de Países

Este proyecto es una aplicación diseñada para la gestión, visualización y análisis estadístico de un dataset de países. Permite realizar operaciones CRUD básicas, búsquedas avanzadas, filtros personalizados, ordenamiento de datos y cálculo de métricas estadísticas a partir de un archivo de datos estructurado (como un archivo CSV).

## 📋 Estructura del Menú y Funcionalidades

El programa cuenta con un menú interactivo que ofrece las siguientes opciones y capacidades:

### 1. Agregar un País
* **Descripción:** Permite registrar un nuevo país dentro del sistema.
* **Restricciones:** * Se deben solicitar todos los campos obligatorios: `nombre`, `poblacion`, `superficie en km2` y `continente`.
    * **No se permiten campos vacíos** ni valores nulos.
    * Se debe validar que los datos numéricos (población y superficie) sean enteros positivos.

### 2. Actualizar un País
* **Descripción:** Modifica la información de un país ya existente en la base de datos.
* **Campos modificables:** Únicamente se permite la actualización de los datos dinámicos:
    * `Población`
    * `Superficie`

### 3. Buscar un País por Nombre
* **Descripción:** Localiza un país específico dentro del dataset.
* **Flexibilidad:** Admite tanto **coincidencias exactas** como **coincidencias parciales** (por ejemplo, buscar "Ar" puede retornar "Argentina", "Armenia", etc.), ignorando mayúsculas y minúsculas.

### 4. Filtrar Países
Permite reducir el listado de países mostrados en pantalla aplicando los siguientes criterios de selección:
* **Por Continente:** Muestra solo los países pertenecientes al continente especificado (ej. "Asia", "América").
* **Por Rango de Población:** Filtra los países cuya población se encuentre entre un valor mínimo y un valor máximo definidos por el usuario.
* **Por Rango de Superficie:** Filtra los países cuya superficie en $km^2$ se encuentre dentro de un rango numérico específico.

### 5. Ordenar Países
Permite reestructurar la presentación visual de la lista de países. El usuario puede elegir el criterio de ordenamiento y el sentido del mismo:
* **Criterios de ordenación:**
    * Nombre (Alfabético)
    * Población
    * Superficie
      * Ascendente (de menor a mayor)
      * Descendente (de mayor a menor)

### 6. Mostrar Estadísticas del Dataset
Genera un reporte analítico resumido con métricas clave del dataset:
* **Criterios de reporte**  
    * mayor población 
    * menor población
    * Promedio general de población.
    * Promedio general de superficie en km^2
    * Cantidad total de países registrados por cada continente.

---

## 📊 Formato de los Datos

El programa trabaja nativamente con un formato de archivo plano (CSV) estructurado de la siguiente manera:

```csv
nombre,poblacion,superficie,continente
China,1425671000,9596961,Asia
Estados Unidos,339996563,9833517,América
Brasil,216422446,8515767,América