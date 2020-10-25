import sys
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from cliente import Cliente
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from trabajo import Trabajo
from listaTrabajos import ListaTrabajos
from repositorioTrabajos import RepositorioTrabajos
import datetime
class Menu:
    '''Mostrar un menu y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.reposclientes = RepositorioClientes()
        self.listatrabajos = ListaTrabajos()
        self.repostrabajos = RepositorioTrabajos()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.mostrar_un_cliente,
            "3": self.nuevo_cliente,
            "4": self.actualizar_datos_clientes,
            "5": self.eliminar_clientes,
            "6": self.nuevo_trabajo,
            "7": self.mostrar_trabajo,
            "8": self.trabajo_finalizado,
            "9": self.trabajo_entregado,
            "10": self.actualizar_datos_trabajo,
            "11": self.eliminar_trabajo,
            "12": self.informe_historial_trabajos,
            "13": self. mostrar_trabajos,
            "0": self.salir
        }
    
    def mostrar_menu(self):
        print ("""
        Menu del sistema:
        1. Mostrar todos los clientes
        2. Mostrar un cliente por ID
        3. Ingresar los datos de un nuevo cliente
        4. Actualizar datos de un cliente
        5. Eliminar cliente
        6. Ingresar los datos de un nuevo trabajo
        7. Mostrar trabajo por ID
        8. Marcar un trabajo como finalizado
        9. Marcar un trabajo como entregado
        10. Actualizar datos de un trabajo
        11. Eliminar trabajo
        12. Ver historial de trabajos de un cliente
        13. Mostrar todos los trabajos
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
    def mostrar_clientes(self, lista = None):
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)
            print("***********************************")
    
    #READ - Metodo para mostrar un solo cliente de la base de datos, buscando por ID
    def mostrar_un_cliente(self, lista = None):
        id_cliente = int(input("Ingrese el id del cliente: "))
        cliente = self.repostrabajos.get_one(id_cliente)
        if cliente == None:
            print("Error, no existe un cliente con el ID ingresado")
        else:
            return cliente  

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

    #NUEVO TRABAJO: Para cargar un nuevo trabajo en base de datos trabajo
    def nuevo_trabajo(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente al que desa asignarle el trabajo: C = Corporativo - P = Particular: ")
        nombre = None
        if tipo in ("C", "c"):
            id = int(input("Ingrese el id del cliente: "))
            contacto = None
            tc= None
        else:
            id = int(input("Ingrese el id del cliente: "))
            apellido = None
        tel = None
        mail = None
        if tipo in ("C", "c"):
            cliente = ClienteCorporativo(nombre, contacto, tc, tel, mail, id)
            fecha_ingreso = datetime.date.today()
            print("Fecha de entrega propuesta: ")
            dia = (int(input("Ingrese el dia de entrega propuesta: ")))
            mes = (int(input("Ingrese el mes de entrega propuesta: ")))
            anio = (int(input("Ingrese el año de entrega propuesta: ")))
            fecha_entrega_propuesta = datetime.date(anio, mes, dia)
            fecha_entrega_real = None
            retirado = False
            descripcion = input("Ingrese una breve descripcion del trabajo a realizar: ")
            nt = self.listatrabajos.nuevo_trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado)
        else:
            cliente = ClienteParticular(nombre, apellido, tel, mail, id)
            fecha_ingreso = datetime.date.today()
            print("Fecha de entrega propuesta: ")
            dia = (int(input("Ingrese el dia de entrega propuesta: ")))
            mes = (int(input("Ingrese el mes de entrega propuesta: ")))
            anio = (int(input("Ingrese el año de entrega propuesta: ")))
            fecha_entrega_propuesta = datetime.date(anio, mes, dia)
            fecha_entrega_real = None
            retirado = False
            descripcion = input("Ingrese una breve descripcion del trabajo a realizar: ")
            nt = self.listatrabajos.nuevo_trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado)
        if nt == 0:
            print("Error al intentar cargar el trabajo nuevo")
        else:
            print("Trabajo cargado exitosamente")

    #Mostrar un trabajo en particular
    def mostrar_trabajo(self):
        id_trabajo = int(input("Ingrese el id del trabajo: "))
        trabajo = self.repostrabajos.get_one(id_trabajo)
        if trabajo == None:
            print("Error, no existe un trabajo con el ID ingresado")
        else:
            return trabajo  
            
    #TRABAJO FINALIZADO: Para marcar un trabajo como finalizado con la fecha actual (hoy)
    def trabajo_finalizado(self):
        id_trabajo = int(input("Ingrese el id del trabajo que desea marcar como concluido: "))
        trabajo = self.repostrabajos.get_one(id_trabajo)
        if trabajo == None:
            print("Error, no existe un trabajo con el ID ingresado")
        else:
            trabajo.fecha_entrega_real = datetime.date.today()
            return self.repostrabajos.update(trabajo)
            print("El trabajo fue marcado como finalizado, de manera exitosa")

    #TRABAJO ENTREGADO: Para marcar un trabajo como entregado
    def trabajo_entregado(self):
        id_trabajo = int(input("Ingrese el id del trabajo que desea marcar como entregado: ")) 
        trabajo = self.repostrabajos.get_one(id_trabajo)
        if trabajo == None:
            print("Error, no existe un trabajo con el ID ingresado")
        else:
            trabajo.retirado = True
            return self.repostrabajos.update(trabajo)
            print("El trabajo fue marcado como entregado, de manera exitosa")

    #ACTUALIZAR TRABAJO: Para actualizar cualquiera de los datos del trabajo
    #(excepto id, y cliente asociado al mismo), buscando por ID
    def actualizar_datos_trabajo(self):
        id_trabajo = int(input("Ingrese el id del trabajo que desea actualizar: "))
        trabajo = self.repostrabajos.get_one(id_trabajo)
        if trabajo == None:
            print("Error, no existe un trabajo con el ID ingresado")
        else:
            preg_uno = int(input("Si desea actualizar la fecha de ingreso marque 1, de lo contrario otro numero: "))
            if preg_uno == 1:
                print("Actualizar la fecha de ingreso: ")
                dia = (int(input("Ingrese el dia de ingreso: ")))
                mes = (int(input("Ingrese el mes de ingreso: ")))
                anio = (int(input("Ingrese el año de ingreso: ")))
                fecha_ingreso = datetime.date(anio, mes, dia)
                trabajo.fecha_ingreso = fecha_ingreso
            preg_dos = int(input("Si desea actualizar la fecha de entrega propuesta marque 1, \n de lo contrario otro numero: "))
            if preg_dos == 1:
                print("Actualizar la fecha de entrega propuesta: ")
                dia = (int(input("Ingrese el dia de entrega propuesta: ")))
                mes = (int(input("Ingrese el mes de entrega propuesta: ")))
                anio = (int(input("Ingrese el año de entrega propuesta: ")))
                fecha_entrega_propuesta = datetime.date(anio, mes, dia)
                trabajo.fecha_entrega_propuesta = fecha_entrega_propuesta
            preg_tres = int(input("Si el trabajo ya fue entregado, y desea modificar esa fecha, marque 1,\n de lo contrario marque otro numero: "))
            if preg_tres == 1:
                print("Actualizar la fecha de entrega real: ")
                dia = (int(input("Ingrese el dia de entrega real: ")))
                mes = (int(input("Ingrese el mes de entrega real: ")))
                anio = (int(input("Ingrese el año de entrega real: ")))
                fecha_entrega_real = datetime.date(anio, mes, dia)
                trabajo.fecha_entrega_real = fecha_entrega_real
            preg_cuatro = int(input("Si desea modificar la descripcion del trabajo, marque 1,\n de lo contrario otro numero: "))
            if preg_cuatro == 1:
                print("Actualizar descripcion del trabajo: ")
                descripcion = input("Ingrese una breve descripcion del trabajo a realizar: ")
                trabajo.descripcion = descripcion
            preg_cinco = int(input("Si desea modificar el estado a retirado/no retirado,\n marque 1, de lo contrario otro numero: "))
            if preg_cinco == 1:
                preg_retirado = int(input("Ingrese 1 para indicar que el trabajo esta retirado,\n otro numero para marcar como no retirado: "))
                if preg_retirado == 1:
                    retirado = True
                else:
                    retirado = False
            return self.repostrabajos.update(trabajo)
            print("Datos del trabajo actualizados con exito !!!")

    #ELIMINAR TRABAJO: busca por ID, en repositorio trabajos y si lo encuentra lo elimina de la base de datos
    def eliminar_trabajo(self):
        id_trabajo = int(input("Ingrese el id del trabajo que desea eliminar: "))
        trabajo = self.repostrabajos.get_one(id_trabajo)
        if trabajo == None:
            print("Error, no existe un trabajo con el ID ingresado")
        else:
            return self.repostrabajos.delete(trabajo)
            print("Trabajo eliminado con exito !!!")

    #INFORME: Historial de trabajos que encargo cada cliente
    '''TERMINAR ESTE METODO Y LUEGO VER TKINTER'''
    def informe_historial_trabajos(self):
        id_cliente = int(input("Ingrese el id del cliente, para ver su historial de trabajos: "))
        lista = self.listatrabajos.lista
        if id_cliente in lista:
            trabajo = self.repostrabajos.get_one(id_cliente)
        if trabajo == None:
            print("Error, no existe un cliente con el ID ingresado")
        else:
            print("Lista de trabajos del cliente: ", trabajo.cliente)
            return trabajo
            print("***********************************")
    
    #Mostrar todos los trabajos de la base de datos
    def mostrar_trabajos(self, lista = None):
        if lista == None:
            lista = self.listatrabajos.lista
        for cliente in lista:
            print(cliente)
            print("***********************************")

    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

'''******************************************************************************************'''

if __name__ == "__main__":
    a = Menu()
    a.ejecutar()

                               