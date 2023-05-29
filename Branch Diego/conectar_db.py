
import mysql.connector

class Conectar_Base_de_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port= 3306,
                user= 'root',
                password = '1234',
                db = 'big_bread'
            )
        except mysql.connector.Error as descripcionError:
             print ("¡No se a conectado la base de datos!",descripcionError)
    


