import sys
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from cliente import Cliente
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
class Menu:
    '''Mostrar un menu y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.reposclientes = RepositorioClientes()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.actualizar_datos_clientes,
            "4": self.eliminar_clientes,
            
            "0": self.salir
        }
    
    def mostrar_menu(self):
        print ("""
        Menu del sistema:
        1. Mostrar todos los clientes
        2. Ingresar los datos de un nuevo cliente
        3. Actualizar datos de cliente
        4. Eliminar cliente
        0. Salir
        """)
    
    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones'''
        while True:
            self.mostrar_menu()
            opcion = input ("Ingresar una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion valida".format(opcion))

    #READ - Metodo para mostrar todos los clientes cargados en la base de datos
    '''ESTE METODO PODRIA MEJORARSE PARA BUSCAR LOS DATOS DE UN SOLO CLIENTE POR ID'''
    def mostrar_clientes(self, lista = None):
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)
            print("***********************************")

    #CREATE - Metodo para crear un nuevo objeto cliente en la base de datos, dentro de la clase hija que corresponde (C o P)
    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C = Corporativo - P = Particular: ")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
            contacto = input ("Ingrese el nombre del contacto: ")
            tc= input("Ingrese el telefono del contacto: ")
        else:
            apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el telefono: ")
        mail = input("Ingrese el correo electronico: ")
        if tipo in ("C", "c"):
            c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("Error al cargar el cliente")
        else:
            print("Cliente cargado correctamente")


    #UPDATE - Metodo para modificar y actualizar los datos de un cliente particular o corporativo, en la base de datos.
    def actualizar_datos_clientes(self):
        id = int(input("Ingrese el id del cliente: "))
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C = Corporativo - P = Particular: ")
        nombre = input("Ingrese el nuevo nombre: ")
        if tipo in ("C", "c"):
            contacto = input ("Ingrese el nuevo nombre del contacto: ")
            tc= input("Ingrese el telefono del contacto: ")
        else:
            apellido = input("Ingrese el nuevo apellido: ")
        tel = input("Ingrese el nuevo telefono: ")
        mail = input("Ingrese el nuevo correo electronico: ")
        if tipo in ("C", "c"):
            cliente = ClienteCorporativo(nombre, contacto, tc, tel, mail, id)
            c = self.reposclientes.update(cliente)
        else:
            cliente = ClienteParticular(nombre, apellido, tel, mail,id)
            c = self.reposclientes.update(cliente)
        if c is False:
            print("Error al intentar modificar al cliente, no existe en la lista que corresponde al tipo seleccionado (C o P)")
        else:
            print("Cliente modificado correctamente")


    #DELETE - Metodo para eliminar definitivamente un cliente particular o corporativo, de la base de datos.
    def eliminar_clientes(self, lista = None):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente que desea eliminar: C = Corporativo - P = Particular: ")
        nombre = None
        if tipo in ("C", "c"):
            id = int(input("Ingrese el id del cliente que desea eliminar: "))
            contacto = None
            tc= None
        else:
            id = int(input("Ingrese el id del cliente que desea eliminar: "))
            apellido = None
        tel = None
        mail = None
        if tipo in ("C", "c"):
            cliente = ClienteCorporativo(nombre, contacto, tc, tel, mail, id)
            c = self.reposclientes.delete(cliente)
        else:
            cliente = ClienteParticular(nombre, apellido, tel, mail, id)
            c = self.reposclientes.delete(cliente)
        if c is False:
            print("Error al intentar eliminar al cliente de la base de datos")
        else:
            print("Cliente eliminado correctamente de la base de datos")    


    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

'''******************************************************************************************'''

if __name__ == "__main__":
    a = Menu()
    a.ejecutar()

                               