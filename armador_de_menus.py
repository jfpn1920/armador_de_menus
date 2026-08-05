import random
ids = []
nombres = []
descripciones = []
categorias = []
precios = []
disponibilidades = []
fechas = []
tiempos = []
observaciones = []
#-------------------------------------#
#--|menu_principal_armador_de_menus|--#
#-------------------------------------#
while True:
    print("menu principal armador de menus")
    print("1) registrar menú")
    print("2) editar menú")
    print("3) eliminar menú")
    print("4) buscar menú")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|registrar_menu|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_menu = 1
        else:
            id_menu = ids[-1] + 1
        nombre = input("nombre del plato: ")
        descripcion = input("descripción: ")
        categoria = input("categoría (entrada, plato fuerte, bebida, postre): ")
        precio = float(input("precio: "))
        disponibilidad = input("disponibilidad (disponible o no disponible): ")
        fecha = input("fecha de registro: ")
        tiempo = int(input("tiempo de preparación (minutos): "))
        observacion = input("observación: ")
        ids.append(id_menu)
        nombres.append(nombre)
        descripciones.append(descripcion)
        categorias.append(categoria)
        precios.append(precio)
        disponibilidades.append(disponibilidad)
        fechas.append(fecha)
        tiempos.append(tiempo)
        observaciones.append(observacion)
        print("menú registrado correctamente.")
        print("id:", id_menu)
    #-----------------#
    #--|editar_menu|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen menús registrados.")
        else:
            print("editar menú")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | ${precios[i]:.2f}")
            id_buscar = int(input("ingrese la id del menú: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                categorias[posicion] = input("nueva categoría: ")
                precios[posicion] = float(input("nuevo precio: "))
                disponibilidades[posicion] = input("nueva disponibilidad: ")
                fechas[posicion] = input("nueva fecha: ")
                tiempos[posicion] = int(input("nuevo tiempo de preparación: "))
                observaciones[posicion] = input("nueva observación: ")
                print("menú actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_menu|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen menús registrados.")
        else:
            print("eliminar menú")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]}")
            id_buscar = int(input("ingrese la id del menú: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del menú")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]}")
                respuesta = input("¿desea eliminar este menú? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    descripciones.pop(posicion)
                    categorias.pop(posicion)
                    precios.pop(posicion)
                    disponibilidades.pop(posicion)
                    fechas.pop(posicion)
                    tiempos.pop(posicion)
                    observaciones.pop(posicion)
                    print("menú eliminado correctamente.")
                else:
                    print("el menú no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_menu|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen menús registrados.")
        else:
            print("buscar menú")
            id_buscar = int(input("ingrese la id del menú: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("categoría:", categorias[posicion])
                print("precio:", precios[posicion])
                print("disponibilidad:", disponibilidades[posicion])
                print("fecha:", fechas[posicion])
                print("tiempo de preparación:", tiempos[posicion], "minutos")
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen menús registrados.")
        else:
            entradas = 0
            platos_fuertes = 0
            bebidas = 0
            postres = 0
            disponibles = 0
            no_disponibles = 0
            total_precios = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | ${precios[i]:.2f} | {disponibilidades[i]}")
                total_precios += precios[i]
                if categorias[i].lower() == "entrada":
                    entradas += 1
                elif categorias[i].lower() == "plato fuerte":
                    platos_fuertes += 1
                elif categorias[i].lower() == "bebida":
                    bebidas += 1
                elif categorias[i].lower() == "postre":
                    postres += 1
                if disponibilidades[i].lower() == "disponible":
                    disponibles += 1
                elif disponibilidades[i].lower() == "no disponible":
                    no_disponibles += 1
            promedio = total_precios / len(ids)
            print("estadísticas armador de menus")
            print("cantidad de menús:", len(ids))
            print("entradas:", entradas)
            print("platos fuertes:", platos_fuertes)
            print("bebidas:", bebidas)
            print("postres:", postres)
            print("disponibles:", disponibles)
            print("no disponibles:", no_disponibles)
            print("precio promedio:", format(promedio, ".2f"))
            posicion = random.randint(0, len(ids) - 1)
            print("menú seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("precio:", precios[posicion])
            print("disponibilidad:", disponibilidades[posicion])
            print("fecha:", fechas[posicion])
            print("tiempo de preparación:", tiempos[posicion], "minutos")
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el armador de menus.")
        break
    else:
        print("opción no válida.")