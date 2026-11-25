import dataset
miBase= dataset.connect("sqlite:///datos.db")
tabla= miBase["Productos"]

"""Lista los productos"""
def listar():
    print("\n*****Listado de productos*****")
    for producto in tabla:
        print(f"ID:{producto['id']} | Producto: {producto['Nombre']} | Precio: {producto['Precio']}" )


while True:     
    opciones = input("""
**********MENU******************
1- Agregar producto
2- Quitar un producto por nombre
3- Quitar un producto por Id
4- Listar los productos
5- Buscar producto la primera vez que aparece
6- Buscar producto todas las veces
7- SALIR
********************************
Ingrese la opción deseada: """).strip()

    match opciones:
        case "1":
            nombreProducto= input("Nombre del producto:").strip().title()
            precio= float(input("Precio:"))
            productoAgregar={"Nombre":nombreProducto,"Precio":precio}
            tabla.insert(productoAgregar)
            print(f"*****El producto {nombreProducto} fue agregado con éxito******")
            listar()

        case"2":
            eliminarProducto =input("\nProducto a eliminar:").strip().title()
            tabla.delete(Nombre=eliminarProducto)
            print(f"*****El producto {eliminarProducto} fue eliminado con éxito******")
            listar()

        case "3":
            eliminarProducto =int(input("\nId de producto a eliminar:"))
            tabla.delete(id=eliminarProducto)
            print(f"*****El id {eliminarProducto} fue eliminado con éxito*****")
            listar()



        case "4":
           listar()


        case "5":
            buscar=input("\nProducto a buscar: ").strip().title()
            encontrado= tabla.find_one(Nombre=buscar)
            if encontrado:
                print(f"{buscar} está en la posición {encontrado['id']}")
            else:
                print(f"No se encontró el producto '{buscar}'.")

        case "6":
            buscar=input("\nProducto a buscar:").strip().title()
            encontrado= tabla.find(Nombre=buscar)
            if encontrado:
                for producto in encontrado:
                    print(f"{buscar} está en el id:{producto['id']}")
            else:
                print(f"No se encontró el producto '{buscar}'.")
        

            
        case "7":
            print("Gracias por utilizar el programa")
            break
        
        case _:
            print("Opción inválida. Por favor, elija un número del 1 al 7.")
