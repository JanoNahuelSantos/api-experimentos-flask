class Cientifico:
    
    @classmethod
    def fromDiccionario(cls, dicc: dict) -> 'Cientifico':
        if not isinstance (dicc, dict):
            raise ValueError("Los datos deben ser un diccionario.")
        if 'dni' not in dicc or 'nombre' not in dicc or 'apellido' not in dicc or 'titulo_academico' not in dicc or 'correo' not in dicc:
            raise ValueError("Faltan campos obligatorios en el diccionario.")
        return cls(
            dni = dicc["dni"], 
            nombre = dicc["nombre"], 
            apellido = dicc["apellido"], 
            titulo_academico = dicc["titulo_academico"], 
            correo = dicc["correo"])
    

    def __init__(self, dni:int, nombre:str, apellido:str, titulo_academico:str, correo:str):
        #validaciones
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("DNI debe ser un entero positivo.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre debe ser una cadena no vacía.")   
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("Apellido debe ser una cadena no vacía.")
        if not isinstance(titulo_academico, str) or not titulo_academico.strip():
            raise ValueError("Título académico debe ser una cadena no vacía.")
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("Correo debe ser una cadena no vacía.")
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__titulo_academico = titulo_academico
        self.__correo = correo

    def obtener_dni(self):
        return self.__dni

    def obtener_nombre(self):
        return self.__nombre

    def obtener_apellido(self):
        return self.__apellido

    def obtener_correo(self):
        return self.__correo

    def obtener_titulo_academico(self):
        return self.__titulo_academico

    def establecer_dni(self, dni: int):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("DNI debe ser un entero positivo.")
        self.__dni = dni

    def establecer_nombre(self, nombre: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre debe ser una cadena no vacía.")
        self.__nombre = nombre

    def establecer_apellido(self, apellido: str):
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("Apellido debe ser una cadena no vacía.")
        self.__apellido = apellido

    def establecer_titulo_academico(self, titulo_academico: str):
        if not isinstance(titulo_academico, str) or not titulo_academico.strip():
            raise ValueError("Título académico debe ser una cadena no vacía.")
        self.__titulo_academico = titulo_academico

    def establecer_correo(self, correo: str):
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("Correo debe ser una cadena no vacía.")
        self.__correo = correo

    def toDiccionario(self):
        return {
            'dni': self.__dni,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'titulo_academico': self.__titulo_academico,
            'correo': self.__correo
        }
    
