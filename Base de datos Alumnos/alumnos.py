import sqlite3

class Alumnos:

    #Funcion que conecta con la base de datos
    def abrir(self):
        conexion=sqlite3.connect("C:/Users/nico/Desktop/Proyecto/Aplicaciones Gise/Base de datos Alumnos/Alumnos.db")
        return conexion


    #Funcion alta de alumno
    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into alumnos(nombre, apellido, DNI, fecha_de_nacimiento, direccion, telefono, mail) values (?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    #Funcion que consulta un alumno
    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, apellido, fecha_de_nacimiento, direccion, telefono, mail from alumnos where DNI=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    #Funcion que trae todos los alumnos        
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select DNI, nombre, apellido, fecha_de_nacimiento, direccion, telefono, mail from alumnos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    #Funcion que da de baja un alumno
    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from alumnos where DNI=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    #Funcion que modifica un alumno
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update alumnos set nombre=?, apellido=?, fecha_de_nacimiento=?, direccion=?, telefono=?,mail=?  where DNI=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()