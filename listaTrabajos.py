from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
import datetime

class ListaTrabajos:
    def __init__(self):
        self.repostrabajos = RepositorioTrabajos()
        self.lista = self.repostrabajos.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta,
        fecha_entrega_real, descripcion, retirado, id_trabajo = None):
        trabajo = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado, id_trabajo)
        trabajo.id_trabajo = self.repostrabajos.store(trabajo)
        if trabajo.id_trabajo == 0:
            return None
        else:
            self.lista.append(trabajo)
            return trabajo

    