#EJERCICIO 1


while True:
    nombre = input("Cliente: ").strip() 
    if nombre.isalpha(): 
        break
    else:
        print("Error: Ingresa un nombre válido (solo letras, sin espacios ni números).")


while True:
    cantidad_str = input("Cantidad de productos: ").strip()
    if cantidad_str.isdigit(): 
        cantidad = int(cantidad_str)
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad debe ser mayor a 0.")
    else:
        print("Error: Ingresa un número entero positivo.")


total_sin_descuentos = 0
total_con_descuentos = 0


for i in range(1, cantidad + 1):
    print(f"\n--- Producto {i} ---")
    

    while True:
        precio_str = input(f"Producto {i} - Precio: ").strip()
        if precio_str.isdigit():
            precio = int(precio_str)
            break
        else:
            print("Error: Ingresa un precio válido (número entero).")
            
 
    while True:
        descuento = input("Descuento (S/N): ").strip().lower() 
        if descuento == 's' or descuento == 'n':
            break
        else:
            print("Error: Ingresa solo 'S' para sí o 'N' para no.")
            
    
    total_sin_descuentos += precio
    

    if descuento == 's':
        precio_final = precio * 0.90 
    else:
        precio_final = precio
        
  
    total_con_descuentos += precio_final


ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print("\n" + "="*30) 
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#EJERCICIO 2



usuario_correcto = "alumno"
clave_correcta = "python123"


intentos_maximos = 3
intentos_actuales = 0
acceso_permitido = False


while intentos_actuales < intentos_maximos:
    print(f"Intento {intentos_actuales + 1}/{intentos_maximos}")
    usuario_ingresado = input("Usuario: ").strip()
    clave_ingresada = input("Clave: ").strip()
    
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.\n")
        acceso_permitido = True
        break 
    else:
        print("Error: credenciales inválidas.\n")
        intentos_actuales += 1


if not acceso_permitido:
    print("Cuenta bloqueada.")
else:
   
    while True:
        print("\n--- Menú Principal ---")
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")
        
        opcion_str = input("Opción: ").strip()
        
     
        if not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            continue 
            
        opcion = int(opcion_str)
        
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue
            
     
        if opcion == 1:
            print("Estado: Inscripto")
            
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ").strip()
            
          
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar nueva clave: ").strip()
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave 
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
                    
        elif opcion == 3:
            print("¡Sigue programando! Cada línea de código te hace más experto.")
            
        elif opcion == 4:
            print("Cerrando sesión. ¡Hasta pronto!")
            break 

#EJERCICIO 3


while True:
    operador = input("Nombre del operador: ").strip()
    if operador.isalpha():
        break
    else:
        print("Error: Ingresa un nombre válido (solo letras, sin espacios).")



lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""


martes1 = ""
martes2 = ""
martes3 = ""


