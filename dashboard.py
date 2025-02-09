import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'alumno/alumnota.py',
        '2': 'area_triangulo/area_triangulo.py',
        '3': 'constructor_destructor/constructor_destructores.py',
        '4': 'herencia/clase_objeto_herencia.py',
        '5': 'temperaturas/temperaturas.py',
        '6': 'Program_ori_objetos/Program_ori_objetos.py',
        #  rutas de los scripts que se encuentran en mi proyecto
    }

    while True:
        print("\n--------  Menu Principal - Dashboard  ------------")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("---------        0 - Salir          ----------     ")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
