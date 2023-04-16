/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.7.36 : Database - complete_my-project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`complete_my-project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `complete_my-project`;

/*Table structure for table `attendence` */

DROP TABLE IF EXISTS `attendence`;

CREATE TABLE `attendence` (
  `attendence_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `group_member_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `external_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`attendence_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

insert  into `attendence`(`attendence_id`,`date`,`group_member_id`,`status`,`external_lid`) values 
(1,'2022-11-26',2,'Present',8),
(2,'2022-11-26',3,'Absent',8);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `chat` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`chat`,`date`) values 
(1,8,3,'haii','2022-11-26'),
(2,8,2,'hello','2022-11-26'),
(3,2,8,'haii','2022-11-26');

/*Table structure for table `daily_works` */

DROP TABLE IF EXISTS `daily_works`;

CREATE TABLE `daily_works` (
  `daily_work_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `workinfo` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `external_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`daily_work_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `daily_works` */

insert  into `daily_works`(`daily_work_id`,`group_id`,`workinfo`,`date`,`external_lid`) values 
(1,15,'bskzgbck gkzhb','2022-11-26',8);

/*Table structure for table `external_group_allocation` */

DROP TABLE IF EXISTS `external_group_allocation`;

CREATE TABLE `external_group_allocation` (
  `eg_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `external_lid` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `internal_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`eg_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `external_group_allocation` */

insert  into `external_group_allocation`(`eg_id`,`group_id`,`external_lid`,`status`,`date`,`internal_lid`) values 
(2,15,8,'Allocated','2022-11-26',2);

/*Table structure for table `external_organization` */

DROP TABLE IF EXISTS `external_organization`;

CREATE TABLE `external_organization` (
  `external_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) DEFAULT NULL,
  `phoneno` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `license_no` varchar(100) DEFAULT NULL,
  `lid` int(100) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`external_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `external_organization` */

insert  into `external_organization`(`external_id`,`company_name`,`phoneno`,`place`,`email`,`post`,`pin`,`license_no`,`lid`,`logo`) values 
(2,'Maxlore ','8967850237','Calicat Cyberpark','maxloretech@gmail.com','calicat','678756','1234566',5,NULL),
(4,'Riss ','8967924610','Calicat','risstch@gmail.com','Calicat','670786','5435847986887267931',8,'/static/external_org/20221125-165227.jpg');

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `fileid` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `tittle` varchar(100) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fileid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `files` */

insert  into `files`(`fileid`,`group_id`,`tittle`,`filename`,`date`) values 
(1,15,'Files','hgm','2022-11-22'),
(2,15,'Encryption','/static/files/20221126-170351.pdf','2022-11-26');

/*Table structure for table `group` */

DROP TABLE IF EXISTS `group`;

CREATE TABLE `group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(100) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `group` */

insert  into `group`(`group_id`,`group_name`,`year`) values 
(5,'dg','dfgd'),
(4,'decrypt','2022-23'),
(3,'Encryption','2022-23'),
(6,'lnsldnvz','2022-23'),
(7,'adf','reds'),
(8,'hjjca','2022-23'),
(9,'df','2022-23'),
(10,'we','2022-23'),
(11,'sgx','2022-23'),
(15,'Block chain','2022-23');

/*Table structure for table `group_allocation` */

DROP TABLE IF EXISTS `group_allocation`;

