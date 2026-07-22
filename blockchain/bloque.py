import hashlib
import json
from datetime import datetime


class Bloque:

    def __init__(
        self,
        indice,
        datos,
        hash_anterior
    ):

        self.indice = indice
        self.timestamp = datetime.now()
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()


    def calcular_hash(self):

        bloque_string = json.dumps(
            {
                "indice": self.indice,
                "timestamp": str(self.timestamp),
                "datos": self.datos,
                "hash_anterior": self.hash_anterior
            },
            sort_keys=True
        )

        return hashlib.sha256(
            bloque_string.encode()
        ).hexdigest()


    def mostrar(self):

        print("=" * 50)
        print("BLOQUE")
        print("=" * 50)

        print("Indice:", self.indice)
        print("Fecha:", self.timestamp)
        print("Datos:", self.datos)
        print("Hash anterior:", self.hash_anterior)
        print("Hash:", self.hash)