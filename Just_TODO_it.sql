--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
CREATE TABLE `Category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(255) NOT NULL,
  `categoryColor` char(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
INSERT INTO `Category` VALUES (1,'Work','#6E18A3'),(2,'Study','#20C92C'),(3,'Personal','#5DA8FC'),(4,'Other','#FAD02A');
UNLOCK TABLES;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
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

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
INSERT INTO `Event` VALUES (1,'Event 1','2021-10-10 00:00:00.000000','Description 1','High',1,0),(2,'Event 2','2021-10-10 00:00:00.000000','Description 2','Medium',0,1),(3,'Event 3','2021-10-10 00:00:00.000000','Description 3','Low',1,0),(4,'Event 4','2021-10-10 00:00:00.000000','Description 4','High',0,0),(5,'Event 5','2021-10-10 00:00:00.000000','Description 5','Medium',1,0);
UNLOCK TABLES;

--
-- Table structure for table `EventCategory`
--

DROP TABLE IF EXISTS `EventCategory`;
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

--
-- Dumping data for table `EventCategory`
--

LOCK TABLES `EventCategory` WRITE;
INSERT INTO `EventCategory` VALUES (1,1,1),(3,1,3),(2,3,4),(2,4,5),(2,2,6);
UNLOCK TABLES;

--
-- Table structure for table `Occurrence`
--

DROP TABLE IF EXISTS `Occurrence`;
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

--
-- Dumping data for table `Occurrence`
--

LOCK TABLES `Occurrence` WRITE;
INSERT INTO `Occurrence` VALUES (1,'2024-08-17',1,1),(2,'2024-09-10',3,0),(3,'2024-10-05',5,1);
UNLOCK TABLES;
