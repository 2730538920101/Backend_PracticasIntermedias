import controlador
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS


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
    

    
if __name__ == '__main__':
    print("SERVIDOR INICIADO EN EL PUERTO: 5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
    
