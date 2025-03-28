from Clase_libro import Libro
from Clase_Biblioteca import Biblioteca

Biblioteca_Nacional= Biblioteca("Biblioteca Nacional")

print(f"Bienvenidos a la {Biblioteca_Nacional.nombre}")

libro1=Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 'Ficcion')
libro2=Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro3=Libro('El amor en los tiempos de colera','Gabriel Garcia Marquez','Ficcion')
libro4=Libro('Pedro Paramo','Juan Rulfo','Ficcion')
libro5=Libro('Pantaleon y los visitadores','Mario Vargas LLosa', 'Comedia')

#agregamos libros
Biblioteca_Nacional.agregar_libro(libro1)
Biblioteca_Nacional.agregar_libro(libro2)
Biblioteca_Nacional.agregar_libro(libro3)
Biblioteca_Nacional.agregar_libro(libro4)
Biblioteca_Nacional.agregar_libro(libro5)

Biblioteca_Nacional.mostrat_todos_libros()

Biblioteca_Nacional.buscar_libros_titulo('Cien años de soledad')
print("")

Biblioteca_Nacional.buscar_libros_genero('Comedia')
print("")

Biblioteca_Nacional.buscar_libros_autor('Juan Rulfo')

