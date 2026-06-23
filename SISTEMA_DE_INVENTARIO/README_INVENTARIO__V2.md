# SISTEMA_INVENTARIO_V2

## Descripción

Sistema de gestión de inventario desarrollado en Python para continuar el proceso de aprendizaje de estructuras de datos, diseño de software y organización de proyectos.

Esta versión busca mejorar la arquitectura de INVENTARIO_V1 mediante una mejor organización de menús, validaciones y flujo de usuario.

El objetivo principal no es crear un sistema empresarial completo, sino construir una versión más estructurada y mantenible utilizando los conocimientos actuales.

---

# Objetivos de Aprendizaje

* Mejorar la organización del código.
* Practicar estructuras de datos anidadas.
* Diseñar sistemas más cercanos a escenarios reales.
* Reducir la repetición de lógica.
* Preparar el proyecto para una futura refactorización con funciones.
* Fortalecer habilidades de análisis y diseño antes de programar.

---

# Menú Principal

```text
1. Categorías
2. Productos
3. Inventario
4. Salir
```

---

# Módulo Categorías

Permite administrar las categorías del inventario.

## Funcionalidades

```text
1. Crear Categoría
2. Ver Categorías
3. Eliminar Categoría
4. Volver
```

## Reglas

* No se pueden crear categorías duplicadas.
* Solo se pueden eliminar categorías vacías.
* Si una categoría contiene productos, no podrá ser eliminada.

---

# Módulo Productos

Permite administrar los productos registrados en el sistema.

## Funcionalidades

```text
1. Crear Producto
2. Ver Productos
3. Buscar Producto
4. Editar Producto
5. Eliminar Producto
6. Volver
```

## Reglas

* No se pueden crear productos si no existen categorías.
* Todo producto debe pertenecer a una categoría existente.
* El sistema debe guiar al usuario cuando falten requisitos previos.

---

# Módulo Inventario

Permite consultar la información almacenada.

## Funcionalidades

```text
1. Ver Inventario Completo
2. Ver Productos por Categoría
3. Volver
```

---

# Estructura General

El sistema utiliza una estructura basada en categorías que contienen productos.

Ejemplo conceptual:

```python
Inventario = {
    "Creatinas": [
        {
            "Nombre": "Creatina Micronizada",
            "Marca": "Optimum Nutrition",
            "Costo": 85000,
            "Precio": 103500,
            "Stock": 20
        }
    ]
}
```

---

# Información de los Productos

Cada producto debe contener como mínimo:

```text
Nombre
Marca
Costo
Precio
Stock
```

---

# Flujo del Sistema

El sistema está diseñado para guiar al usuario y evitar desorden en la información.

Ejemplo:

```text
Crear Producto
↓
No existen categorías
↓
Crear Categoría
↓
Categoría creada
↓
Volver automáticamente al flujo de creación de producto
```

---

# Restricciones del Sistema

* No crear productos sin categorías.
* No eliminar categorías con productos registrados.
* Evitar datos huérfanos.
* Mantener la organización del inventario.
* Guiar al usuario cuando una acción requiera pasos previos.

---

# Alcance de la Versión V2

Incluye:

* Categorías.
* Productos.
* Consulta de inventario.
* Validaciones básicas.
* Estructuras anidadas.

No incluye:

* JSON.
* Archivos.
* Base de datos.
* Programación orientada a objetos.
* Sistema de usuarios.
* Permisos.
* Historial de movimientos.
* Reportes avanzados.

---

# Objetivo Final

Construir una versión más organizada y escalable que INVENTARIO_V1, aplicando principios de diseño y estructura de datos que servirán como base para futuras versiones con funciones, JSON, modularización y persistencia de información.
