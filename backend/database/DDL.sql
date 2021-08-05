-- MySQL Script generated by MySQL Workbench
-- Sat Jul 17 02:55:30 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering


SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- drop schema `mydb`;


-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;
-- -----------------------------------------------------
-- Table   `Vendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vendedor` (
  `nombre` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `contrasenia` VARCHAR(106) NULL,
  `correo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`correo`))
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `TarjetaVendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarjetaVendedor` (
  `numero` INT NOT NULL,
  correo varchar(45) not null,
  `duenio` VARCHAR(45) NOT NULL,
  `fechaCad` DATE NOT NULL,
  `cvv` INT NOT NULL,
  PRIMARY KEY (`numero`, correo),
  CONSTRAINT correo_tarjetaVendedor
    FOREIGN KEY (correo)
    REFERENCES   `vendedor` (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `DireccionVendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `direccionVendedor` (
  `idDir` INT NOT NULL AUTO_INCREMENT,
  correo varchar(45) not null,
  `estado` VARCHAR(45) NOT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `colonia` VARCHAR(45) NOT NULL,
  `cp` VARCHAR(45) NOT NULL,
  `calle` VARCHAR(45) NOT NULL,
  `numero` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDir`, correo),
  CONSTRAINT correo_dirVendedor
    FOREIGN KEY (correo)
    REFERENCES `vendedor` (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `Comprador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `comprador` (
  `correo` varchar(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `contrasenia` VARCHAR(106) NOT NULL,
  PRIMARY KEY (correo))
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `TarjetaComprador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarjetaComprador` (
  `numero` varchar(105) NOT NULL,
  correo varchar(45) not null,
  `dueno` VARCHAR(60) NOT NULL,
  `fechaCad` DATE NOT NULL,
  `cvv` INT NOT NULL,
  PRIMARY KEY (`numero`, correo),
  CONSTRAINT correo_tarjetaComprador
    FOREIGN KEY (correo)
    REFERENCES `comprador` (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table   `DireccionComprador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `direccionComprador` (
  idDir INT NOT NULL AUTO_INCREMENT,
  correo varchar(45) not null,
  `estado` VARCHAR(45) NOT NULL,
  `ciudad` VARCHAR(45) NOT NULL,
  `colonia` VARCHAR(45) NOT NULL,
  `cp` INT NOT NULL,
  `calle` VARCHAR(45) NOT NULL,
  `numero` INT NOT NULL,
  PRIMARY KEY (`idDir`, correo),
  CONSTRAINT correo_dirComprador
    FOREIGN KEY (correo)
    REFERENCES `comprador` (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `producto` (
  idProducto INT NOT NULL AUTO_INCREMENT,
  correo VARCHAR(45) not null,
  precio FLOAT NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  descripcion VARCHAR(500) NOT NULL,
  vendidos INT NOT NULL,
  disponibles INT NOT NULL,
  PRIMARY KEY (idProducto),
  CONSTRAINT correo_producto
    FOREIGN KEY (correo)
    REFERENCES  vendedor (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table   `Imagen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS   `imagen` (
  `imagen` VARCHAR(100) NOT NULL,
  `idProducto` int NOT NULL,
  PRIMARY KEY (`imagen`, idProducto),
  CONSTRAINT idProducto_imagen
    FOREIGN KEY (idProducto)
    REFERENCES   `producto` (idProducto)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table   `Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS   `categoria` (
  `categoria` VARCHAR(45) not NULL,
  idProducto int not null,
  primary key (categoria, idProducto),
  CONSTRAINT idProducto_categoria
    FOREIGN KEY (idProducto)
    REFERENCES   `producto` (idProducto)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `Carrito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carrito` (
  idCarrito INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (idCarrito))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table   `Opinar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `opinar` (
	correo varchar(45) not null,
	idProducto INT not null,
	`opinion` LONGTEXT NULL,
  	`calificacion` INT NULL,
  CONSTRAINT correo_opinar
    FOREIGN KEY (correo)
    REFERENCES `comprador` (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT idProducto_opinar
    FOREIGN KEY (idProducto)
    REFERENCES `producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;




-- -----------------------------------------------------
-- Table   `Contener`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `contener` (
	idProducto int not null,
	idCarrito int not null,
	cantidad INT NOT NULL,
	primary key (idProducto, idCarrito),
  CONSTRAINT idProducto_contener
    FOREIGN KEY (idProducto)
    REFERENCES   producto (idProducto),
  CONSTRAINT idCarrito_contener
    FOREIGN KEY (idCarrito)
    REFERENCES   carrito (idCarrito))
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table   `incluir`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `incluir` (
	idProducto int not null,
	idCompra int not null,
	`cantidad` INT NOT NULL,
	primary key (idProducto, idCompra),
  CONSTRAINT idProducto_incluir
    FOREIGN KEY (idProducto)
    REFERENCES   `producto` (idProducto)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT idCompra_incluir
    FOREIGN KEY (idCompra)
    REFERENCES   `compra` (idCompra))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table   `pertenecer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `pertenecer` (
	correo varchar(45) not null,
	idCarrito int not null,
	primary key (correo, idCarrito),
  CONSTRAINT correo_pertenecer
    FOREIGN KEY (correo)
    REFERENCES   `comprador` (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT idCarrito_pertenecer
    FOREIGN KEY (idCarrito)
    REFERENCES   `carrito` (idCarrito))
ENGINE = InnoDB;


-- drop table `mydb`.`pertenecer` ;


-- -----------------------------------------------------
-- Table   `Compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `compra` (
  idCompra INT NOT NULL AUTO_INCREMENT,
  correo varchar(45) not null,
  idDir int not null,
  numero varchar(105) not null,
  PRIMARY KEY (`idCompra`),
  CONSTRAINT correo_comprador_compra
    FOREIGN KEY (correo)
    REFERENCES   `comprador` (correo)
    ON DELETE NO ACTION         -- Cómo cambia respecto a las acciones
    ON UPDATE NO ACTION,        -- en las otras tablas
  CONSTRAINT correo_tarComprador_compra
    FOREIGN KEY (correo)
    REFERENCES   tarjetaComprador (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT correo_dirComprador_compra
    FOREIGN KEY (correo)
    REFERENCES   direccionComprador (correo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT idDir_compra
    FOREIGN KEY (idDir)
    REFERENCES   `direccionComprador` (idDir)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT numero_compra
    FOREIGN KEY (numero)
    REFERENCES   `tarjetaComprador` (numero)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;




SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
