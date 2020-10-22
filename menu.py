import sys
from listaClientes import ListaClientes
class Menu:
    '''Mostrar un menu y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "0": self.salir
        }
    
    def mostrar_menu(self):
        print ("""
        Menu del sistema:
        1. Mostrar todos los clientes
        2. Ingresar losdatos de un nuevo cliente
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
    
    def mostrar_clientes(self, lista = None):
        if lista == None:
            lista = self.lista
        for cliente in lista:
            print(cliente)
            print("***********************************")

    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C = Corporativo - P = Particular")
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

    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

    if __name__ == "__main__":
        m = Menu()
        m.ejecutar()

                               