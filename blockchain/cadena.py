from bloque import Bloque


class Blockchain:


    def __init__(self):

        self.cadena = []

        self.crear_bloque_genesis()



    def crear_bloque_genesis(self):

        bloque_genesis = Bloque(
            0,
            {
                "mensaje": "Bloque Genesis AgroChain"
            },
            "000000"
        )

        self.cadena.append(
            bloque_genesis
        )



    def ultimo_bloque(self):

        return self.cadena[-1]



    def agregar_bloque(self, datos):

        nuevo_bloque = Bloque(
            len(self.cadena),
            datos,
            self.ultimo_bloque().hash
        )

        self.cadena.append(
            nuevo_bloque
        )



    def mostrar_cadena(self):

        for bloque in self.cadena:

            bloque.mostrar()


    def validar_cadena(self):

        for i in range(1, len(self.cadena)):

            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i-1]


            if bloque_actual.hash != bloque_actual.calcular_hash():
                return False


            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False


        return True


