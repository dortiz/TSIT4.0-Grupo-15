
import mysql.connector

class Conectar_Base_de_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port= 3306,
                user= 'root',
                password = '1234',
                db = 'db_group15_innova'
            )
        except mysql.connector.Error as descripcionError:
             print ("¡No se a conectado la base de datos!",descripcionError)
    


