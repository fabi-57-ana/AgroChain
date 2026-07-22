from cadena import Blockchain


cadena = Blockchain()


cadena.agregar_bloque(
    {
        "cultivo": "mani",
        "anio": 2024,
        "provincia": "Cordoba",
        "departamento": "Rio Cuarto",
        "produccion_tn": 297500
    }
)


cadena.agregar_bloque(
    {
        "cultivo": "mani",
        "anio": 2024,
        "provincia": "Buenos Aires",
        "departamento": "General Villegas",
        "produccion_tn": 64750
    }
)


cadena.mostrar_cadena()


print("\nVALIDACION DE CADENA:")
print(cadena.validar_cadena())