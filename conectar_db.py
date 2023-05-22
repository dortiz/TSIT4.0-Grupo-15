
import mysql.connector

class Conectar_Base_de_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port= 3306,
                user= 'root',
                password = 'Lacarta2',
                db = 'db_ejemplo_innova'
            )
        except mysql.connector.Error as descripcionError:
             print ("¡No se a conectado la base de datos!",descripcionError)
    




