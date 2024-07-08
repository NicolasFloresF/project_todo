-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: localhost    Database: Just_TODO_it
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.22.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(255) NOT NULL,
  `categoryColor` char(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (1,'Work','#6E18A3'),(2,'Study','#20C92C'),(3,'Personal','#5DA8FC'),(4,'Other','#FAD02A');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `eventName` varchar(45) NOT NULL,
  `eventDate` datetime(6) NOT NULL,
  `event_description` varchar(255) DEFAULT NULL,
  `eventPriority` varchar(45) DEFAULT NULL,
  `EventHasDeadline` tinyint NOT NULL,
  `EventStatus` tinyint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (1,'Event 1','2021-10-10 00:00:00.000000','Description 1','High',1,0),(2,'Event 2','2021-10-10 00:00:00.000000','Description 2','Medium',0,1),(3,'Event 3','2021-10-10 00:00:00.000000','Description 3','Low',1,0),(4,'Event 4','2021-10-10 00:00:00.000000','Description 4','High',0,0),(5,'Event 5','2021-10-10 00:00:00.000000','Description 5','Medium',1,0);
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EventCategory`
--

DROP TABLE IF EXISTS `EventCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EventCategory` (
  `Category_idCategory` int NOT NULL,
  `Event_idEvent` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `fk_Category_has_Event_Event1_idx` (`Event_idEvent`),
  KEY `fk_Category_has_Event_Category_idx` (`Category_idCategory`),
  CONSTRAINT `fk_Category_has_Event_Category` FOREIGN KEY (`Category_idCategory`) REFERENCES `Category` (`id`),
  CONSTRAINT `fk_Category_has_Event_Event1` FOREIGN KEY (`Event_idEvent`) REFERENCES `Event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EventCategory`
--

LOCK TABLES `EventCategory` WRITE;
/*!40000 ALTER TABLE `EventCategory` DISABLE KEYS */;
INSERT INTO `EventCategory` VALUES (1,1,1),(3,1,3),(2,3,4),(2,4,5),(2,2,6);
/*!40000 ALTER TABLE `EventCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Occurrence`
--

DROP TABLE IF EXISTS `Occurrence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Occurrence` (
  `id` int NOT NULL AUTO_INCREMENT,
  `OccurrenceDeadlineDate` date NOT NULL,
  `Event_idEvent` int NOT NULL,
  `OccurrenceStatus` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Occurrence_Event1_idx` (`Event_idEvent`),
  CONSTRAINT `fk_Occurrence_Event1` FOREIGN KEY (`Event_idEvent`) REFERENCES `Event` (`id`),
  CONSTRAINT `Occurrence_ibfk_1` FOREIGN KEY (`Event_idEvent`) REFERENCES `Event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Occurrence`
--

LOCK TABLES `Occurrence` WRITE;
/*!40000 ALTER TABLE `Occurrence` DISABLE KEYS */;
INSERT INTO `Occurrence` VALUES (1,'2024-08-17',1,1),(2,'2024-09-10',3,0),(3,'2024-10-05',5,1);
/*!40000 ALTER TABLE `Occurrence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-08 14:01:08
