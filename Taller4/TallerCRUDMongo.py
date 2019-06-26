""" Proyecto CRUD en Mongo DB Atlas
La empresa de Pepito Pérez quiere crear una base de datos en MongoDB que contenga 
toda la información de sus empleados para poder realizar los pagos de nomina de 
una manera más eficiente, para esto, Don Pepito requiere que la base de datos 
contenga la siguiente información:
    Cédula
    Nombres y Apellidos
    Correo
    Cargo
    Valor hora
    Horas trabajadas
    Salario a pagar
Crear un proyecto de python capaz de realizar un CRUD(Crear, Leer, Actualizar y 
Eliminar) a la base de datos Mongo; Inicialmente, al crear un nuevo empleado el 
campo "Salario a pagar" debe de estar vacío y actualizarse con el resultado de 
la multiplicación entre los campos "Valor hora" y "Horas trabajadas".
"""
from pymongo import MongoClient
# cliente para conexion al servidor
client = MongoClient("mongodb+srv://cmunoz-admin:Seti2019*@cluster0-ghkjh.gcp.mongodb.net/test?retryWrites=true&w=majority")
# objeto que se conecta a la base de datos
mongodb = client.get_database('employee_db')
# objeto para manejo de la coleccion de documentos
records = mongodb.employee_records

# funcion para insertar datos
class empleado():
    # Initializer / Instance Attributes
    def __init__(self):
        self.emp_cc = ""
        self.emp_nombre = ""
        self.emp_email = ""
        self.emp_cargo = ""
        self.emp_val_hora = 0
        self.emp_horas = 0
        self.emp_salario = 0
    # metodo para insertar un documento
    def insertar(self):
        self.emp_cc = input("Numero CC: ")
        self.emp_nombre = input("Nombre: ")
        self.emp_email = input("E-mail: ")
        self.emp_cargo = input("Cargo: ")
        self.emp_val_hora = float(input("Valor Hora: "))

        records.insert_one( {"emp_cc": self.emp_cc,
                             "emp_nombre": self.emp_nombre,
                             "emp_email": self.emp_email,
                             "emp_cargo": self.emp_cargo,
                             "emp_val_hora": self.emp_val_hora,
                             "emp_horas": 0,
                             "emp_salario": 0
                            }
                        )
        print("Documento registrado exitosamente. Lleva ",
               records.count_documents({})," documentos ")
    # metodo para listar los documentos
    def listar(self):
        employees = records.find()
        for emp in employees:
            print(emp)
    # metodo para borrar un documento
    def borrar(self):
        self.emp_cc = input("Numero CC a borrar: ")
        doc = records.find_one({"emp_cc": self.emp_cc})
        if doc is not None:
            records.delete_one({"emp_cc": self.emp_cc})
            print("La CC ",self.emp_cc," ha sido borrada. Quedan ",
                records.count_documents({})," documentos")
        else:
            print("La CC ",self.emp_cc," no ha sido encontrada.")
    # modificar un documento
    def modificar(self):
        self.emp_cc = input("Numero CC a modificar: ")
        doc = records.find_one({"emp_cc": self.emp_cc})
        if doc is not None:
            self.emp_horas = float(input("Horas Trabajadas de "+doc['emp_nombre']+': '))
            # calcular el salario
            self.emp_salario = self.emp_horas * doc['emp_val_hora']
            records.update_one({"emp_cc": self.emp_cc},
                                {"$set": {"emp_horas": self.emp_horas,
                                          "emp_salario": self.emp_salario}
                                }
                            )
            print("La CC ",self.emp_cc," el salario ha sido actualizado a ", self.emp_salario)
        else:
            print("La CC ",self.emp_cc," no ha sido encontrada.")

miemp = empleado()

while(1):
    sel = input("Digite (1) para insertar, (2) para listar, (3) para borrar (4) para modificar, (0) para salir ")
    if   sel == '1':
        miemp.insertar()
    elif sel == '2':
        miemp.listar()
    elif sel == '3':
        miemp.borrar()
    elif sel == '4':
        miemp.modificar()
    elif sel == '0':
        break
    else:
        print("opción no válida")
