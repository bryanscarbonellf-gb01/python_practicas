                INVENTARIO V 1

Entender qué problema resuelve el sistema.

R//

Negocio: Tienda de suplementos

Productos:
- Proteínas
- Creatinas
- Pre-entrenos
- Vitaminas
- etc.

Estructura de datos: 

Inventario
│
├── Creatinas
│   ├── Producto
│   ├── Producto
│   └── Producto
│
├── Proteínas
│   ├── Producto
│   └── Producto
│
├── Pre-entrenos
│   └── Producto
│
└── Categorías nuevas
# ========================================================= #
# ====== SISTEMA DE INVENTARIO PARA TIENDA DE SUPLEMENTOS V1====== #
# ========================================================= #

# FLUJO DEL SISTEMA

# FASE 1
# OBJETIVO: Crear la estructura principal del sistema.

# 1. Crear inventario vacío.
# 2. Crear menú principal.
# 3. Crear while True.
# 4. Crear opción salir.
# 5. Validar opciones del menú.

# RESULTADO ESPERADO:
#
# 1. Crear categoría
# 2. Ver categorías
# 3. Agregar producto
# 4. Ver productos por categoría
# 5. Salir
#
# El sistema navega correctamente.


# ========================================================= #


# FASE 2
# OBJETIVO: Crear categorías dinámicamente.

# 1. Pedir nombre de categoría.
# 2. Validar si existe.
# 3. Crear categoría.
# 4. Guardar categoría dentro del inventario.
# 5. Mostrar confirmación.

# RESULTADO ESPERADO:
#
# Categoría creada:
# Creatinas
#
# Categoría creada:
# Proteínas
#
# Categoría creada:
# Vitaminas


# ========================================================= #


# FASE 3
# OBJETIVO: Mostrar categorías registradas.

# 1. Recorrer inventario.
# 2. Mostrar categorías existentes.
# 3. Mostrar mensaje si no existen categorías.

# RESULTADO ESPERADO:
#
# Categorías registradas:
#
# 1. Creatinas
# 2. Proteínas
# 3. Vitaminas


# ========================================================= #


# FASE 4
# OBJETIVO: Agregar productos a una categoría.

# 1. Seleccionar categoría.
# 2. Pedir nombre del producto.
# 3. Pedir marca.
# 4. Pedir precio.
# 5. Pedir cantidad.
# 6. Crear diccionario producto.
# 7. Guardar producto en la categoría.

# RESULTADO ESPERADO:
#
# Nombre:
# Creatina Micronizada
#
# Marca:
# Optimum Nutrition
#
# Precio:
# 103500
#
# Cantidad:
# 20
#
# Producto agregado correctamente.


# ========================================================= #


# FASE 5
# OBJETIVO: Mostrar productos de una categoría.

# 1. Mostrar categorías.
# 2. Elegir categoría.
# 3. Recorrer productos.
# 4. Mostrar información de cada producto.

# RESULTADO ESPERADO:
#
# CATEGORÍA: CREATINAS
#
# Nombre: Creatina Micronizada
# Marca: Optimum Nutrition
# Precio: 103500
# Cantidad: 20


# ========================================================= #

# ========================================================= #
# ====== SISTEMA DE INVENTARIO PARA TIENDA DE SUPLEMENTOS V2====== #
# ========================================================= #

# FASE 6
# OBJETIVO: Buscar producto por nombre.

# 1. Pedir nombre.
# 2. Recorrer inventario.
# 3. Comparar nombres.
# 4. Mostrar producto encontrado.
# 5. Mostrar mensaje si no existe.

# RESULTADO ESPERADO:
#
# Buscar:
# Creatina
#
# Producto encontrado.


# ========================================================= #


# FASE 7
# OBJETIVO: Actualizar stock.

# 1. Buscar producto.
# 2. Mostrar cantidad actual.
# 3. Pedir nueva cantidad.
# 4. Actualizar inventario.

# RESULTADO ESPERADO:
#
# Cantidad anterior: 20
# Cantidad nueva: 35


# ========================================================= #


# FASE 8
# OBJETIVO: Mostrar resumen del inventario.

# 1. Contar categorías.
# 2. Contar productos.
# 3. Mostrar total de unidades.
# 4. Mostrar valor total del inventario.

# RESULTADO ESPERADO:
#
# Categorías: 5
# Productos: 28
# Unidades: 340
# Valor inventario: $12.450.000


# ========================================================= #


# FASE 9
# OBJETIVO: README Y DOCUMENTACIÓN.

# 1. Explicar funcionamiento.
# 2. Explicar estructura de datos.
# 3. Explicar limitaciones de V1.
# 4. Explicar mejoras para V2.


# ========================================================= #


# INVENTARIO_V1 TERMINADO
#
# Conceptos practicados:
#
# - while
# - if / elif / else
# - for
# - listas
# - diccionarios
# - listas dentro de diccionarios
# - diccionarios dentro de listas
# - validaciones
# - menús
# - modelado de datos
# - lógica de negocio
#
# Evolución esperada:
#
# INVENTARIO_V1
# ↓
# INVENTARIO_V2 (funciones)
# ↓
# INVENTARIO_V3 (archivos JSON)
# ↓
# INVENTARIO_V4 (ventas y facturación)


