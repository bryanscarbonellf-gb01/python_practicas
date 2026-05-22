# DATOS BASE #

numero_secreto = 7

intentos = 0

# BUCLE #

while intentos != numero_secreto:
    
    intentos = int(input("Ingresa tu numero para ganar ¡AQUI! "))
    
    if intentos == numero_secreto:
        print("¡Eres el feliz GANADOR!")
        break

    elif intentos < numero_secreto:
        print("¡CERCA!, un poco mas arriba, sigue intentando")

    elif intentos > numero_secreto:
        print("¡CASI!, esta vez te pasaste")