from Clase_libro import Libro

class Biblioteca:
    
    def __init__(self, nombre): #Atributos clase biblioteca 
        self._nombre=nombre
        self._libros=[]
    
    def agregar_libro(self,libro):
        self._libros.append(libro)
    
    def buscar_libros_autor(self, autor):
        print(f"Libros Autor:  {autor}:\n")
        for libro in self._libros:
            if libro.Autor.lower() == autor.lower():
                self.mostrar_libro(libro)


    
    def mostrar_libro(self,libro):
        print(f"Libro->     Titulo: {libro._Titulo}, Autor   {libro._Autor},  Genero:  {libro._Genero}")
    
    def buscar_libros_genero(self, genero):
        print(f"Libros del genero: {genero} :\n")
        for libro in self._libros:
            if libro.Genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    
    def buscar_libros_titulo(self, titulo):
        print(f"Libro con el titulo:{titulo} \n")
        for libro in self._libros:
            if libro.Titulo.lower() == titulo.lower():
                self.mostrar_libro(libro)

    
    def mostrat_todos_libros(self):
        print(f"\nTodos los libros de la biblioteca {self._nombre}")
        for libro in self._libros:
            self.mostrar_libro(libro)

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def libros(self):
        return self._libros

