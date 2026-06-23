# ================================================================================== #
#                           SISTEMA DE INVENTARIO V2 (Checkeasy)                     #
# ================================================================================== #
# ---------------------------------------------------------------------------------- #
# ================================================================================== #
#                                    BASES DE DATOS                                  #
# ================================================================================== #

Inventario = {
# Este contenido es de prueba
    "Creatinas": [
        
        {
            "Nombre": "Creatina Monohidratada",
            "Marca": "Megaplex",
            "Cantidad": 10,
            "Precio": 80000,
            "Extras": {}
        },
        {
            "Nombre": "Creatina Hidrolizada",
            "Marca": "Megaplex",
            "Cantidad": 8,
            "Precio": 90000
        }

    ],
    "Proteinas": []

}

# --------------------------------- LIBRERIAS -------------------------------------- #

import re

def Sistema_Checkeasy():
    Gestionar_menu_principal()
# ================================================================================== #
#                                    MENU PRINCIPAL                                  #
# ================================================================================== #
def Presentar_menu_principal():
    print("\n")
    print("****************************************************************")
    print("*        Menu principal sistema de invetarios Easycheck        *")
    print("****************************************************************") 
    print("* 1. Categorias                                                *")
    print("* 2. Productos                                                 *")
    print("* 3. Invetario                                                 *")
    print("* 4. Salir                                                     *")
    print("****************************************************************")

def Opcion_menu_principal():
    while True:
        try:
            print("\n")
            Menu_principal = int(input("¿Que opcion deseas escoger?: "))
            if Menu_principal in [1, 2, 3, 4]:
                break
            else:
                print("\n")
                print("¡Opcion invalida!, debes escoger una opcion del menu...")
        except ValueError:
            print("\n")
            print("Error: ¡Solo puedes ingresar numeros!")        
    print("\n")
    return Menu_principal

def Gestionar_menu_principal():
    while True:
        Presentar_menu_principal()
        Procesar_opcion = Opcion_menu_principal()

        if Procesar_opcion == 1:
            Procesar_opcion_menu_categorias()
        
        elif Procesar_opcion == 2:
            Manejar_opciones_productos()

        elif Procesar_opcion == 3:
            print("En construccion...") 

        elif Procesar_opcion == 4:
            print("\n", "¡Haz salido con exito de Easycheck¡", "\n", "¡Te esperamos de vuelta!", "\n") 
            break
                

# =================================================================================== #
#                                 SISTEMA DE CATEGORIAS                               #
# =================================================================================== #

def Desplegar_menu_categorias():
    print("\n")
    print("****************************************************************")
    print("*                     Menu de categorias                       *")
    print("****************************************************************")
    print("* 1. Crear Categorias                                          *")
    print("* 2. Ver Categorias Registradas                                *")
    print("* 3. Eliminar Categorias                                       *")
    print("* 4. Volver menu principal                                     *")
    print("****************************************************************")     

def Opcion_menu_categorias():
    while True:
        try:
            print("\n")
            Menu_categorias = int(input("¿Que opcion deseas escoger?: "))
            print("\n")
            if Menu_categorias in [1, 2, 3, 4, 5]:
                break
            else:
                print("\n")
                print("¡Opcion invalida!, escoge una opcion del menu categorias... ")
        except  ValueError:
            print("¡Error!, solo puedes digitar numeros... ")
    return Menu_categorias
    
def Procesar_opcion_menu_categorias():
    while True:
        Desplegar_menu_categorias()
        Gestion_menu_categorias = Opcion_menu_categorias()

        if Gestion_menu_categorias == 1:
            Categoria = Crear_categorias() 
            print(f"¡Tu categoria: {Categoria[0]}, fue creada exitosamente!")

        elif Gestion_menu_categorias == 2:
            Mostrar_categorias()             

        elif Gestion_menu_categorias == 3:
            Eliminar_categorias()  

        elif Gestion_menu_categorias == 4:
            print("¡Haz salido de categorias con exito!")
            break            

# -------------------------------- CREAR CATEGORIAS --------------------------------- #

