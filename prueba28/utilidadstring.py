class UtilidadString:
    #Función que devuelva el número de dígitos de un str
    @staticmethod
    def contarDigitos(cadena:str) -> int:
        totalDigitos = 0
        for caracter in range(len(cadena)):
            if cadena[caracter].isdigit():
                totalDigitos+=1
        return totalDigitos


if __name__=='__main__':
    def main():
        cadena = "holajd 6 jd2jdkjs98"
        print(UtilidadString.contarDigitos(cadena))
    