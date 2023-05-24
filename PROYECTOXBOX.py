# Abstracción y encapsulamiento
class Xbox:
    def __init__(self, modelo):
        self.__modelo = modelo

    def obtener_modelo(self):
        return self.__modelo

    def encender(self):
        print("Encendiendo la Xbox...")

    def jugar(self):
        print("Jugando en la Xbox.")


# Polimorfismo y herencia
class XboxSeriesX(Xbox):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.__resolucion_maxima = "4K"

    def obtener_resolucion_maxima(self):
        return self.__resolucion_maxima

    def jugar(self):
        print("Jugando en la Xbox Series X con gráficos impresionantes.")


# Crear instancia de una Xbox básica
xbox_basica = Xbox("Xbox One")
print(xbox_basica.obtener_modelo())  # Output: Xbox One
xbox_basica.encender()  # Output: Encendiendo la Xbox...
xbox_basica.jugar()  # Output: Jugando en la Xbox.

# Crear instancia de una Xbox Series X
xbox_series_x = XboxSeriesX("Xbox Series X")
print(xbox_series_x.obtener_modelo())  # Output: Xbox Series X
print(xbox_series_x.obtener_resolucion_maxima())  # Output: 4K
xbox_series_x.encender()  # Output: Encendiendo la Xbox...
xbox_series_x.jugar()  # Output: Jugando en la Xbox Series X con gráficos impresionantes.