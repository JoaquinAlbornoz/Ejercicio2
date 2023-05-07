from Viajero import ViajeroFrecuente
import csv
class lista_viajeros:
    def __init__(self):
        self.__listav=[]
    def agregarviajero(self,v):
        self.__listav.append(v)
    def viaj(self):
        f=open("viajeros.csv")
        reader=csv.reader(f,delimiter=',')
        for fila in reader:
            if fila[0]!='' and fila[1]!='' and fila[2]!='' and fila[3]!='' and fila[4]!='':
                num=int(fila[0])
                dni=fila[1]
                nombre=fila[2]
                apellido=fila[3]
                millas= int(fila[4])
                viajero=ViajeroFrecuente(num,dni,nombre,apellido,millas)
                self.agregarviajero(viajero)
        f.close()
  
    def buscarviajero(self,num):
        i=0
        b=True
        j = None
        while b and i<len(self.__listav):
            nv=self.__listav[i].getnum()
            if nv==num:
                b=False
                j = i
            else:
                i+=1
        if j==None:
            j=len(self.__listav)
        return j
    def getlen(self):
        return len(self.__listav)
    def getcantmillas(self):
        num = int(input('Ingrese numero de viajero:'))
        i=self.buscarviajero(num)
        if i< len(self.__listav):
            return self.__listav[i].cantidadTotaldeMillas()
        else:
            print('No se encotro viajero')
    def acumillas(self,i,l):
        return self.__listav[i].acumularMillas(l)
    def canjmillas(self,i,l):
        return self.__listav[i].canjearMillas(l)