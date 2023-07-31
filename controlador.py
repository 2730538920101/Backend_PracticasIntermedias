from conexion import obtener_conexion

#Controlador para registrar contactos en la base de datos
def RegistrarContacto(nombre, telefono):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO CONTACTOS(NOMBRE, TELEFONO) VALUES(%s, %s);",(nombre,telefono))
            conexion.commit()
            # Validar la inserción
            if cursor.rowcount > 0:
                # Inserción exitosa
                return True
            else:
                # Error en la inserción
                return False
        except:
            # Manejo de excepciones en caso de error
            return False
        finally:
            conexion.close()

#Controlador para modificar la informacion del contacto
def ModificarTelefono(telefono, id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "UPDATE CONTACTOS SET TELEFONO = %s WHERE ID = %s"
            cursor.execute(query,(telefono, id))
            if cursor.rowcount > 0:
                # La actualización se realizó correctamente
                conexion.commit()
                return "SE HA MODIFICADO EXITOSAMENTE EL NUMERO DE TELEFONO DEL CONTACTO SELECCIONADO"
            else:
                # No se realizó la actualización
                return None
    except:
        return None
    finally:
        conexion.close()

#Controlador para eliminar un contacto
def EliminarContacto(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM CONTACTOS WHERE ID = %s"
            cursor.execute(query, (id,))
            if cursor.rowcount > 0:
                # La actualización se realizó correctamente
                conexion.commit()
                return "SE HA ELIMINADO EXITOSAMENTE EL CONTACTO"
            else:
                # No se realizó la actualización
                return None
    except:
        return None
    finally:
        conexion.close()

#Controlador para mostrar todos los contactos registrados
def MostrarContactos():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "SELECT ID, NOMBRE, TELEFONO FROM CONTACTOS"
            cursor.execute(query)
            contactos = cursor.fetchall()
            if len(contactos) == 0:
                return None
            else:
                contactos_obj = []
                for contacto in contactos:
                    contacto_obj = {
                        "id":contacto[0],
                        "nombre":contacto[1],
                        "telefono":contacto[2]
                    }
                    contactos_obj.append(contacto_obj)
                return contactos_obj
    except:
        return None
    finally:
        conexion.close()