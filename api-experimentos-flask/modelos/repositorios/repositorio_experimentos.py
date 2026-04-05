import json
from modelos.entidades.experimento import Experimento
from modelos.entidades.cientifico import Cientifico
from repositorios.repositorio_cientificos import obtener_repositorio_cientificos

class RepositorioExperimentos:
    __RUTA_ARCHIVO = 'datos/experimentos.json'

    def __init__(self):
        self.__experimentos = []
        self.__cargar_todos()
        self.__repositorio_cientificos = obtener_repositorio_cientificos()

    def __cargar_todos(self):
        lista_datos = []
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding='utf-8') as f:
                lista_datos = json.load(f)
        except FileNotFoundError:
            print("Archivo de experimentos no encontrado, iniciando con lista vacía.")

        if "ultimo_id" in lista_datos:
            ultimo_id = lista_datos["ultimo_id"]
            Experimento.establecer_ultimo_id(ultimo_id)

        for d in lista_datos:
            obj = Experimento.fromDiccionario(d)
            self.__experimentos.append(obj)

    def __guardar_todos(self):
        datos = []
        for e in self.__experimentos:
            datos.append(e.toDiccionario())
        datos = {
            "ultimo_id": Experimento.obtenerUltimoID(), 
            "experimentos": datos
        }
        with open(self.__RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)

    def obtener_todos(self):
        return self.__experimentos

    def obtener_por_id(self, id:int)->Experimento|None:
        for e in self.__experimentos:
            if e.obtener_id() == id:
                return e
        return None
    
    #Faltaba el metodo POST
    def agregar(self, experimento:Experimento):
        if self.existe_experimento(experimento.obtener_id()):
            return False
        dni_autor = experimento.obtener_autor().obtener_dni()
        if not self.__repositorio_cientificos(experimento.obtener_autor().obtener_dni()):
            raise ValueError("El autor no existe como científico.")
        self.__experimentos.append(experimento)
        self.__guardar_todos()
        return True

    def existe_experimento(self, id:int)->bool:
        for e in self.__experimentos:
            if e.obtener_id() == id:
                return True
        return False

    def actualizar(self, id:int, cambios: dict):
        for e in self.__experimentos:
            if e.obtener_id() == id:
                if 'titulo' in cambios:
                    e.establecer_titulo(cambios['titulo'])
                if 'descripcion' in cambios:
                    e.establecer_descripcion(cambios['descripcion'])
                if 'resultado' in cambios:
                    e.establecer_resultado(cambios['resultado'])
                if 'fecha' in cambios:
                    e.establecer_fecha(cambios['fecha'])
                if 'autor' in cambios:
                    e.establecer_autor(Cientifico.fromDiccionario(cambios['autor']))
                self.__guardar_todos()
                return True
        return False
    
    def eliminar(self, id:int)->bool:
        for e in self.__experimentos:
            if e.obtener_id() == id:
                self.__experimentos.remove(e)
                self.__guardar_todos()
                return True
        return False
    
