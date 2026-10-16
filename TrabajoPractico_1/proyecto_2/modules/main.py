# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el códigoimport os
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'biblioteca_ayed_fiuner'))

from modules.temperaturas_db import TemperaturasDB


def mostrar_menu():
    '''
    Muestra el menu de opciones en pantalla.

    PRE: Ninguna.
    POST: Imprime el menu con las 10 opciones disponibles mas la opcion de salida.
          No modifica ningun estado interno.
    '''
    print("\n" + "=" * 60)
    print("                TEMPERATURAS DB - MENÚ")
    print("=" * 60)
    print("1. Cargar datos desde muestras.txt")
    print("2. Guardar temperatura")
    print("3. Devolver temperatura por fecha")
    print("4. Máxima temperatura en rango")
    print("5. Mínima temperatura en rango")
    print("6. Temperaturas extremas en rango")
    print("7. Borrar temperatura")
    print("8. Listar temperaturas en rango")
    print("9. Cantidad de muestras")
    print("10. Mostrar todas las temperaturas")
    print("0. Salir")
    print("=" * 60)


def main():
    '''
    Punto de entrada principal del programa TemperaturasDB.

    PRE: Ninguna.
    POST: Ejecuta un bucle interactivo que permite al usuario cargar datos,
          consultar, agregar y eliminar temperaturas mediante un menu numerico.
          Finaliza cuando el usuario ingresa "0".
    '''
    db = TemperaturasDB()
    archivo_cargado = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ruta = input("Ruta del archivo (Enter para data/muestras.txt): ").strip()
            if not ruta:
                ruta = os.path.join(os.path.dirname(__file__), "data", "muestras.txt")
            try:
                cant = db.cargar_desde_archivo(ruta)
                archivo_cargado = True
                print(f"\n✓ Se cargaron {cant} registros correctamente.")
            except FileNotFoundError as e:
                print(f"\n✗ Error: {e}")
            except Exception as e:
                print(f"\n✗ Error inesperado: {e}")

        elif opcion == "2":
            fecha = input("Fecha (dd/mm/aaaa): ").strip()
            temp = input("Temperatura: ").strip()
            try:
                db.guardar_temperatura(float(temp), fecha)
                print(f"\n✓ Temperatura {temp} guardada para {fecha}.")
            except (ValueError, TypeError) as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "3":
            fecha = input("Fecha (dd/mm/aaaa): ").strip()
            try:
                temp = db.devolver_temperatura(fecha)
                print(f"\nTemperatura del {fecha}: {temp} ºC")
            except (ValueError, TypeError) as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "4":
            f1 = input("Fecha inicial (dd/mm/aaaa): ").strip()
            f2 = input("Fecha final (dd/mm/aaaa): ").strip()
            try:
                temp = db.max_temp_rango(f1, f2)
                print(f"\nMáxima temperatura en [{f1} - {f2}]: {temp} ºC")
            except ValueError as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "5":
            f1 = input("Fecha inicial (dd/mm/aaaa): ").strip()
            f2 = input("Fecha final (dd/mm/aaaa): ").strip()
            try:
                temp = db.min_temp_rango(f1, f2)
                print(f"\nMínima temperatura en [{f1} - {f2}]: {temp} ºC")
            except ValueError as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "6":
            f1 = input("Fecha inicial (dd/mm/aaaa): ").strip()
            f2 = input("Fecha final (dd/mm/aaaa): ").strip()
            try:
                minimo, maximo = db.temp_extremos_rango(f1, f2)
                print(f"\nExtremos en [{f1} - {f2}]:")
                print(f"  Mínima: {minimo} ºC")
                print(f"  Máxima: {maximo} ºC")
            except ValueError as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "7":
            fecha = input("Fecha a borrar (dd/mm/aaaa): ").strip()
            try:
                db.borrar_temperatura(fecha)
                print(f"\n✓ Temperatura del {fecha} eliminada.")
            except ValueError as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "8":
            f1 = input("Fecha inicial (dd/mm/aaaa): ").strip()
            f2 = input("Fecha final (dd/mm/aaaa): ").strip()
            try:
                resultados = db.devolver_temperaturas(f1, f2)
                print(f"\nTemperaturas en [{f1} - {f2}]:")
                for r in resultados:
                    print(f"  {r}")
            except ValueError as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "9":
            print(f"\nCantidad de muestras almacenadas: {db.cantidad_muestras()}")

        elif opcion == "10":
            try:
                resultados = db.devolver_temperaturas("01/01/2025", "31/12/2025")
                print(f"\nTodas las temperaturas ({len(resultados)} registros):")
                for r in resultados:
                    print(f"  {r}")
            except ValueError as e:
                print(f"\n✗ No hay datos cargados.")

        elif opcion == "0":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n✗ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()