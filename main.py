import numpy as np
import matplotlib.pyplot as plt

class Fila(object):
    """Clase base de fila"""
    def __init__(self):
        """constructor de la clase Fila """
        self.enfila = 0
        self.fila = []

    def get_enfila(self):
        """getter del atributo enfila """
        return self.enfila

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente preferencial"""
        if self.enfila > 0:
            self.enfila-=1
            self.fila.pop(0)

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""

    def abrircajanueva(self,maxenfila,cajaNueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if self.enfila > maxenfila:
            cajaNueva.atender()
            print('se abrio caja 2')

class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def saludar(self):
        print('Hola, soy una fila general')

class Cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria = categoria


if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    # INPUTS
    cantidadInicial = 20
    maxenfila = 15
    tiempoTotal = 100
    graficar = True
    clientesG_percent = 0.55

    # creo los objetos fila
    filaG = FilaGeneral()
    filaP = FilaPreferencial()

    # FIla inicial antes de que abra el banco
    for jj in range(cantidadInicial):
        persona = Cliente(dni = np.random.randint(10000000,40000000))
        categoriaID = np.random.rand()
        if categoriaID < clientesG_percent:
            persona.modificarcategoria('General')
            filaG.insertar(persona)
        else:
            persona.modificarcategoria('Preferencial')
            filaP.insertar(persona)

    enfilaG = [filaG.get_enfila()]
    enfilaP = [filaP.get_enfila()]

    # hago un loop temporal
    for ii in range(tiempoTotal):
        # cantidad de clientes que llegan (random entre 0 y 4)
        NuevosClientes = np.random.randint(0,5)

        # inserto los clientes a la fila
        for jj in range(NuevosClientes):
            persona = Cliente(dni = np.random.randint(10000000,40000000))
            categoriaID = np.random.rand()
            if categoriaID < clientesG_percent:
                persona.modificarcategoria('General')
                filaG.insertar(persona)
            else:
                persona.modificarcategoria('Preferencial')
                filaP.insertar(persona)
        # atiendo al primero
        filaG.atender()
        filaP.atender()
        filaP.abrircajanueva(maxenfila,filaP)

        enfilaG.append(filaG.get_enfila())
        enfilaP.append(filaP.get_enfila())

        #print('n = ', str(ii+1), 'Generl = ', filaG.enfila, \
        #      ' +++ Preferencial = ', filaP.enfila)
        print('General = ', filaG.get_enfila(), ' +++ Preferencial = ', filaP.get_enfila() )
        print('---------------------------------------------------------')


    if graficar:
        plt.figure()
        plt.plot(np.array(enfilaG), 'b-')
        plt.plot(np.array(enfilaP), 'r-')
        plt.show()
