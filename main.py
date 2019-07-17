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
        self.enfila-=1
        self.fila.pop(0)


class cliente(object):
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
    import numpy as np

    # creo la fila general
    filaG = FilaGeneral()

    for ii in range(10):
        # cantidad de clientes que llegan (random entre 0 y 4)
        NuevosClientes = int((np.random.random())*5)

        # inserto los clientes a la fila
        for jj in range(NuevosClientes):
            filaG.insertar((np.random.random())*10)

        # atiendo al primero
        filaG.atender()

        print('atencion numero = ' + str(ii+1))
        print(filaG.enfila, filaG.fila)
        print('---------------------------')
