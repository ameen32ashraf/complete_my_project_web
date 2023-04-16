/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - complete_my-project
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
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

insert  into `attendence`(`attendence_id`,`date`,`group_member_id`,`status`,`external_lid`) values 
(1,'2023-03-26',1,'Present',5),
(2,'2023-03-26',1,'Present',5),
(3,'2023-03-26',1,'Present',5);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `chat` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`chat`,`date`) values 
(1,2,5,'hai','2023-03-26'),
(2,5,2,'hello','2023-03-26');

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
(1,1,'successfull','2023-03-26',5);

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
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `external_group_allocation` */

insert  into `external_group_allocation`(`eg_id`,`group_id`,`external_lid`,`status`,`date`,`internal_lid`) values 
(1,7,5,'Allocated','2023-03-24',2),
(2,8,6,'Allocated','2023-03-24',3),
(3,7,5,'Allocated','2023-03-26',2),
(4,12,6,'Allocated','2023-03-26',4);

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
  `ac_status` varchar(50) DEFAULT 'pending',
  PRIMARY KEY (`external_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `external_organization` */

insert  into `external_organization`(`external_id`,`company_name`,`phoneno`,`place`,`email`,`post`,`pin`,`license_no`,`lid`,`logo`,`ac_status`) values 
(1,'riss','9876543322','kozhikode','Risstechnologies@gmail.com','kozhikode','673517','lic12',5,'/static/external_org/20230324-163444.jpg','approved'),
(2,'bluegen','9544928881','kozhikode','bluegen@gmail.com','kozhikode','673517','lic32',6,'/static/external_org/20230324-163552.jpg','approved'),
(3,'region','9876543322','trissur','region@gmail.com','trissur','673517','lic 101',9,'/static/external_org/20230326-132302.jpg','approved'),
(4,'softtechnolgy','9544928881','kannur','softtechnology@gmail.com','kannur','673517','lic 234',10,'/static/external_org/20230326-133645.jpg','Rejected');

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `fileid` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `tittle` varchar(100) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fileid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `files` */

insert  into `files`(`fileid`,`group_id`,`tittle`,`filename`,`date`) values 
(1,1,'cmp','/static/files/20230326-084423.pdf','2023-03-26');

/*Table structure for table `group` */

DROP TABLE IF EXISTS `group`;

CREATE TABLE `group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(100) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  `group_lid` int(100) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `group` */

insert  into `group`(`group_id`,`group_name`,`year`,`group_lid`) values 
(1,'grp1','2023',7),
(2,'grp2','2023',8),
(4,'Group C','2023',12);

/*Table structure for table `group_allocation` */

DROP TABLE IF EXISTS `group_allocation`;

CREATE TABLE `group_allocation` (
  `allocation_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `internal_lid` int(11) DEFAULT NULL,
  `allocated_date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`allocation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `group_allocation` */

insert  into `group_allocation`(`allocation_id`,`group_id`,`internal_lid`,`allocated_date`,`status`) values 
(1,1,2,'2023-03-24','Allocated'),
(2,2,3,'2023-03-24','Allocated'),
(3,7,2,'2023-03-26','Allocated'),
(4,8,3,'2023-03-26','Allocated'),
(7,12,4,'2023-03-26','Allocated');

/*Table structure for table `group_member` */

DROP TABLE IF EXISTS `group_member`;

CREATE TABLE `group_member` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `student_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `group_member` */

insert  into `group_member`(`member_id`,`group_id`,`student_lid`) values 
(1,7,1),
(2,8,2),
(4,12,3);

/*Table structure for table `group_topic` */

DROP TABLE IF EXISTS `group_topic`;

CREATE TABLE `group_topic` (
  `grp_topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `topic_name` varchar(100) DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `date_of_upload` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`grp_topic_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `group_topic` */

insert  into `group_topic`(`grp_topic_id`,`group_id`,`topic_name`,`file`,`date_of_upload`,`status`) values 
(1,7,'topic','//static//topic//20230326-085459.jpg','2023-03-26','Rejected'),
(2,7,'topic','/static/topic/20230326-095034.pdf','2023-03-26','pending'),
(3,7,'topic','/static/topic/20230326-095045.pdf','2023-03-26','Approved'),
(4,7,'topic','/static/topic/20230326-095138.pdf','2023-03-26','pending'),
(5,7,'topic ','/static/topic/20230326-095807.pdf','2023-03-26','pending'),
(6,7,'mybusss','/static/topic/20230326-100522.pdf','2023-03-26','pending'),
(7,7,'mybusss','/static/topic/20230326-100540.pdf','2023-03-26','pending');

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
(1,'hemalatha V','hemalathaV@gmail.com','9544928881','ed','1987-05-21','Female','/static/internal_guide/20230324-163103.jpg',2),
(2,'Lubna P H','lubnaph@gmail.com','9544928881','changarakulam','1987-09-12','Female','/static/internal_guide/20230324-163214.jpg',3),
(3,'midhula','midhula@gmail.com','9876543321','pattambi','1981-08-30','Female','/static/internal_guide/20230324-163322.jpg',4);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'hemalathaV@gmail.com','4997','internal_guide'),
(3,'lubnaph@gmail.com','1284','internal_guide'),
(4,'midhula@gmail.com','4001','internal_guide'),
(5,'Risstechnologies@gmail.com','riss','external_organization'),
(6,'bluegen@gmail.com','blue','external_organization'),
(7,'grp1','3231','group'),
(8,'grp2','845','group'),
(9,'region@gmail.com','region','external_organization'),
(10,'softtechnology@gmail.com','soft','Rejected'),
(11,'grp 4','0','group'),
(12,'Group C','9967','group');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `mark` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`mark_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

insert  into `mark`(`mark_id`,`student_id`,`mark`,`date`) values 
(1,1,'20','2023-03-26');

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
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `progress` */

insert  into `progress`(`progress_id`,`progress_status`,`group_id`,`duration`,`date`,`file_name`) values 
(1,'not suuccsfull','7','22','0000-00-00','staticprogress20230326-084120.jpg'),
(2,'not suuccsfull','7','22','0000-00-00','staticprogress20230326-084124.jpg'),
(3,'not suuccsfull','7','22','0000-00-00','staticprogress20230326-084124.jpg'),
(4,'not suuccsfull','7','22','0000-00-00','staticprogress20230326-084129.jpg'),
(5,'not suuccsfull','7','22','0000-00-00','staticprogress20230326-084138.jpg'),
(6,'not successfull','7','22','0000-00-00','staticprogress20230326-102420.jpg');

/*Table structure for table `project_schedule` */

DROP TABLE IF EXISTS `project_schedule`;

CREATE TABLE `project_schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `tittle` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `project_schedule` */

insert  into `project_schedule`(`schedule_id`,`description`,`date`,`tittle`) values 
(1,'n bvfhffd','2023-03-12','ghfgmbghf');

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
(1,'Shebil A','shebil003@gmail.com','9645213833','malapuram','malapuram','676561','Kasargod','Male','2003-05-17','/static/student/20230324-163717.jpg'),
(2,'jishal','jishalmohammed555@gmail.com','7592891999','malapuram','malapuram','676561','Kasargod','Male','2002-05-15','/static/student/20230326-104609.jpg'),
(3,'rinshad','rinshad01@gmailcom','9544928881','malapuram','malapuram','676561','Kasargod','Male','2002-04-22','/static/student/20230324-163910.jpg');

/*Table structure for table `videos` */

DROP TABLE IF EXISTS `videos`;

CREATE TABLE `videos` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `tittle` varchar(100) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `videos` */

insert  into `videos`(`video_id`,`group_id`,`tittle`,`filename`,`date`) values 
(2,7,'my buss','/static/videos/20230326-111111.mp4','2023-03-26');

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
