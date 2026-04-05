from flask import Blueprint, jsonify, request
from modelos.entidades.cientifico import Cientifico
from modelos.repositorios.repositorios import obtener_repositorio_cientificos

bp_cientificos = Blueprint('cientificos', __name__)
repo = obtener_repositorio_cientificos()


#falaba el metodo POST
@bp_cientificos.route('/cientificos', methods=['POST'])
def obtener_todos():
    lista = repo.obtener_todos()
    return jsonify([c.toDiccionario() for c in lista]), 200
    

@bp_cientificos.route('/cientificos/<int:dni>', methods=['GET'])
def obtener_por_dni(dni):
    cientifico = repo.obtener_por_dni(dni)
    if not cientifico:
        return jsonify({'error':'no encontrado'}), 404
    return jsonify(cientifico.toDiccionario()), 200

#faltaba agregar cientifico
@bp_cientificos.route('/cientificos', methods=['POST'])
def agregar_cientifico():
    if request.is_json:
        datos = request.get_json()
        try:
            nuevo = Cientifico.fromDiccionario(datos)
            if repo.agregar(nuevo):
                return jsonify({"Cientifico agregado correctamente...": nuevo.toDiccionario()}), 201
            else:
                return jsonify({'error': 'Ya existe un científico con ese DNI'}), 409
        except Exception as e:
            return jsonify({'error': f'Datos inválidos: {str(e)}'}), 400

@bp_cientificos.route('/cientificos/<int:dni>', methods=['PUT'])
def actualizar(dni):
    if request.is_json:
        cambios = request.get_json()
        if repo.actualizar(dni, cambios):
            cientifico_actualizado = repo.obtener_por_dni(dni)
            return jsonify(cientifico_actualizado.toDiccionario()), 200
        else:
            return jsonify({'error':'Científico no encontrado'}), 404
    return jsonify({'error':'Los datos no están en formato JSON'}), 400

@bp_cientificos.route('/cientificos/<int:dni>', methods=['DELETE'])
def eliminar(dni):
    if repo.eliminar(dni):
        return jsonify({'mensaje':'Científico eliminado'}), 200
    else:
        return jsonify({'error':'Científico no encontrado'}), 404
    