CREATE TABLE `group_allocation` (
  `allocation_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `internal_lid` int(11) DEFAULT NULL,
  `allocated_date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`allocation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `group_allocation` */

insert  into `group_allocation`(`allocation_id`,`group_id`,`internal_lid`,`allocated_date`,`status`) values 
(1,9,2,'2022-11-17','Allocated');

/*Table structure for table `group_member` */

DROP TABLE IF EXISTS `group_member`;

CREATE TABLE `group_member` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `student_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `group_member` */

insert  into `group_member`(`member_id`,`group_id`,`student_lid`) values 
(2,15,3),
(3,15,2);

/*Table structure for table `group_topic` */

DROP TABLE IF EXISTS `group_topic`;

CREATE TABLE `group_topic` (
  `grp_topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `topic_name` varchar(100) DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `date_of_upload` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`grp_topic_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `group_topic` */

insert  into `group_topic`(`grp_topic_id`,`group_id`,`topic_name`,`file`,`date_of_upload`,`status`) values 
(1,15,'Crowd Funding',NULL,'2022-11-22','Rejected');

/*Table structure for table `internal_guide` */

DROP TABLE IF EXISTS `internal_guide`;

CREATE TABLE `internal_guide` (
  `internal_guide_id` int(11) NOT NULL AUTO_INCREMENT,
  `internal_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phoneno` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `lid` int(100) DEFAULT NULL,
  PRIMARY KEY (`internal_guide_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `internal_guide` */

insert  into `internal_guide`(`internal_guide_id`,`internal_name`,`email`,`phoneno`,`place`,`dob`,`gender`,`photo`,`lid`) values 
(1,'Abhinav','abced@gmailcom','6758273672','kannur','14/07/1993','Male','/static/internal_guide/20221117-111505.jpg',2),
(2,'Akharsh ','abced@gmailcom','6758273672','knnur','14/07/1993','Male','/static/internal_guide/20221117-111505.jpg',3),
(3,'yfytafvbjVCHJv1123','amal@gmail.com','7046821827','Ayippuzha','2022-11-20','Male','/static/internal_guide/20221117-111505.jpg',6);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'abced@gmailcom','7952','internal_guide'),
(3,'abcedf@gmailcom','587','internal_guide'),
(4,'risstrch@gmail.com','870','external_organization'),
(5,'maxloretech@gmail.com','3347','external_organization'),
(6,'amal@gmail.com','1638','internal_guide'),
(7,'risstrch@gmail.com','7910','external_organization'),
(8,'risstch@gmail.com','3178','external_organization'),
(9,'b','b','group');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `mark` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`mark_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

/*Table structure for table `progress` */

DROP TABLE IF EXISTS `progress`;

CREATE TABLE `progress` (
  `progress_id` int(11) NOT NULL AUTO_INCREMENT,
  `progress_status` varchar(100) DEFAULT NULL,
  `group_id` varchar(100) DEFAULT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `file_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`progress_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `progress` */

insert  into `progress`(`progress_id`,`progress_status`,`group_id`,`duration`,`date`,`file_name`) values 
(1,'Admin module Complete','15','5 day','2022-11-14','/static/internal_guide/20221117-111159.jpg');

/*Table structure for table `project_schedule` */

DROP TABLE IF EXISTS `project_schedule`;

CREATE TABLE `project_schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `tittle` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `project_schedule` */

insert  into `project_schedule`(`schedule_id`,`description`,`date`,`tittle`) values 
(2,'khvbcBJ','2022-11-17','abcdefghijklmonpq');

/*Table structure for table `status_request` */

DROP TABLE IF EXISTS `status_request`;

CREATE TABLE `status_request` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `status_request` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phoneno` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`sname`,`email`,`phoneno`,`place`,`post`,`pin`,`district`,`gender`,`dob`,`photo`) values 
(2,'Amal Chandran P K','amal@gmail.com','9046821827','Ayippuzha','Ayippuzha','670593','Kannur','Male','2022-11-21','/static/student/20221117-124239.jpg'),
(3,'Vipin P','vipi@gmail.com','9867345246','Kalliad','Kalliad','670593','Kannur','Male','2022-11-03','/static/student/20221117-142523.jpg');

/*Table structure for table `videos` */

DROP TABLE IF EXISTS `videos`;

CREATE TABLE `videos` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `tittle` varchar(100) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `videos` */

/*Table structure for table `viva_schedule` */

DROP TABLE IF EXISTS `viva_schedule`;

CREATE TABLE `viva_schedule` (
  `viva_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`viva_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `viva_schedule` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
