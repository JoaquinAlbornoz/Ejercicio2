from Viajero import ViajeroFrecuente
from lista import lista_viajeros

def test(lista):
    lista.viaj()
    m=1
    while m!=0:
          m=int(input('\n1.Consultar cantidad de millas\n2.Acumular Millas\n3.Canjear Millas\nIngrese opcion elegida, para terminar ingrese 0:'))
          if m==1:
              millas=lista.getcantmillas()
              print("\nCantidad de millas:{0}".format(millas))
          elif m==2:
                n=int(input('Ingrese numero de viajero: '))
                i=lista.buscarviajero(n)
                l=int(input('\nIngrese millas a acumular:'))
                if i==lista.getlen():
                    print('No se encontro el viajero')
                else:
                    k=lista.acumillas(i,l)
                    print('Cantidad de millas: {0}'.format(k))
          elif m==3:
              n=int(input('Ingrese numero de viajero: '))
              l=int(input('\nIngrese numero de millas a canjear:'))
              i=lista.buscarviajero(n)
              if i<lista.getlen():
                  print('Millas restantes:{0}'.format(lista.canjmillas(i,l)))
              else:
                  print('No se encontro el viajero')

if __name__== '__main__':
    lista=lista_viajeros()
    test(lista)