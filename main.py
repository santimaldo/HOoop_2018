import numpy as np
import matplotlib.pyplot as plt

class Fila(object):
    """Clase base de fila"""
    def __init__(self):
        """constructor de la clase Fila """
        self.enfila = 0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente preferencial"""
        if self.enfila > 0:
            self.enfila-=1
            self.fila.pop(0)

    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        #if self.enfila > maxenfila:
        pass

class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente no preferencial"""
        if self.enfila > 0:
            self.enfila-=1
            self.fila.pop(0)


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

    cantidadInicial = 30

    # creo los objetos fila
    filaG = FilaGeneral()
    filaP = FilaPreferencial()

    # FIla inicial antes de que abra el banco
    for jj in range(cantidadInicial):
        persona = Cliente(dni = np.random.randint(10000000,40000000))
        categoriaID = np.random.rand()
        if categoriaID < 0.75:
            persona.modificarcategoria('General')
            filaG.insertar(persona)
        else:
            persona.modificarcategoria('Preferencial')
            filaP.insertar(persona)

    enfilaG = [filaG.enfila]
    enfilaP = [filaP.enfila]

    # hago un loop temporal
    for ii in range(10):
        # cantidad de clientes que llegan (random entre 0 y 4)
        NuevosClientes = np.random.randint(0,5)

        # inserto los clientes a la fila
        for jj in range(NuevosClientes):
            persona = Cliente(dni = np.random.randint(10000000,40000000))
            categoriaID = np.random.rand()
            if categoriaID < 0.50:
                persona.modificarcategoria('General')
                filaG.insertar(persona)
            else:
                persona.modificarcategoria('Preferencial')
                filaP.insertar(persona)
        # atiendo al primero
        filaG.atender()
        filaP.atender()

        enfilaG.append(filaG.enfila)
        enfilaP.append(filaP.enfila)

        #print('n = ', str(ii+1), 'Generl = ', filaG.enfila, \
        #      ' +++ Preferencial = ', filaP.enfila)
        print('General = ', filaG.enfila, ' +++ Preferencial = ', filaP.enfila)
        print('---------------------------------------------------------')

'''
plt.figure()
plt.plot(np.array(enfilaG), 'b-')
plt.plot(np.array(enfilaP), 'r-')
plt.show()
'''
