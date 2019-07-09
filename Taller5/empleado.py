"""
Este modulo soporta todas las operaciones REST que se soportan
en una base de datos MongoDB
"""

# Modulos externos
from flask import make_response, abort
from pymongo import MongoClient
import json

# cliente para conexion al servidor
client = MongoClient("mongodb+srv://cmunoz-admin:Seti2019*@cluster0-ghkjh.gcp.mongodb.net/test?retryWrites=true&w=majority")
# objeto que se conecta a la base de datos
mongodb = client.get_database('employee_db')
# objeto para manejo de la coleccion de documentos
records = mongodb.employee_records

def listar_todos():
    """
    Esta funcion responde a la peticion /api/empleado
    listando todos los empleados
    :return:        objeto json con los empleados
    """
    # Create the list of people from our data
    # return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
    # crear la lista de empleados
    employees = records.find()
    return [employees]



def buscar(emp_cc):
    """
    Esta funcion responde a la peticion /empleado/{emp_cc}
    con un solo empleado
    :param emp_cc:   ceduloa del empleado
    :return:         empleado que tiene la cedula
    """
    # Buscar el empleado
    doc = records.find_one({"emp_cc": emp_cc})
    # Existe el empleado?
    if doc is not None:
        doc['_id']= str(doc['_id'])
        return json.dumps(doc)
    # no existe
    else:
        abort(
            404, "Empleado con CC: {emp_cc} no existe".format(emp_cc=emp_cc)
        )


def insertar(empleado):
    """
    Esta funcion crea un nuevo empleado
    basado en el parametro empleado 
    :param empleado:  empleado a crear
    :return:        201 si es exitoso, 406 si ya existe 
    """
    emp_cc= empleado.get("emp_cc", None)
    emp_nombre= empleado.get("emp_nombre", None)
    emp_email= empleado.get("emp_email", None)
    emp_cargo= empleado.get("emp_cargo", None)
    emp_val_hora= empleado.get("emp_val_hora", None)

    # verificar si el empleado existe
    doc = records.find_one({"emp_cc": emp_cc})
    if doc is None:
        records.insert_one( {"emp_cc": emp_cc,
                            "emp_nombre": emp_nombre,
                            "emp_email": emp_email,
                            "emp_cargo": emp_cargo,
                            "emp_val_hora": emp_val_hora,
                            "emp_horas": 0,
                            "emp_salario": 0
                            }
                        )
        return empleado, 201
    # sino, ya existe, esto es un error
    else:
        abort(
            406,
            "El empleado {emp_cc} ya existe".format(emp_cc=emp_cc),
        )


def modificar(emp_cc, empleado):
    """
    Esta funcion actualiza los datos de un empleado que exista
    :param emp_cc:    CC del empleado a actualizar
    :param empleado:  datos del empleado a actualizar
    :return:          estructura del empleado actualizado
    """
    # verificar si el empleado existe
    doc = records.find_one({"emp_cc": emp_cc})
    if doc is not None:
        doc['emp_horas']= float(empleado.get("emp_horas", doc['emp_horas']))
        doc['emp_val_hora']= float(empleado.get("emp_val_hora", doc['emp_val_hora']))
        # calcular el salario
        doc['emp_salario']= doc['emp_horas'] * doc['emp_val_hora']
        records.update_one({"emp_cc": emp_cc},
                            {"$set": {"emp_horas": doc['emp_horas'],
                                      "emp_salario": doc['emp_salario']}
                            }
                        )
        doc['_id']= str(doc['_id'])
        return json.dumps(doc)
    # sino, no existe, error
    else:
        abort(
            404, "La CC {emp_cc} no ha sido encontrada.".format(emp_cc=emp_cc)
        )


def borrar(emp_cc):
    """
    Esta funcion borra un empleado
    :param emp_cc:   CC del empleado a borrar
    :return:         200 si es borraro, 404 si no se encuentra
    """
    doc = records.find_one({"emp_cc": emp_cc})
    if doc is not None:
        records.delete_one({"emp_cc": emp_cc})
        return make_response(
            "La CC {emp_cc} ha sido borrada".format(emp_cc=emp_cc), 200
        )
    # sino, empleado no borrado
    else:
        abort(
            404, "Empleado con CC {emp_cc} no encontrado".format(emp_cc=emp_cc)
        )