while True:
    print(f"\n--- Agenda de Turnos | Operador: {operador} ---")
    print("1) Reservar turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    
    opcion_str = input("Selecciona una opción: ").strip()
    
   
    if not opcion_str.isdigit():
        print("Error: Ingresa un número válido.")
        continue
        
    opcion = int(opcion_str)
    
    if opcion < 1 or opcion > 5:
        print("Error: Opción fuera de rango (1-5).")
        continue

   
    if opcion == 1:
        while True:
            dia_str = input("Día a reservar (1=Lunes, 2=Martes): ").strip()
            if dia_str == "1" or dia_str == "2":
                dia = int(dia_str)
                break
            else:
                print("Error: Ingresa 1 para Lunes o 2 para Martes.")
                
        while True:
            paciente = input("Nombre del paciente: ").strip()
            if paciente.isalpha():
                break
            else:
                print("Error: Ingresa un nombre válido (solo letras).")
                
        if dia == 1: 
            
            if lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                print("Error: No hay cupos disponibles el Lunes.")
           
            elif paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El paciente ya tiene un turno asignado el Lunes.")
            
            else:
                if lunes1 == "":
                    lunes1 = paciente
                elif lunes2 == "":
                    lunes2 = paciente
                elif lunes3 == "":
                    lunes3 = paciente
                elif lunes4 == "":
                    lunes4 = paciente
                print("Turno reservado con éxito.")
                
        elif dia == 2: # MARTES
            
            if martes1 != "" and martes2 != "" and martes3 != "":
                print("Error: No hay cupos disponibles el Martes.")
            
            elif paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El paciente ya tiene un turno asignado el Martes.")
           
            else:
                if martes1 == "":
                    martes1 = paciente
                elif martes2 == "":
                    martes2 = paciente
                elif martes3 == "":
                    martes3 = paciente
                print("Turno reservado con éxito.")

   
    elif opcion == 2:
        while True:
            dia_str = input("Día a cancelar (1=Lunes, 2=Martes): ").strip()
            if dia_str == "1" or dia_str == "2":
                dia = int(dia_str)
                break
            else:
                print("Error: Ingresa 1 o 2.")
                
        while True:
            paciente = input("Nombre del paciente a cancelar: ").strip()
            if paciente.isalpha():
                break
            else:
                print("Error: Ingresa solo letras.")
                
        cancelado = False 
        
        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
                
        elif dia == 2:
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True
                
        if cancelado:
            print("Turno cancelado exitosamente.")
        else:
            print("Error: Paciente no encontrado en ese día.")

   
    elif opcion == 3:
        while True:
            dia_str = input("Día a ver (1=Lunes, 2=Martes): ").strip()
            if dia_str == "1" or dia_str == "2":
                dia = int(dia_str)
                break
            else:
                print("Error: Ingresa 1 o 2.")
                
        if dia == 1:
            print("\n--- Agenda LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == 2:
            print("\n--- Agenda MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

   
    elif opcion == 4:
        
        ocupados_l = 0
        if lunes1 != "": ocupados_l += 1
        if lunes2 != "": ocupados_l += 1
        if lunes3 != "": ocupados_l += 1
        if lunes4 != "": ocupados_l += 1
        
        
        ocupados_m = 0
        if martes1 != "": ocupados_m += 1
        if martes2 != "": ocupados_m += 1
        if martes3 != "": ocupados_m += 1
        
        libres_l = 4 - ocupados_l
        libres_m = 3 - ocupados_m
        
        print("\n--- Resumen General ---")
        print(f"LUNES:  {ocupados_l} ocupados | {libres_l} disponibles")
        print(f"MARTES: {ocupados_m} ocupados | {libres_m} disponibles")
        
        if ocupados_l > ocupados_m:
            print("Día con más turnos: LUNES")
        elif ocupados_m > ocupados_l:
            print("Día con más turnos: MARTES")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")

    
    elif opcion == 5:
        print("Cerrando el sistema. ¡Hasta luego!")
        break 

#EJERCICIO 4


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0 


while True:
    agente = input("Nombre del agente: ").strip()
    if agente.isalpha():
        break
    print("Error: El nombre solo debe contener letras.")

print(f"\n¡Bienvenido, Agente {agente.capitalize()}! La bóveda te espera.")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
   
    if alarma and tiempo <= 3:
        break 

   
    estado_alarma = "ACTIVADA" if alarma else "Desactivada"
    print("\n" + "="*40)
    print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {estado_alarma} | Código parcial: '{codigo_parcial}' ({len(codigo_parcial)} caracteres)")
    print("="*40)

   
    print("1. Forzar cerradura (Costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel    (Costo: -10 energía, -3 tiempo)")
    print("3. Descansar        (Costo: +15 energía, -1 tiempo)")
    
    while True:
        opcion_str = input("Selecciona una acción (1-3): ").strip()
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            if 1 <= opcion <= 3:
                break
        print("Error: Ingresa un número válido del 1 al 3.")

   
    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        
        
        if forzar_seguidas == 3:
            print("\n¡LA CERRADURA SE TRABÓ! Has intentado forzarla 3 veces seguidas.")
            print("Se activa la alarma y NO abres la cerradura.")
            alarma = True
        else:
            
            if energia < 40:
                print("\n⚠️ ¡Energía baja! Riesgo de activar la alarma.")
                while True:
                    calib_str = input("Calibra la presión (Elige un número del 1 al 3): ").strip()
                    if calib_str.isdigit():
                        calib = int(calib_str)
                        if 1 <= calib <= 3:
                            break
                    print("Error: Ingresa un número entre 1 y 3.")
                
                if calib == 3:
                    print("¡Error de calibración! La alarma comenzó a sonar.")
                    alarma = True

            
            if not alarma:
                cerraduras_abiertas += 1
                print("\n¡Éxito! Lograste forzar y abrir 1 cerradura.")

  
    elif opcion == 2:
        forzar_seguidas = 0 
        energia -= 10
        tiempo -= 3
        
        print("\nHackeando panel de seguridad...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f" Progresando paso {paso}/4... Código actual: '{codigo_parcial}'")
            
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = "" 
                print("¡CÓDIGO DE SCRIPT COMPLETO! Se abrió 1 cerradura automáticamente.")

    
    elif opcion == 3:
        forzar_seguidas = 0 
        ganancia = 15
        
        if alarma:
            ganancia -= 10
            print("\nDescansando bajo tensión (Alarma activa: -10 de energía extra por estrés).")
            
        
        if energia + ganancia > 100:
            energia = 100
        else:
            energia += ganancia
            
        tiempo -= 1
        print(f"\nHas descansado. Energía actual: {energia}")


print("\n" + "="*40)
print("FIN DEL JUEGO")
print("="*40)

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {agente.capitalize()} abrió la bóveda y completó la misión.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó por completo. La alarma sonó demasiado tiempo con poco margen.")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energía y caíste desmayado.")
elif tiempo <= 0:
    print("DERROTA: Se acabó el tiempo. Llegaron los refuerzos de seguridad.")

#Ejercicio 5

print("--- BIENVENIDO A LA ARENA ---")


while True:
    nombre = input("Nombre del Gladiador: ").strip()
    if nombre.isalpha():
        break
    print("Error: Solo se permiten letras.")


vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")


while vida_jugador > 0 and vida_enemigo > 0:
    
    if turno_gladiador:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
        
        while True:
            opcion_str = input("Opción: ").strip()
            if opcion_str.isdigit():
                opcion = int(opcion_str)
                if 1 <= opcion <= 3:
                    break
            print("Error: Ingrese un número válido (1, 2 o 3).")
            
        if opcion == 1:
           
            if vida_enemigo < 20:
                daño = float(dano_pesado * 1.5)
                print("¡GOLPE CRÍTICO!")
            else:
                daño = float(dano_pesado)
                
            vida_enemigo -= int(daño)
            print(f"¡Atacaste al enemigo por {daño} puntos de daño!")
            
        elif opcion == 2:
            
            print(">> ¡Inicias una ráfaga de golpes!")
            for _ in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
                
        elif opcion == 3:
           
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te curaste 30 puntos de vida!")
            else:
                print("¡No quedan pociones! Has perdido el turno.")
                
        
        turno_gladiador = False
        
    else:
       
        if vida_enemigo > 0: 
            vida_jugador -= dano_enemigo
            print(f">> ¡El enemigo te atacó por {dano_enemigo} puntos de daño!")
            
        
        turno_gladiador = True

#
print("\n=== FIN DE LA BATALLA ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

