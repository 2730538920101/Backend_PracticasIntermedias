import controlador
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from conexion import obtener_conexion

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": ["*"]}})
app.config['CORS_HEADERS'] = 'Content-Type'



#Enpoint para probar la conexion con la base de datos
@app.route('/', methods=['GET'])
def index():
    try:
        conexion = obtener_conexion()
        response = make_response(jsonify({'status':'success','PracticasI': "CONEXION EXITOSA"}))
        response.status_code = 200
        return response
    except:
        print("NO SE PUEDE ESTABLECER LA CONEXION A LA BASE DE DATOS")
        response = make_response(jsonify({'status':'error','PracticasI': "NO SE PUEDE ESTABLECER LA CONEXION A LA BASE DE DATOS"}))
        response.status_code = 500
        return response

#Enpoint para insertar un contacto en la base de datos
@app.route('/RegistrarContacto', methods=['POST'])
def RegistrarContacto():
    try:
        data = request.get_json()
        nombre = data['nombre']
        telefono = data['telefono']
        flag = controlador.RegistrarContacto(nombre, telefono)
        if flag:
            response = make_response(jsonify({'status':'success','PracticasI': "SE HA INSERTADO EL CONTACTO EXITOSMENTE"}))
            response.status_code = 200
            return response
        else:
            response = make_response(jsonify({'status':'error','PracticasI': "NO SE HA PODIDO INSERTAR EL NUEVO CONTACTO"}))
            response.status_code = 400
            return response
    except:
        response = make_response(jsonify({'status':'error','PracticasI': "ERROR DE CONEXION CON EL SERVIDOR"}))
        response.status_code = 500
        return response

#Endpoint para modificar el numero de telefono de un contacto
@app.route('/ModificarTelefono/<id>', methods=['PUT'])
def ModificarTelefono(id):
    try:
        data = request.get_json()
        telefono = data['telefono']
        flag = controlador.ModificarTelefono(telefono, id)
        if flag is not None:
            response = make_response(jsonify({'status':'success','PracticasI': flag}))
            response.status_code = 200
            return response
        else:
            response = make_response(jsonify({'status':'error','PracticasI': "NO SE HA PODIDO ACTUALIZAR EL NUMERO DE TELEFONO DEL CONTACTO"}))
            response.status_code = 400
            return response
    except:
        response = make_response(jsonify({'status':'error','PracticasI': "ERROR DE CONEXION CON EL SERVIDOR"}))
        response.status_code = 500
        return response

#Endpoint para Eliminar un contacto de la base de datos
@app.route('/EliminarContacto/<id>', methods=['DELETE'])
def EliminarContacto(id):
    try:
        flag = controlador.EliminarContacto(id)
        if flag is not None:
            response = make_response(jsonify({'status':'success','PracticasI': flag}))
            response.status_code = 200
            return response
        else:
            response = make_response(jsonify({'status':'error','PracticasI': "NO SE HA PODIDO ELIMINAR EL CONTACTO"}))
            response.status_code = 400
            return response
    except:
        response = make_response(jsonify({'status':'error','PracticasI': "ERROR DE CONEXION CON EL SERVIDOR"}))
        response.status_code = 500
        return response
    
#Endpoint para mostrar todos los contactos
@app.route('/MostrarContactos', methods=['GET'])
def MostrarContactos():
    try:
        contactos = controlador.MostrarContactos()
        if contactos is not None:
            response = make_response(jsonify({'status':'success', 'PracticasI':contactos}))
            response.status_code = 200
            return response
        else:
            response = make_response(jsonify({'status':'error', 'PracticasI':'ERROR AL OBTENER LOS CONTACTOS'}))
            response.status_code = 400
            return response  
    except:
        response = make_response(jsonify({'status':'error','PracticasI': 'ERROR DE COMUNICACION'}))
        response.status_code = 500
        return response
    
if __name__ == '__main__':
    print("SERVIDOR INICIADO EN EL PUERTO: 5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
    
