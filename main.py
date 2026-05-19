# ============================================================
# Archivo: main.py
# Proyecto: Gestor de Combustible y Gastos de Vehículos
# Rama: main
# Responsable: Estudiante 1
# Descripción: Programa principal con menú interactivo.
#              Integra los módulos de registro, cálculos y búsqueda.
# ============================================================

from registro import registrar_gasto
from calculos import mostrar_resumen
from busqueda import buscar_por_placa

# Lista principal donde se almacenan todos los gastos en memoria
gastos = []


def mostrar_menu():
    """Imprime el menú principal del programa."""
    print("\n" + "="*45)
    print("   GESTOR DE GASTOS DE VEHÍCULOS v1.0")
    print("="*45)
    print("  1. Registrar nuevo gasto")
    print("  2. Ver resumen total de gastos")
    print("  3. Buscar gastos por placa")
    print("  4. Salir")
    print("="*45)


def main():
    """Función principal: ejecuta el bucle del menú interactivo."""
    print("\n  Bienvenido al sistema de gestión de gastos.")

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            registrar_gasto(gastos)

        elif opcion == "2":
            mostrar_resumen(gastos)

        elif opcion == "3":
            buscar_por_placa(gastos)

        elif opcion == "4":
            print("\n  Gracias por usar el gestor. ¡Hasta luego!\n")
            break

        else:
            print("\n  [ERROR] Opción inválida. Por favor elija entre 1 y 4.")


if __name__ == "__main__":
    main()