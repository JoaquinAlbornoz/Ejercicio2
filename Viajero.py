class ViajeroFrecuente:
    def __init__(self,num_viajero=0,dni= '',nombre= '',apellido='', millas_acumuladas=0):
        self.__num_viajero =num_viajero
        self.__dni =dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acumuladas=millas_acumuladas
    def cantidadTotaldeMillas(self):
        return self.__millas_acumuladas
    def acumularMillas(self,millas):
        self.__millas_acumuladas+=millas
        return self.__millas_acumuladas
    def canjearMillas(self,millasaCanjear):
        if(millasaCanjear<=self.__millas_acumuladas):
            self.__millas_acumuladas-=millasaCanjear
        else:
            print("\n---Error al canjear millas---\n")
        return self.__millas_acumuladas
    def getnum(self):
        return self.__num_viajero
    