def Capturar_datos_categorias():
    while True:
        try:
            print("\n")
            Datos_ingresados = input("Nombre de la categoria que deseas crear: ").strip().title()
        
            if not Datos_ingresados:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in Datos_ingresados):
                print("\n")
                raise ValueError("La categoria debe contener al menos una letra o un número.")
            
            print("\n")
            print(f"Escribiste: '{Datos_ingresados}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return Datos_ingresados        

def Confirmar_guardado_categoria():
    Nombre_categoria = Capturar_datos_categorias()
    print("\n")
    print(f"¿Deseas guardar la categoria: {Nombre_categoria}")
    print("1. Si")
    print("2. No")
    def Entrada_usuario():
        while True:
            try:
                print("\n")
                Ingreso_opcion = int(input("¿Que opcion deseas escoger?: "))
                print("\n")
                if Ingreso_opcion in [1, 2]:
                    break
                else:
                    print("\n")
                    print("¡Opcion invalida!, escoge una opcion del menu categorias... ")
            except  ValueError:
                print("¡Error!, solo puedes digitar numeros... ")
        return Ingreso_opcion
    Recibir_opcion = Entrada_usuario()
    return Nombre_categoria, Recibir_opcion

def Agregar_categoria():
    Datos = Confirmar_guardado_categoria()
    Categoria_creada = Datos[0]
    Confirmacion = Datos[1]
    if Confirmacion == 1:
        Almacenaje_categoria = Inventario[Categoria_creada] = []
    elif Confirmacion == 2:
        Procesar_opcion_menu_categorias()     
    return Categoria_creada, Almacenaje_categoria

def Crear_categorias():    
    Datos = Agregar_categoria()
    Nombre_categoria = Datos[0]
    Categoria_guardada = Datos[1]
    return Nombre_categoria, Categoria_guardada

# ----------------------------------- VER CATEGORIAS ------------------------------- #

def Recorrer_existencias_categorias():
    Comprobacion = len(Inventario)
    return Comprobacion

def Recorrer_productos_existentes():
    Categorias_existentes = Recorrer_existencias_categorias()
    if Categorias_existentes >= 1:
        for Categoria, Productos in Inventario.items():
            Cantidad_categorias = Categoria
            Cantidad_productos = Productos
                        
    return Cantidad_categorias, Cantidad_productos                    

def Mostrar_categorias():
    diccionario_a_lista = list(Inventario)
    print("¡Estas son tus categorias existentes!:")
    for indice, Categoria in enumerate(diccionario_a_lista, start= 1):
        print(f"- {indice}. {Categoria}")
    

# ------------------------------- SISTEMA DE BUSQUEDA ------------------------------ #

def Validacion_entrada_busqueda():
    while True:
        try:
            print("\n")
            Datos_ingresados = input("Nombre de la categoria que deseas buscar: ").strip().title()
        
            if not Datos_ingresados:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in Datos_ingresados):
                print("\n")
                raise ValueError("La categoria debe contener al menos una letra o un número.")
            
            print("\n")
            print(f"Escribiste: '{Datos_ingresados}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return Datos_ingresados   

def Datos_busqueda_Categorias():
    print("\n")
    print("¡Que categoria deseas eliminar!")
    Entrada_datos = Validacion_entrada_busqueda()
    Categoria_cantidad_encontrada = Inventario[Entrada_datos]
    Nombre_categoria = Entrada_datos
    return Categoria_cantidad_encontrada, Nombre_categoria

def Busqueda_categorias():
    print("\n")
    print("¡Que categoria deseas buscar!")
    Entrada_datos = Validacion_entrada_busqueda()
    Categoria_cantidad_encontrada = Inventario[Entrada_datos]
    Nombre_categoria = Entrada_datos
    return Categoria_cantidad_encontrada, Nombre_categoria

# ---------------------------- ELIMINAR CATEGORIAS ---------------------------------- # 
def Obtener_respuesta_numerica():
    while True:
        try:
            print("\n")
            Respuesta = int(input("¿Que opcion deseas escoger?: "))
            if Respuesta in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
                break
            else:
                print("\n")
                print("¡Opcion invalida!, escoge una opcion ofrecida... ")
        except  ValueError:
            print("¡Error!, solo puedes digitar numeros... ")
    return Respuesta        

def Condicion_eliminar_categoria():
    Datos = Datos_busqueda_Categorias()
    Datos_01 = len(Datos[0])
    Datos_02 = Datos[1]
    if Datos_01 == 0:
        Inventario.pop(Datos_02)
        print("\n")
        print("¡Tu categoria ha sido eliminada con exito!")
    elif Datos_01 >= 1:
        print("\n")
        print("¡Error!, no puedes eliminar una categoria, que contiene productos...")

def Eliminar_categorias():
    Mostrar_categorias() 
    Condicion_eliminar_categoria() 

# =================================================================================== #
#                                 SISTEMA DE PRODUCTOS                                #
# =================================================================================== #

def Desplegar_menu_productos():
    print("\n")
    print("****************************************************************")
    print("*                       Menu productos                         *")
    print("****************************************************************")
    print("* 1. Crear producto/s                                          *")
    print("* 2. Ver productos                                             *")
    print("* 3. Eliminar productos                                        *")
    print("* 4. Buscar productos                                          *")
    print("* 5. Editar productos                                          *")
    print("* 6. Volver al menu                                            *")
    print("****************************************************************")

def Opcion_menu_productos():
    while True:
        try:
            print("\n")
            Menu_principal = int(input("¿Que opcion deseas escoger?: "))
            if Menu_principal in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("\n")
                print("¡Opcion invalida!, debes escoger una opcion del menu...")
        except ValueError:
            print("\n")
            print("Error: ¡Solo puedes ingresar numeros!")        
    print("\n")
    return Menu_principal

def Manejar_opciones_productos():
    while True:
        Desplegar_menu_productos()
        Procesar_opcion = Opcion_menu_productos()

        if Procesar_opcion == 1:
            Crear_Productos()
        
        elif Procesar_opcion == 2:
            Mostrar_productos()

        elif Procesar_opcion == 3:
            Eliminar_productos()
        
        elif Procesar_opcion == 4:
            Buscar_o_ver_productos()           

        elif Procesar_opcion == 5:
            Editar_productos() 

        elif Procesar_opcion == 6:
            print("\n")
            print("¡Has salido con exito de productos")
            break
                  
# ------------------------------- VALIDACIONES DE RESPUESTAS ----------------------- #

def Validacion_confirmacion_respuesta():
    while True:
        try:
            print("\n")
            Validacion = int(input("¿Que opcion deseas escoger?: "))
            if Validacion in [1, 2]:
                break
            else:
                print("\n")
                print("¡Opcion invalida!, debes escoger una opcion...")
        except ValueError:
            print("\n")
            print("Error: ¡Solo puedes ingresar numeros!")        
    print("\n")
    return Validacion

def Confirmacion_respuesta():
    print("\n")
    print("¡Confirma tu respuesta!")
    print("1. Si")
    print("2. No")
    Respuesta = Validacion_confirmacion_respuesta()
    return Respuesta

# ------------------------------------ CREAR PRODUCTOS ----------------------------- #

def Caracteristicas_validacion_palabras():
    while True:
        try:
            print("\n")
            producto = input("Ingresa la caracteristica de tu producto: ").strip().title()
        
            if not producto:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in producto):
                print("\n")
                raise ValueError("El producto debe contener al menos una letra o un número.")
            
            print("\n")
            print(f"Escribiste: '{producto}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return producto

def Caracteristicas_validacion_numeros():
    while True:
        try:
            print("\n")
            producto = input("Ingresa la caracteristica de tu producto: ").strip().title()
        
            if not producto:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isdigit() for caracter in producto):
                print("\n")
                raise ValueError("El producto debe contener al menos un un número.")
            
            print("\n")
            print(f"Escribiste: '{producto}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return producto

def Datos_productos():
    print("\n")
    print("¡Ingresa los siguientes datos para crear tu producto!")
    print("\n")
    print("¿Con que nombre vas a identificar tu producto?")
    Nombre = Caracteristicas_validacion_palabras()
    print("\n")
    print("¿Cual es la marca de tu producto?")
    print("\n")
    Marca = Caracteristicas_validacion_palabras()
    print("\n")
    print("¿Cual es el precio de tu producto?:")
    Precio = Caracteristicas_validacion_numeros()
    print("\n")
    print("¿Cual es la cantidad fisica de tu producto:")
    Cantidad = Caracteristicas_validacion_numeros()
    print("\n")
    print("¿Cual es el codigo de tu producto?")
    Codigo = Caracteristicas_validacion_numeros()
    return Nombre, Marca, Precio, Cantidad, Codigo

def Caracteristicas_productos():
    Mostrar_categorias()
    Datos =  Busqueda_categorias()
    Productos = Datos[0]
    Categoria_buscada = Datos[1]
    if len(Productos) == 0:
        print("\n")
        print(f"¡La categoria {Categoria_buscada} tiene {len(Productos)} productos!")
        print("\n")
        print(f"¿Deseas crear un producto para la categoria {Categoria_buscada}?")
        Confirmar_respuesta = Confirmacion_respuesta()
        if Confirmar_respuesta == 1:
            def Agregar_productos():
                Datos = Datos_productos()
                Dato_nombre = Datos[0]
                Dato_marca = Datos[1]
                Dato_precio = Datos[2]
                Dato_cantidad = Datos[3]
                Dato_codigo = Datos[4]
                print("\n")
                print("¿Los datos ingresados son correctos?")
                print(f"Nombre: {Dato_nombre}")
                print(f"Marca: {Dato_marca}")
                print(f"Precio: {Dato_precio}")
                print(f"Cantidad: {Dato_cantidad}")
                print(f"Codigo interno: {Dato_codigo}")
                confirmar_datos =  Confirmacion_respuesta()

                if confirmar_datos == 1:
                    Agregar_diccionario = Inventario[Categoria_buscada].append({"Nombre": Dato_nombre, "Marca": Dato_marca, "Precio": Dato_precio, "Cantidad": Dato_cantidad, "Codigo": Dato_codigo})
                    print("\n")
                    print(f"¡Tu producto {Dato_nombre} fue agregado con exito a la categoria {Categoria_buscada}!")
                    print("\n")                                     
            Agregar_producto = Agregar_productos()                        
        elif Confirmar_respuesta == 2:
            Manejar_opciones_productos()
    return Agregar_producto

def Crear_Productos():
    Informacion_productos = Caracteristicas_productos() 
      
# ----------------------------------- BUSCAR PRODUCTOS ----------------------------- #

def Validacion_entrada_productos():
    while True:
        try:
            print("\n")
            producto = input("Nombre del producto que deseas buscar: ").strip().title()
        
            if not producto:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in producto):
                print("\n")
                raise ValueError("El producto debe contener al menos una letra o un número.")
            
            print("\n")
            print(f"Escribiste: '{producto}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return producto

def Buscar_o_ver_productos():
    Mostrar_categorias()
    Datos =  Busqueda_categorias()
    Productos_en_categoria = Datos[0] # diccionario completo de producto
    Nombre_categoria_buscada = Datos[1] # nombre exacto categoria
    Nombre_del_producto = Validacion_entrada_productos() # nombre del producto buscado
    for clave in Productos_en_categoria:
        if clave["Nombre"] == Nombre_del_producto:
            print("\n")
            print(f"El producto encontrado ({Nombre_del_producto}) contiene:")
            for llave in clave:
                print(f"- {llave}: {clave[llave]}")
            print("\n")
        elif clave["Nombre"] != Nombre_del_producto:
            print("¡Error!, nombre incorrecto, o el producto no existe...")
     

# --------------------------------- MOSTRAR PRODUCTOS ------------------------------ #

def Mostrar_productos():
    Mostrar_categorias()
    Datos =  Busqueda_categorias()
    Productos = Datos[0]
    Categoria_buscada = Datos[1]
    if len(Productos) == 0:
        print("\n")
        print(f"¡La categoria {Categoria_buscada} tiene {len(Productos)} productos!")
        print("\n")
        print(f"¿Deseas crear un producto para la categoria {Categoria_buscada}?")
        Confirmar_respuesta = Confirmacion_respuesta()
        if Confirmar_respuesta == 1:
            Caracteristicas_productos()
        elif Confirmar_respuesta == 2:
            Manejar_opciones_productos()    
    elif len(Productos) >= 1:     
        print("\n")
        print(f"La categoria {Categoria_buscada} contiene {len(Productos)} productos:")
        print("\n")
        for clave in Productos:
            print(f"Producto registrado:")
            for llave in clave:
                print(f"- {llave}: {clave[llave]}")
            print("\n")
                

# --------------------------------- ELIMINAR PRODUCTOS ----------------------------- #

def Validacion_eliminar():
    while True:
        try:
            print("\n")
            producto = input("Ingresa el nombre del tu producto: ").strip().title()
        
            if not producto:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in producto):
                print("\n")
                raise ValueError("El producto debe contener al menos una letra.")
            
            print("\n")
            print(f"Escribiste: '{producto}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return producto


    Mostrar_categorias()
    Datos =  Busqueda_categorias()
    Productos = Datos[0]
    Categoria_buscada = Datos[1]
    if len(Productos) == 0:
        print("\n")
        print(f"¡La categoria {Categoria_buscada} tiene {len(Productos)} productos!")
        print("\n")
        print(f"¿Deseas crear un producto para la categoria {Categoria_buscada}?")
        Confirmar_respuesta = Confirmacion_respuesta()
        if Confirmar_respuesta == 1:
            Caracteristicas_productos()
        elif Confirmar_respuesta == 2:
            Manejar_opciones_productos()    
    elif len(Productos) >= 1:     
        print("\n")
        print(f"La categoria {Categoria_buscada} contiene {len(Productos)} productos:")
        print("\n")
        for clave in Productos:
            print(f"Producto registrado:")
            for llave in clave: # clave diccionario -- llave nombres o caracteristicas
                print(f"- llave {clave[llave]}")
                print(f" clave: {clave}")
                print(f"- tipo de llave {type(clave[llave])}")
                print(f" tipo clave: {type(clave)}")
            print("\n")
                              
def Eliminar_productos():
    Mostrar_categorias()
    Datos =  Busqueda_categorias()
    Productos_en_categoria = Datos[0] # diccionario completo de producto
    Nombre_categoria_buscada = Datos[1] # nombre exacto categoria
    Nombre_del_producto = Validacion_entrada_productos() # nombre del producto buscado
    for clave in Productos_en_categoria:
        if clave["Nombre"] == Nombre_del_producto:
            print("\n")
            print(f"El producto encontrado ({Nombre_del_producto}) contiene:")
            for llave in clave:
                print(f"- {llave}: {clave[llave]}")
            print("\n") 
            print(f"¡Tu producto {Nombre_del_producto} fue borrado exitosamente!")
            Productos_en_categoria.remove(clave)
            break    
    if clave["Nombre"] != Nombre_del_producto:
        print("¡Error!, nombre incorrecto, o el producto no existe...")      
     
# --------------------------------- EDITAR PRODUCTOS ------------------------------- #

def validacion_editar():
    while True:
        try:
            print("\n")
            producto = input("Ingresa la caracteristica del tu producto: ").strip().title()
        
            if not producto:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in producto):
                print("\n")
                raise ValueError("El producto debe contener al menos una letra.")
            
            print("\n")
            print(f"Escribiste: '{producto}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return producto

def Nuevo_valor():
    while True:
        try:
            print("\n")
            producto = input("Ingresa el nuevo valor del tu producto: ").strip().title()
        
            if not producto:
                print("\n")
                raise ValueError("El campo no puede estar vacío.")
            
            if not any(caracter.isalnum() for caracter in producto):
                print("\n")
                raise ValueError("El producto debe contener al menos una letra o numero.")
            
            print("\n")
            print(f"Escribiste: '{producto}'")
            break 
        
        except ValueError as error:
            print("\n")
            print(f" Error: {error}")
    return producto

def Editar_productos():
    Mostrar_categorias()
    Datos =  Busqueda_categorias()
    Productos_en_categoria = Datos[0] # diccionario completo de producto
    Nombre_categoria_buscada = Datos[1] # nombre exacto categoria
    Nombre_del_producto = Validacion_entrada_productos() # nombre del producto buscado
    for clave in Productos_en_categoria:
        if clave["Nombre"] == Nombre_del_producto:
            print("\n")
            print(f"El producto encontrado ({Nombre_del_producto}) contiene:")
            for llave in clave:
                print(f"- {llave}: {clave[llave]}")
            print("\n") 
            print(f"¿Que caracteristica del producto {Nombre_del_producto} deseas modificar?")
            Caracteristica_editar = validacion_editar()
            for Editar in clave:
                if Editar == Caracteristica_editar: 
                    Nuevo_elemento = Nuevo_valor()
                    clave[Caracteristica_editar] = Nuevo_elemento
                    print("\n")
                    print("¡Tu nuevo valor a sido editado con exito!")
            break    
    if clave["Nombre"] != Nombre_del_producto:
        print("¡Error!, nombre incorrecto, o el producto no existe...")    

# ---------------------------------------------------------------------------------- #

Sistema_Checkeasy()

