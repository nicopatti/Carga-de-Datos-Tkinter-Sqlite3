import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("C:/Users/nico/Desktop/Proyecto/Aplicaciones Gise/Base de datos Alumnos/bd1.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into alumnos(nombre, apellido, DNI, fecha_de_nacimiento, direccion, telefono, mail) values (?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, apellido, DNI, fecha_de_nacimiento, direccion, telefono, mail from alumnos where codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, nombre, apellido, DNI, fecha_de_nacimiento, direccion, telefono, mail from alumnos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from alumnos where codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update alumnos set nombre=?, apellido=?, DNI=?, fecha_de_nacimiento=?, direccion=?, telefono=?,mail=?  where codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()