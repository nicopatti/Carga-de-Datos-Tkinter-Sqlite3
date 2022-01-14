import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table alumnos (
                              codigo integer primary key autoincrement,
                              nombre text,
                              apellido text,
                              DNI text,
                              fecha_de_nacimiento text,
                              direccion text,
                              telefono text,
                              mail text
                        )""")
    print("se creo la tabla alumnos")                        
except sqlite3.OperationalError:
    print("La tabla alumnos ya existe")                    
conexion.close()