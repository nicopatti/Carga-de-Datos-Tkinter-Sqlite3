import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table alumnos (
                              DNI integer primary key,
                              nombre TEXT,
                              apellido TEXT,
                              fecha_de_nacimiento DATETIME,
                              direccion TEXT,
                              telefono INT,
                              mail text
                        )""")
    print("se creo la tabla alumnos")                        
except sqlite3.OperationalError:
    print("La tabla alumnos ya existe")                    
conexion.close()