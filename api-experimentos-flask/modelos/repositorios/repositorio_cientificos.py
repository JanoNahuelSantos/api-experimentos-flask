import json
from modelos.entidades.cientifico import Cientifico

class RepositorioCientificos:
    __RUTA_ARCHIVO = 'datos/cientificos.json'

    def __init__(self):
        self.__cientificos = []
        self.__cargar_todos()

    def __cargar_todos(self):
        lista_datos = []
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding='utf-8') as f:
                lista_datos = json.load(f)
        except FileNotFoundError:
            print("Archivo de cientificos no encontrado, iniciando con lista vacía.")
        for d in lista_datos:
            obj = Cientifico.fromDiccionario(d)
            self.__cientificos.append(obj)
    
    def __guardar_todos(self):
        try:
            datos = []
            for e in self.__cientificos:
                datos.append(e.toDiccionario())
            with open(self.__RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def obtener_todos(self):
        return self.__cientificos

    #Faltaba el obtener a una persona unica por dni.
    def obtener_por_dni(self, dni:int) -> Cientifico | None:
        for c in self.__cientificos:
            if c.obtener_dni() == dni:
                return c
        return None

    def existe_cientifico(self, dni):
        for c in self.__cientificos:
            if c.obtener_dni() == dni:
                return True
        return False
    
    #Metodo para la peticion POST
    def agregar(self, cientifico:Cientifico):
        if not self.existe_cientifico(cientifico.obtener_dni()):
            self.__cientificos.append(cientifico)
            self.__guardar_todos()
            return True
        return False

    #Metodo para la peticion PUT
    def actualizar(self, dni:int, cambios:dict):
        cientifico = self.obtener_por_dni(dni)
        if cientifico:
            if 'nombre' in cambios:
                cientifico.establecer_nombre(cambios['nombre'])
            if 'apellido' in cambios:
                cientifico.establecer_apellido(cambios['apellido'])
            if 'titulo_academico' in cambios:
                cientifico.establecer_titulo_academico(cambios['titulo_academico'])
            if 'correo' in cambios:
                cientifico.establecer_correo(cambios['correo'])
            self.__guardar_todos()
            return True
        return False

    #Metodo para la peticion DELETE
    def eliminar(self, dni:int):
        for c in self.__cientificos:
            if c.obtener_dni() == dni:
                self.__cientificos.remove(c)
                self.__guardar_todos()
                return True
        return False