from ast import Return


PI = 3.1416

class Science:
    
    GVD = 9.8

    @staticmethod
    def GRAVEDAD():
        return 9.8

# PI y GVD son valores que realmente solo tienen la nomenglatura de constante
# pero realmente pueden modificarse en tiempo de ejecución, Sin embargo en el
# caso del metodo GRAVEDAD, este no tiene forma de modificar.