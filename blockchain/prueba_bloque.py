from bloque import Bloque


datos = {
    "cultivo": "mani",
    "anio": 2024,
    "provincia": "Cordoba",
    "departamento": "Rio Cuarto",
    "produccion_tn": 297500
}


bloque = Bloque(
    1,
    datos,
    "000000"
)


bloque.mostrar()