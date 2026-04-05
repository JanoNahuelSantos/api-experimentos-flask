from flask import Flask
from rutas.rutas_experimentos import bp_experimentos
from modelos.repositorios.repositorios import obtener_repositorio_experimentos, obtener_repositorio_cientificos

try:
    obtener_repositorio_cientificos()
    obtener_repositorio_experimentos()
    print("Repositorios inicializados correctamente.")
except Exception as e:
    # Capturar y reportar errores de carga de archivos (ej. JSON malformado)
    print(f"Error CRÍTICO al inicializar repositorios: {e}")

app = Flask(__name__) #creamos una instancia de la clase Flask

#registramos el blueprint
app.register_blueprint(bp_experimentos, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #iniciamos la aplicación
