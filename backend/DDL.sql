-- MySQL dump 10.13  Distrib 5.7.34, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.34-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carrito`
--

DROP TABLE IF EXISTS `carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carrito` (
  `idCarrito` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idCarrito`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito`
--

LOCK TABLES `carrito` WRITE;
/*!40000 ALTER TABLE `carrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoria` (
  `categoria` varchar(45) NOT NULL,
  `idProducto` int(11) NOT NULL,
  PRIMARY KEY (`categoria`,`idProducto`),
  KEY `idProducto_categoria` (`idProducto`),
  CONSTRAINT `idProducto_categoria` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compra` (
  `idCompra` int(11) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `idDir` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  PRIMARY KEY (`idCompra`),
  KEY `correo_dirComprador_compra` (`correo`),
  KEY `idDir_compra` (`idDir`),
  KEY `numero_compra` (`numero`),
  CONSTRAINT `correo_comprador_compra` FOREIGN KEY (`correo`) REFERENCES `comprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `correo_dirComprador_compra` FOREIGN KEY (`correo`) REFERENCES `direccionComprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `correo_tarComprador_compra` FOREIGN KEY (`correo`) REFERENCES `tarjetaComprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `idDir_compra` FOREIGN KEY (`idDir`) REFERENCES `direccionComprador` (`idDir`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `numero_compra` FOREIGN KEY (`numero`) REFERENCES `tarjetaComprador` (`numero`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comprador`
--

DROP TABLE IF EXISTS `comprador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comprador` (
  `correo` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `contrasenia` varchar(106) NOT NULL,
  PRIMARY KEY (`correo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comprador`
--

LOCK TABLES `comprador` WRITE;
/*!40000 ALTER TABLE `comprador` DISABLE KEYS */;
/*!40000 ALTER TABLE `comprador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contener`
--

DROP TABLE IF EXISTS `contener`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contener` (
  `idProducto` int(11) NOT NULL,
  `idCarrito` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  KEY `idProducto_contener` (`idProducto`),
  KEY `idCarrito_contener` (`idCarrito`),
  CONSTRAINT `idCarrito_contener` FOREIGN KEY (`idCarrito`) REFERENCES `carrito` (`idCarrito`),
  CONSTRAINT `idProducto_contener` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contener`
--

LOCK TABLES `contener` WRITE;
/*!40000 ALTER TABLE `contener` DISABLE KEYS */;
/*!40000 ALTER TABLE `contener` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccionComprador`
--

DROP TABLE IF EXISTS `direccionComprador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccionComprador` (
  `idDir` int(11) NOT NULL AUTO_INCREMENT,
  `correo` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `colonia` varchar(45) NOT NULL,
  `cp` int(11) NOT NULL,
  `calle` varchar(45) NOT NULL,
  `numero` int(11) NOT NULL,
  PRIMARY KEY (`idDir`,`correo`),
  KEY `correo_dirComprador` (`correo`),
  CONSTRAINT `correo_dirComprador` FOREIGN KEY (`correo`) REFERENCES `comprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccionComprador`
--

LOCK TABLES `direccionComprador` WRITE;
/*!40000 ALTER TABLE `direccionComprador` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccionComprador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccionVendedor`
--

DROP TABLE IF EXISTS `direccionVendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccionVendedor` (
  `idDir` int(11) NOT NULL AUTO_INCREMENT,
  `correo` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `colonia` varchar(45) NOT NULL,
  `cp` varchar(45) NOT NULL,
  `calle` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  PRIMARY KEY (`idDir`,`correo`),
  KEY `correo_dirVendedor` (`correo`),
  CONSTRAINT `correo_dirVendedor` FOREIGN KEY (`correo`) REFERENCES `vendedor` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccionVendedor`
--

LOCK TABLES `direccionVendedor` WRITE;
/*!40000 ALTER TABLE `direccionVendedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccionVendedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagen`
--

DROP TABLE IF EXISTS `imagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imagen` (
  `imagen` varchar(45) NOT NULL,
  `idProducto` int(11) NOT NULL,
  PRIMARY KEY (`imagen`,`idProducto`),
  KEY `idProducto_imagen` (`idProducto`),
  CONSTRAINT `idProducto_imagen` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagen`
--

LOCK TABLES `imagen` WRITE;
/*!40000 ALTER TABLE `imagen` DISABLE KEYS */;
/*!40000 ALTER TABLE `imagen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incluir`
--

DROP TABLE IF EXISTS `incluir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `incluir` (
  `idProducto` int(11) NOT NULL,
  `idCompra` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  KEY `idProducto_incluir` (`idProducto`),
  KEY `idCompra_incluir` (`idCompra`),
  CONSTRAINT `idCompra_incluir` FOREIGN KEY (`idCompra`) REFERENCES `compra` (`idCompra`),
  CONSTRAINT `idProducto_incluir` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incluir`
--

LOCK TABLES `incluir` WRITE;
/*!40000 ALTER TABLE `incluir` DISABLE KEYS */;
/*!40000 ALTER TABLE `incluir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opinar`
--

DROP TABLE IF EXISTS `opinar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opinar` (
  `correo` varchar(45) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `opinion` longtext,
  `calificacion` int(11) DEFAULT NULL,
  KEY `correo_opinar` (`correo`),
  KEY `idProducto_opinar` (`idProducto`),
  CONSTRAINT `correo_opinar` FOREIGN KEY (`correo`) REFERENCES `comprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `idProducto_opinar` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opinar`
--

LOCK TABLES `opinar` WRITE;
/*!40000 ALTER TABLE `opinar` DISABLE KEYS */;
/*!40000 ALTER TABLE `opinar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pertenecer`
--

DROP TABLE IF EXISTS `pertenecer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pertenecer` (
  `correo` varchar(45) NOT NULL,
  `idCarrito` int(11) NOT NULL,
  KEY `correo_pertenecer` (`correo`),
  KEY `idCarrito_pertenecer` (`idCarrito`),
  CONSTRAINT `correo_pertenecer` FOREIGN KEY (`correo`) REFERENCES `comprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `idCarrito_pertenecer` FOREIGN KEY (`idCarrito`) REFERENCES `carrito` (`idCarrito`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pertenecer`
--

LOCK TABLES `pertenecer` WRITE;
/*!40000 ALTER TABLE `pertenecer` DISABLE KEYS */;
/*!40000 ALTER TABLE `pertenecer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto` (
  `idProducto` int(11) NOT NULL AUTO_INCREMENT,
  `correo` varchar(45) NOT NULL,
  `precio` float NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `vendidos` int(11) NOT NULL,
  `disponibles` int(11) NOT NULL,
  PRIMARY KEY (`idProducto`),
  KEY `correo_producto` (`correo`),
  CONSTRAINT `correo_producto` FOREIGN KEY (`correo`) REFERENCES `vendedor` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjetaComprador`
--

DROP TABLE IF EXISTS `tarjetaComprador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tarjetaComprador` (
  `numero` int(11) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `dueno` varchar(45) NOT NULL,
  `fechaCad` date NOT NULL,
  `cvv` int(11) NOT NULL,
  PRIMARY KEY (`numero`,`correo`),
  KEY `correo_tarjetaComprador` (`correo`),
  CONSTRAINT `correo_tarjetaComprador` FOREIGN KEY (`correo`) REFERENCES `comprador` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjetaComprador`
--

LOCK TABLES `tarjetaComprador` WRITE;
/*!40000 ALTER TABLE `tarjetaComprador` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarjetaComprador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjetaVendedor`
--

DROP TABLE IF EXISTS `tarjetaVendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tarjetaVendedor` (
  `numero` int(11) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `duenio` varchar(45) NOT NULL,
  `fechaCad` date NOT NULL,
  `cvv` int(11) NOT NULL,
  PRIMARY KEY (`numero`,`correo`),
  KEY `correo_tarjetaVendedor` (`correo`),
  CONSTRAINT `correo_tarjetaVendedor` FOREIGN KEY (`correo`) REFERENCES `vendedor` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjetaVendedor`
--

LOCK TABLES `tarjetaVendedor` WRITE;
/*!40000 ALTER TABLE `tarjetaVendedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarjetaVendedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendedor`
--

DROP TABLE IF EXISTS `vendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendedor` (
  `nombre` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `contrasenia` varchar(45) DEFAULT NULL,
  `correo` varchar(45) NOT NULL,
  PRIMARY KEY (`correo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendedor`
--

LOCK TABLES `vendedor` WRITE;
/*!40000 ALTER TABLE `vendedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-30 13:01:04
