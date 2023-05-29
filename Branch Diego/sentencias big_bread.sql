CREATE DATABASE big_bread;
USE big_bread;
CREATE TABLE Producto (
ID INT PRIMARY KEY,
Nombre VARCHAR(50),
Descripcion VARCHAR(255)
);
CREATE TABLE Insumo (
ID INT PRIMARY KEY,
Nombre VARCHAR(50),
Cantidad_Stock INT
);
CREATE TABLE Receta (
ID INT PRIMARY KEY,
ID_Producto INT,
FOREIGN KEY (ID_Producto) REFERENCES Producto(ID)
);
CREATE TABLE Receta_Insumo (
ID INT PRIMARY KEY,
ID_Receta INT,
ID_Insumo INT,
Cantidad_Requerida INT,
FOREIGN KEY (ID_Receta) REFERENCES Receta(ID),
FOREIGN KEY (ID_Insumo) REFERENCES Insumo(ID)
);
CREATE TABLE Produccion (
ID INT PRIMARY KEY,
Fecha DATE,
insumoIDNombreCantidad_StockPRIMARYCantidad INT
);



