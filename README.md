# Sistema de Gestión de Datos de Países

Este proyecto es una aplicación diseñada para la gestión, visualización y análisis estadístico de un dataset de países. Permite realizar operaciones CRUD básicas, búsquedas avanzadas, filtros personalizados, ordenamiento de datos y cálculo de métricas estadísticas a partir de un archivo de datos estructurado (como un archivo CSV).

## 📋 Estructura del Menú y Funcionalidades

El programa cuenta con un menú interactivo que ofrece las siguientes opciones y capacidades:

<img width="226" height="174" alt="Screenshot_20260609_005247" src="https://github.com/user-attachments/assets/88e4952a-9d68-4c0f-b74e-208bc6d18bfd" />

### 1. Agregar un País
* **Descripción:** Permite registrar un nuevo país dentro del sistema.
* **Restricciones:** * Se deben solicitar todos los campos obligatorios: `nombre`, `poblacion`, `superficie en km2` y `continente`.
    * **No se permiten campos vacíos** ni valores nulos.
    * Se debe validar que los datos numéricos (población y superficie) sean enteros positivos.
<img width="250" height="99" alt="Screenshot_20260609_005054" src="https://github.com/user-attachments/assets/6ab44d04-d8a7-421f-b1eb-fb99c5ad971e" />



### 2. Actualizar un País
* **Descripción:** Modifica la información de un país ya existente en la base de datos.
* **Campos modificables:** Únicamente se permite la actualización de los datos dinámicos:
    * `Población`
    * `Superficie`
      
<img width="448" height="81" alt="Screenshot_20260609_005536" src="https://github.com/user-attachments/assets/f2e48330-121d-4a94-9043-58273531fa5f" />


### 3. Buscar un País por Nombre
* **Descripción:** Localiza un país específico dentro del dataset.
* **Flexibilidad:** Admite tanto **coincidencias exactas** como **coincidencias parciales** (por ejemplo, buscar "Ar" puede retornar "Argentina", "Armenia", etc.), ignorando mayúsculas y minúsculas.
<img width="667" height="81" alt="Screenshot_20260609_005653" src="https://github.com/user-attachments/assets/cb4444a6-fd24-4eab-a42b-154ecbd7a18e" />


### 4. Filtrar Países
Permite reducir el listado de países mostrados en pantalla aplicando los siguientes criterios de selección:

<img width="169" height="98" alt="Screenshot_20260609_005739" src="https://github.com/user-attachments/assets/f57165f6-ba48-4f77-86e4-035918b50018" />

* **Por Continente:** Muestra solo los países pertenecientes al continente especificado (ej. "Asia", "América").
<img width="687" height="152" alt="Screenshot_20260609_005904" src="https://github.com/user-attachments/assets/1c2e396c-4219-4f2f-8ece-aebaac24b038" />

* **Por Rango de Población:** Filtra los países cuya población se encuentre entre un valor mínimo y un valor máximo definidos por el usuario.
  
<img width="659" height="124" alt="Screenshot_20260609_010130" src="https://github.com/user-attachments/assets/9bf367fa-20c0-417c-9272-3ef42e41a66a" />

* **Por Rango de Superficie:** Filtra los países cuya superficie en $km^2$ se encuentre dentro de un rango numérico específico.

<img width="659" height="114" alt="Screenshot_20260609_010307" src="https://github.com/user-attachments/assets/40ab7f0c-f5b1-4cbd-9288-b6c3cf87769f" />

### 5. Ordenar Países
Permite reestructurar la presentación visual de la lista de países. El usuario puede elegir el criterio de ordenamiento y el sentido del mismo:

<img width="187" height="103" alt="Screenshot_20260609_010403" src="https://github.com/user-attachments/assets/7da4fefa-a8f1-477b-af9d-440d43e8a7de" />

* **Criterios de ordenación:**
  
    * Nombre (Alfabético)
   <img width="659" height="217" alt="Screenshot_20260609_010351" src="https://github.com/user-attachments/assets/602cb4ec-30c2-470f-97b9-c7fdf5939a17" />

    * Población
   <img width="676" height="216" alt="Screenshot_20260609_010504" src="https://github.com/user-attachments/assets/b788d545-4579-4d53-b937-7aa82d16bc17" />

    * Superficie
   <img width="206" height="76" alt="Screenshot_20260609_010717" src="https://github.com/user-attachments/assets/47790b3d-ae5d-441a-9d13-9e272374d58a" />

    * Ascendente (de menor a mayor)
  <img width="670" height="218" alt="Screenshot_20260609_010901" src="https://github.com/user-attachments/assets/6587ed94-b3d7-45c7-b085-37017beab3a0" />

    * Descendente (de mayor a menor)
   <img width="670" height="218" alt="Screenshot_20260609_010912" src="https://github.com/user-attachments/assets/b0715514-3bfa-4c9b-9f7a-54514f198ca2" />


### 6. Mostrar Estadísticas del Dataset
Genera un reporte analítico resumido con métricas clave del dataset:

<img width="279" height="124" alt="Screenshot_20260609_011211" src="https://github.com/user-attachments/assets/18b0e5db-c6d8-41d7-9aba-35c2ee1b5c17" />

* **Criterios de reporte**  
    * mayor población y menor población
  <img width="668" height="143" alt="Screenshot_20260609_011427" src="https://github.com/user-attachments/assets/06975af1-77de-4d8d-b944-bc6b897a80c8" />

    * Promedio general de población.
  <img width="281" height="37" alt="Screenshot_20260609_011501" src="https://github.com/user-attachments/assets/1ba974f4-fba7-4ee4-84b4-2f2c9732cf92" />

    * Promedio general de superficie en km^2
  <img width="316" height="37" alt="Screenshot_20260609_011537" src="https://github.com/user-attachments/assets/7936619a-c165-4e88-9f33-6a361649fc66" />

    * Cantidad total de países registrados por cada continente.
  <img width="328" height="147" alt="Screenshot_20260609_011628" src="https://github.com/user-attachments/assets/fd78396b-9c23-4df9-a27d-72ab7683de38" />


---

## 📊 Formato de los Datos

El programa trabaja nativamente con un formato de archivo plano (CSV) estructurado de la siguiente manera:

```csv
nombre,poblacion,superficie,continente
China,1425671000,9596961,Asia
Estados Unidos,339996563,9833517,América
Brasil,216422446,8515767,América
