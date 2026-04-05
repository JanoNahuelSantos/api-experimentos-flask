from modelos.entidades.cientifico import Cientifico
class Experimento:

    __ID = 0 #con esto no repito id nunca


    #faltaba el fromDiccionario
    @classmethod
    def fromDiccionario(cls, dicc: dict):
        if not isinstance (dicc, dict):
            raise ValueError("Los datos deben ser un diccionario.")
        if 'id' not in dicc or 'titulo' not in dicc or 'descripcion' not in dicc or 'resultado' not in dicc or 'fecha' not in dicc or 'autor' not in dicc:
            raise ValueError("Faltan campos obligatorios en el diccionario.")
        autor_datos = dicc["autor"]
        if not isinstance(autor_datos, dict):
            raise ValueError("Los datos del autor deben ser un diccionario.")
        objeto_autor = Cientifico.fromDiccionario(autor_datos)
        return cls(
            id = dicc("id", None),
            titulo = dicc["titulo"],
            descripcion = dicc["descripcion"],
            resultado = dicc["resultado"],
            fecha = dicc["fecha"],
            autor = objeto_autor
        )
    
    @classmethod
    def establecerUltimoID(cls, ultimo_id):
        if not isinstance(ultimo_id, int) or ultimo_id < 0:
            raise ValueError("El ID debe ser un entero no negativo.")
        cls.__ID = ultimo_id

    @classmethod
    def obtenerUltimoID(cls):
        return cls.__ID
    
    @classmethod
    def generarID(cls):
        cls.__ID += 1
        return cls.__ID

    def __init__(self, titulo:str, descripcion:str, resultado:str, fecha:str, autor:Cientifico, id:int|None=None):
        #validaciones
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título debe ser una cadena no vacía.")
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción debe ser una cadena no vacía.")
        if not isinstance(resultado, str) or not resultado.strip():
            raise ValueError("El resultado debe ser una cadena no vacía.")
        if not isinstance(fecha, str) or not fecha.strip():
            raise ValueError("La fecha debe ser una cadena no vacía.")
        if not isinstance(autor, Cientifico):
            raise ValueError("El autor debe ser una instancia de Cientifico.")
        if id is not None and (not isinstance(id, int) or id <= 0):
            raise ValueError("El ID debe ser un entero positivo si se proporciona.")
        if id is None:
            id = self.generarID()
        else:
            if id > self.__ID:
                Experimento.__ID = id
        self.__id = id
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__resultado = resultado
        self.__fecha = fecha
        self.__autor =  autor

    def obtener_id(self)->int:
        return self.__id
    
    def obtener_titulo(self):
        return self.__titulo

    def obtener_descripcion(self):
        return self.__descripcion

    def obtener_resultado(self):
        return self.__resultado

    def obtener_fecha(self):
        return self.__fecha

    def obtener_autor(self):
        return self.__autor

    def establecer_titulo(self, titulo:str):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título debe ser una cadena no vacía.")
        self.__titulo = titulo

    def establecer_descripcion(self, descripcion:str):
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción debe ser una cadena no vacía.")
        self.__descripcion = descripcion

    def establecer_resultado(self, resultado:str):
        if not isinstance(resultado, str) or not resultado.strip():
            raise ValueError("El resultado debe ser una cadena no vacía.")
        self.__resultado = resultado

    def establecer_fecha(self, fecha:str):
        if not isinstance(fecha, str) or not fecha.strip():
            raise ValueError("La fecha debe ser una cadena no vacía.")
        self.__fecha = fecha

    def establecer_autor(self, autor: Cientifico):
        if not isinstance(autor, Cientifico):
            raise ValueError("El autor debe ser una instancia de Cientifico.")
        self.__autor = autor

    def __str__(self):
        return f"ID: {self.__id}, Título: {self.__titulo}, Descripción: {self.__descripcion}, Resultado: {self.__resultado}, Fecha: {self.__fecha}, Autor: {self.__autor.obtener_nombre()} {self.__autor.obtener_apellido()}"
    
    #falta el toDiccionario
    def toDiccionario(self):
        return {
            'id': self.__id,
            'titulo': self.__titulo,
            'descripcion': self.__descripcion,
            'resultado': self.__resultado,
            'fecha': self.__fecha,
            'autor': self.__autor.toDiccionario()
        }
