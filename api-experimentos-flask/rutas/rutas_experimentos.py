from flask import Blueprint, jsonify, request
from modelos.entidades.experimento import Experimento
from modelos.repositorios.repositorios import obtener_repositorio_experimentos, obtener_repositorio_cientificos

bp_experimentos = Blueprint('experimentos', __name__)
repo_experimentos = obtener_repositorio_experimentos()
repo_cientificos = obtener_repositorio_cientificos()


@bp_experimentos.route('/experimentos', methods=['GET'])
def listar():
    resultados = []
    for e in repo_experimentos.obtener_todos():
        resultados.append(e.toDiccionario())
    return jsonify(resultados), 200


@bp_experimentos.route('/<int:id>', methods=['GET'])
def obtener_por_id(id):
    exp = repo_experimentos.obtener_por_id(id)
    if not exp:
        return jsonify({'error': 'no encontrado'}), 404
    return jsonify(exp.toDiccionario()), 200


@bp_experimentos.route('/experimentos', methods=['POST'])
def crear():
    if request.is_json:
        datos = request.get_json()
        experimento_nuevo = Experimento.fromDiccionario(datos)
        if repo_cientificos.existe_cientifico(experimento_nuevo.obtener_autor().obtener_dni()):
            if repo_experimentos.agregar(experimento_nuevo):
                return jsonify(experimento_nuevo.toDiccionario()), 201
            else:
                return jsonify({'error': 'El experimento ya existe'}), 400
        else:
            return jsonify({'error': 'El científico no existe'}), 400
    return jsonify({'error': 'Los datos no están en formato JSON'}), 400

@bp_experimentos.route('/<int:id>', methods=['DELETE'])
def eliminar(id):
    experimento = repo_experimentos.obtener_por_id(id)
    if experimento:
        repo_experimentos.eliminar(id)
        return jsonify({'mensaje': 'Experimento eliminado'}), 200
    else:
        return jsonify({'error': 'Experimento no encontrado'}), 404
    

@bp_experimentos.route('/<int:id>', methods=['PUT'])
def actualizar(id):
    if not request.is_json:
        return jsonify({'error': 'Los datos no están en formato JSON'}), 400

    cambios = request.get_json()

    #valido autor
    if 'autor' in cambios:
        autor_datos = cambios['autor']
        #es dict y tiene id?
        if not isinstance(autor_datos, dict) or 'dni' not in autor_datos:
            return jsonify({'error': 'Los datos del autor deben ser un diccionario válido con DNI.'}), 400
        #existe cientifico?
        dni_autor = autor_datos['dni']
        if not repo_cientificos.existe_cientifico(dni_autor):
            return jsonify({'error': 'El científico autor no existe en el sistema.'}), 400
 
    try:
        if repo_experimentos.actualizar(id, cambios):
            exp_actualizado = repo_experimentos.obtener_por_id(id)
            return jsonify(exp_actualizado.toDiccionario()), 200
        else:
            return jsonify({'error': 'Experimento no encontrado'}), 404
    except ValueError as e:
        return jsonify({'error': f'Error de validación de datos: {str(e)}'}), 400
