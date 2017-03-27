-- MySQL dump 10.13  Distrib 5.7.12, for Linux (x86_64)
--
-- Host: localhost    Database: cdn_db
-- ------------------------------------------------------
-- Server version	5.7.12

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
-- Table structure for table `cdn`
--

DROP TABLE IF EXISTS `cdn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdn` (
  `idcdn` int(11) NOT NULL AUTO_INCREMENT,
  `iduser` int(11) NOT NULL,
  `namecdn` varchar(200) NOT NULL,
  `qoe` int(11) NOT NULL,
  `timestart` datetime NOT NULL,
  `timeend` datetime NOT NULL,
  `validatetime` tinyint(1) NOT NULL,
  `started` tinyint(1) NOT NULL,
  `destroy` tinyint(1) NOT NULL,
  PRIMARY KEY (`idcdn`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdn`
--

LOCK TABLES `cdn` WRITE;
/*!40000 ALTER TABLE `cdn` DISABLE KEYS */;
/*!40000 ALTER TABLE `cdn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cdnmachine`
--

DROP TABLE IF EXISTS `cdnmachine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdnmachine` (
  `idcdn` int(11) NOT NULL,
  `idmachine` varchar(200) NOT NULL,
  UNIQUE KEY `idcdn` (`idcdn`,`idmachine`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdnmachine`
--

LOCK TABLES `cdnmachine` WRITE;
/*!40000 ALTER TABLE `cdnmachine` DISABLE KEYS */;
/*!40000 ALTER TABLE `cdnmachine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cdnservice`
--

DROP TABLE IF EXISTS `cdnservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdnservice` (
  `idcdn` int(11) NOT NULL,
  `idservice` int(11) NOT NULL,
  `numsub` int(11) NOT NULL,
  `numvid` int(11) NOT NULL,
  PRIMARY KEY (`idcdn`,`idservice`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdnservice`
--

LOCK TABLES `cdnservice` WRITE;
/*!40000 ALTER TABLE `cdnservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `cdnservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machine`
--

DROP TABLE IF EXISTS `machine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `machine` (
  `idmachine` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `flavor` varchar(200) NOT NULL,
  `idservice` int(11) NOT NULL,
  `destroy` tinyint(1) NOT NULL,
  PRIMARY KEY (`idmachine`),
  UNIQUE KEY `idmachine` (`idmachine`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine`
--

LOCK TABLES `machine` WRITE;
/*!40000 ALTER TABLE `machine` DISABLE KEYS */;
/*!40000 ALTER TABLE `machine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicearea`
--

DROP TABLE IF EXISTS `servicearea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicearea` (
  `idservice` int(11) NOT NULL AUTO_INCREMENT,
  `regionservice` varchar(200) NOT NULL,
  `auth_url` varchar(200) NOT NULL,
  `auth_username` varchar(200) NOT NULL,
  `auth_password` varchar(200) NOT NULL,
  `project_name` varchar(200) NOT NULL,
  `region_name` varchar(200) NOT NULL,
  PRIMARY KEY (`idservice`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicearea`
--

LOCK TABLES `servicearea` WRITE;
/*!40000 ALTER TABLE `servicearea` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicearea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL AUTO_INCREMENT,
  `firstnameuser` varchar(200) NOT NULL,
  `lastnameuser` varchar(200) NOT NULL,
  `login` varchar(200) NOT NULL,
  `pwd` varchar(200) NOT NULL,
  `secretquestion` varchar(20) NOT NULL,
  `secretanswer` varchar(20) NOT NULL,
  PRIMARY KEY (`iduser`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-02 15:56:27
