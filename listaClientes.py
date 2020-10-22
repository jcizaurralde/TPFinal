from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes

class ListaClientes:
    def __init__(self):
        self.reposclientes = RepositorioClientes()
        self.lista = self.reposclientes.get_all()

    

    def nuevo_cliente_corporativo(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        client = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        client.id_cliente = self.reposclientes.store(client)
        if client.id_cliente == 0:
            return None
        else:
            self.lista.append(client)
            return client

    def nuevo_cliente_particular(self, nombre, apellido, telefono, mail):
        client = ClienteParticular(nombre, apellido, telefono, mail)
        client.id_cliente = self.reposclientes.store(client)
        if client.id_cliente == 0:
            return None
        else:
            self.lista.append(client)
            return client