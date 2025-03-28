class Libro:
    def __init__(self,Titulo,Autor,Genero):
        self._Titulo=Titulo
        self._Autor=Autor
        self._Genero=Genero

    @property
    def Titulo(self):
        return self._Titulo

    @property
    def Autor(self):
        return self._Autor

    @property
    def Genero (self):
        return self._Genero
    
    
        