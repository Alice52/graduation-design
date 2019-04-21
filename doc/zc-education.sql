/*
Navicat MySQL Data Transfer

Source Server         : aliyun
Source Server Version : 50725
Source Host           : 101.132.45.28:3306
Source Database       : zc-education

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-04-20 15:25:27
*/

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for courses_courseinfo
-- ----------------------------
DROP TABLE IF EXISTS `courses_courseinfo`;
CREATE TABLE `courses_courseinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `name` varchar(20) NOT NULL,
  `study_time` int(11) NOT NULL,
  `study_num` int(11) NOT NULL,
  `level` varchar(5) NOT NULL,
  `love_num` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `detail` longtext NOT NULL,
  `category` varchar(5) NOT NULL,
  `course_notice` varchar(200) NOT NULL,
  `course_need` varchar(100) NOT NULL,
  `teacher_tell` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `orginfo_id` int(11) NOT NULL,
  `teacherinfo_id` int(11) NOT NULL,
  `is_banner` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_courseinfo_orginfo_id_3d3f29c6_fk_orgs_orginfo_id` (`orginfo_id`),
  KEY `courses_courseinf_teacherinfo_id_fc77d47e_fk_orgs_teacherinfo_id` (`teacherinfo_id`),
  CONSTRAINT `courses_courseinf_teacherinfo_id_fc77d47e_fk_orgs_teacherinfo_id` FOREIGN KEY (`teacherinfo_id`) REFERENCES `orgs_teacherinfo` (`id`),
  CONSTRAINT `courses_courseinfo_orginfo_id_3d3f29c6_fk_orgs_orginfo_id` FOREIGN KEY (`orginfo_id`) REFERENCES `orgs_orginfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for courses_lessoninfo
-- ----------------------------
DROP TABLE IF EXISTS `courses_lessoninfo`;
CREATE TABLE `courses_lessoninfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `courseinfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_lessonin_courseinfo_id_25919b0f_fk_courses_courseinfo_id` (`courseinfo_id`),
  CONSTRAINT `courses_lessonin_courseinfo_id_25919b0f_fk_courses_courseinfo_id` FOREIGN KEY (`courseinfo_id`) REFERENCES `courses_courseinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for courses_sourceinfo
-- ----------------------------
DROP TABLE IF EXISTS `courses_sourceinfo`;
CREATE TABLE `courses_sourceinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `down_load` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `courseinfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_sourcein_courseinfo_id_9d1b6a06_fk_courses_courseinfo_id` (`courseinfo_id`),
  CONSTRAINT `courses_sourcein_courseinfo_id_9d1b6a06_fk_courses_courseinfo_id` FOREIGN KEY (`courseinfo_id`) REFERENCES `courses_courseinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for courses_videoinfo
-- ----------------------------
DROP TABLE IF EXISTS `courses_videoinfo`;
CREATE TABLE `courses_videoinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `study_time` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `lessoninfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_videoinf_lessoninfo_id_02a97f3a_fk_courses_lessoninfo_id` (`lessoninfo_id`),
  CONSTRAINT `courses_videoinf_lessoninfo_id_02a97f3a_fk_courses_lessoninfo_id` FOREIGN KEY (`lessoninfo_id`) REFERENCES `courses_lessoninfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for operations_usercomment
-- ----------------------------
DROP TABLE IF EXISTS `operations_usercomment`;
CREATE TABLE `operations_usercomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_content` varchar(300) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `comment_course_id` int(11) NOT NULL,
  `comment_man_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operations_usercomment_ad012e59` (`comment_course_id`),
  KEY `operations_usercomment_5dfc3666` (`comment_man_id`),
  CONSTRAINT `operations_u_comment_course_id_39dc5cdf_fk_courses_courseinfo_id` FOREIGN KEY (`comment_course_id`) REFERENCES `courses_courseinfo` (`id`),
  CONSTRAINT `operations_userc_comment_man_id_c4c79f25_fk_users_userprofile_id` FOREIGN KEY (`comment_man_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for operations_usercourse
-- ----------------------------
DROP TABLE IF EXISTS `operations_usercourse`;
CREATE TABLE `operations_usercourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `study_course_id` int(11) NOT NULL,
  `study_man_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operations_usercourse_study_man_id_ca233d28_uniq` (`study_man_id`,`study_course_id`),
  KEY `operations_usercourse_2c9863aa` (`study_course_id`),
  KEY `operations_usercourse_b4cc9642` (`study_man_id`),
  CONSTRAINT `operations_use_study_course_id_ad6771e9_fk_courses_courseinfo_id` FOREIGN KEY (`study_course_id`) REFERENCES `courses_courseinfo` (`id`),
  CONSTRAINT `operations_usercou_study_man_id_a1251afb_fk_users_userprofile_id` FOREIGN KEY (`study_man_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for operations_userlove
-- ----------------------------
DROP TABLE IF EXISTS `operations_userlove`;
CREATE TABLE `operations_userlove` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `love_id` int(11) NOT NULL,
  `love_type` int(11) NOT NULL,
  `love_status` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `love_man_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operations_userlove_bf012eab` (`love_man_id`),
  CONSTRAINT `operations_userlove_love_man_id_7fb97ad4_fk_users_userprofile_id` FOREIGN KEY (`love_man_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for orgs_cityinfo
-- ----------------------------
DROP TABLE IF EXISTS `orgs_cityinfo`;
CREATE TABLE `orgs_cityinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for orgs_orginfo
-- ----------------------------
DROP TABLE IF EXISTS `orgs_orginfo`;
CREATE TABLE `orgs_orginfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `name` varchar(20) NOT NULL,
  `course_num` int(11) NOT NULL,
  `study_num` int(11) NOT NULL,
  `address` varchar(200) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `detail` longtext NOT NULL,
  `love_num` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `category` varchar(10) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `cityinfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_orginfo_cityinfo_id_b30bafbf_fk_orgs_cityinfo_id` (`cityinfo_id`),
  CONSTRAINT `orgs_orginfo_cityinfo_id_b30bafbf_fk_orgs_cityinfo_id` FOREIGN KEY (`cityinfo_id`) REFERENCES `orgs_cityinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for orgs_teacherinfo
-- ----------------------------
DROP TABLE IF EXISTS `orgs_teacherinfo`;
CREATE TABLE `orgs_teacherinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `name` varchar(20) NOT NULL,
  `work_year` int(11) NOT NULL,
  `work_position` varchar(20) NOT NULL,
  `work_style` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `love_num` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `work_company_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_teacherinfo_work_company_id_b897a136_fk_orgs_orginfo_id` (`work_company_id`),
  CONSTRAINT `orgs_teacherinfo_work_company_id_b897a136_fk_orgs_orginfo_id` FOREIGN KEY (`work_company_id`) REFERENCES `orgs_orginfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_bannerinfo
-- ----------------------------
DROP TABLE IF EXISTS `users_bannerinfo`;
CREATE TABLE `users_bannerinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_emailverifycode
-- ----------------------------
DROP TABLE IF EXISTS `users_emailverifycode`;
CREATE TABLE `users_emailverifycode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `email` varchar(200) NOT NULL,
  `send_type` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users_userprofile
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `image` varchar(200) DEFAULT NULL,
  `nick_name` varchar(20) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `add_time` datetime(6) NOT NULL,
  `is_start` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
