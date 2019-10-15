-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: MG_JOURNEY
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `MG_JRNY_Creation`
--

DROP TABLE IF EXISTS `MG_JRNY_Creation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `MG_JRNY_Creation` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `journeyID` varchar(30) NOT NULL,
  `UserEmail` varchar(30) NOT NULL,
  `Journey_Duedate` date NOT NULL,
  `journeypurpose` varchar(100) NOT NULL,
  `Journey_Extension` date DEFAULT NULL,
  `journeytimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `journeytype` varchar(20) NOT NULL,
  `journeymode` varchar(20) NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MG_JRNY_Creation`
--

LOCK TABLES `MG_JRNY_Creation` WRITE;
/*!40000 ALTER TABLE `MG_JRNY_Creation` DISABLE KEYS */;
INSERT INTO `MG_JRNY_Creation` VALUES (12,'J1_1562394494','puttasachin6@gmail.com','2019-07-17','learning',NULL,'2019-07-06 06:28:13','open','destroy'),(14,'J1_1562580292','arjunputta12@gmail.com','2019-07-17','learning',NULL,'2019-07-08 10:04:52','open','destroy'),(21,'J1_1563265650','sachin6@gmail.com','2019-07-16','data science',NULL,'2019-07-16 08:27:29','public','destroy');
/*!40000 ALTER TABLE `MG_JRNY_Creation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MG_JRNY_Details`
--

DROP TABLE IF EXISTS `MG_JRNY_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `MG_JRNY_Details` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `journeyID` varchar(30) NOT NULL,
  `journeyDATE` date NOT NULL,
  `Emotion_tag` varchar(30) NOT NULL,
  `userupload` varchar(100) DEFAULT NULL,
  `Activity` varchar(40) NOT NULL,
  `Others` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MG_JRNY_Details`
--

LOCK TABLES `MG_JRNY_Details` WRITE;
/*!40000 ALTER TABLE `MG_JRNY_Details` DISABLE KEYS */;
INSERT INTO `MG_JRNY_Details` VALUES (4,'J1_1562394494','2019-07-19','help','C:\\fakepath\\20170115_092451.jpg','what an idea ','playing'),(5,'J1_1562394494','2019-07-19','advice','C:\\fakepath\\20170115_092615.jpg','take care','confused'),(6,'J1_1562394494','2019-07-17','bored','C:\\fakepath\\20170115_092615.jpg','sleeping','playing');
/*!40000 ALTER TABLE `MG_JRNY_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MG_JRNY_Operations`
--

DROP TABLE IF EXISTS `MG_JRNY_Operations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `MG_JRNY_Operations` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `journeyID` varchar(30) NOT NULL,
  `Emotion_tag` varchar(30) NOT NULL,
  `userupload_location` varchar(100) DEFAULT NULL,
  `emotiontag_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `journeytimestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MG_JRNY_Operations`
--

LOCK TABLES `MG_JRNY_Operations` WRITE;
/*!40000 ALTER TABLE `MG_JRNY_Operations` DISABLE KEYS */;
INSERT INTO `MG_JRNY_Operations` VALUES (1,'J1_1562394494','stress',NULL,'2019-07-08 07:30:08','2019-07-08 07:30:08'),(2,'J1_1562394494','Help',NULL,'2019-07-08 07:30:38','2019-07-08 07:30:38'),(3,'J1_1562394494','turnAround',NULL,'2019-07-08 07:30:53','2019-07-08 07:30:53'),(5,'J1_1562394494','Advice',NULL,'2019-07-08 07:40:22','2019-07-08 07:40:22'),(6,'J1_1562394494','turnAround',NULL,'2019-07-08 07:52:05','2019-07-08 07:52:05'),(7,'J1_1562580292','Help',NULL,'2019-07-08 10:06:17','2019-07-08 10:06:17');
/*!40000 ALTER TABLE `MG_JRNY_Operations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MG_JRNY_Requests`
--

DROP TABLE IF EXISTS `MG_JRNY_Requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `MG_JRNY_Requests` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `journeyID` varchar(30) NOT NULL,
  `Guest_Email` varchar(30) NOT NULL,
  `Emotion_tag` varchar(30) NOT NULL,
  `Emotion_tag_value` varchar(30) NOT NULL,
  `journeytimestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MG_JRNY_Requests`
--

LOCK TABLES `MG_JRNY_Requests` WRITE;
/*!40000 ALTER TABLE `MG_JRNY_Requests` DISABLE KEYS */;
INSERT INTO `MG_JRNY_Requests` VALUES (1,'J1_1562394494','puttasachin6@gmail.com','help','errror','2019-07-10 09:38:17'),(2,'J1_1562394494','puttasachin6@gmail.com','advice','take rest','2019-07-10 09:40:07'),(3,'J1_1562580292','puttasachin6@gmail.com','help','take rest','2019-07-10 09:41:24'),(7,'J1_1562394494','puttasachin6@gmail.com','stress','bottom break','2019-07-10 11:14:39'),(9,'J1_1562394494','puttasachin6@gmail.com','help','be carefull','2019-07-10 11:43:24'),(10,'J1_1562394494','sachin@gmail.com','advice','drink water','2019-07-10 11:55:04'),(11,'J1_1562394494','sachin@gmail.com','stress','play','2019-07-10 11:56:23'),(12,'J1_1562580292','rahul@gmail.com','help','switch mood','2019-07-11 10:13:48'),(18,'J1_1562394494','ravi@gmail.com','advice','writing','2019-07-14 08:40:34'),(19,'J1_1562394494','ian@gmail.com','help','sleep','2019-07-15 07:51:48'),(20,'J1_1562394494','ian@gmail.com','help','meditate','2019-10-15 14:31:17'),(21,'J1_1562394494','ian@gmail.com','help','yoga','2019-10-15 14:31:35');
/*!40000 ALTER TABLE `MG_JRNY_Requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MG_User_Creation`
--

DROP TABLE IF EXISTS `MG_User_Creation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `MG_User_Creation` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `UserEmail` varchar(30) NOT NULL,
  `usertimestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MG_User_Creation`
--

LOCK TABLES `MG_User_Creation` WRITE;
/*!40000 ALTER TABLE `MG_User_Creation` DISABLE KEYS */;
INSERT INTO `MG_User_Creation` VALUES (3,'puttasachin6@gmail.com','2019-07-05 12:08:57'),(7,'ced15i018@iiitdm.ac.in','2019-07-05 13:04:03'),(9,'arjunputta12@gmail.com','2019-07-08 15:33:28'),(12,'sachin6@gmail.com','2019-07-13 11:45:46'),(13,'abcd@gmail.com','2019-08-13 11:18:39'),(14,'doctoravatar@yahoo.com','2019-08-13 11:35:04'),(15,'sachinputta@gmail.com','2019-08-13 13:29:18'),(16,'sachinlovedany@gmail.com','2019-08-13 13:29:51'),(17,'Sachinbiryani.com','2019-08-13 13:30:26'),(18,'+919908280443','2019-08-13 13:48:35'),(19,'abcd@gmail.com ','2019-08-13 15:32:21'),(20,'hjg@gmail.com','2019-10-15 19:43:22');
/*!40000 ALTER TABLE `MG_User_Creation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-15 20:46:30
