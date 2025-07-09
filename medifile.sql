-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 29, 2021 at 08:53 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `medifile`
--

-- --------------------------------------------------------

--
-- Table structure for table `adddoc`
--

CREATE TABLE IF NOT EXISTS `adddoc` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `img_files` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `age` varchar(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `qualification` varchar(300) NOT NULL,
  `department` varchar(100) NOT NULL,
  `spacialization` varchar(200) NOT NULL,
  `date` varchar(100) NOT NULL,
  `salary` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `files` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL,
  `cnf_password` varchar(100) NOT NULL,
  `g_id` varchar(100) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `hos_name` varchar(100) NOT NULL,
  `forenoon` varchar(50) NOT NULL,
  `fore_token` int(50) NOT NULL,
  `afternoon` varchar(50) NOT NULL,
  `after_token` int(50) NOT NULL,
  PRIMARY KEY (`id`,`g_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `adddoc`
--

INSERT INTO `adddoc` (`id`, `img_files`, `name`, `email`, `age`, `phone`, `qualification`, `department`, `spacialization`, `date`, `salary`, `designation`, `files`, `password`, `cnf_password`, `g_id`, `hos_id`, `hos_name`, `forenoon`, `fore_token`, `afternoon`, `after_token`) VALUES
(1, 'Megha T B_zbFliEz.jpg', 'roy mathew', 'meghatb@gmail.com', '56', '8089186044', 'Md. california', 'Cardiology', 'In cardiac Science', '2019-10-24', '100000', 'doctor', 'None', 'Roy10000', 'Roy10000', '910510', '429475', 'renai Medicity', 'Forenoon', 10, 'None', 0),
(2, 'Megha photo 40kb_9c1kUld.jpg', 'Teneena james', 'meghatb@gmail.com', '23', '8089186044', 'Md. california', 'Gynecology', 'aaa', '2019-10-25', '100000', 'doctor', 'None', 'Teneena1', 'Teneena1', '379411', '429475', 'renai Medicity', 'None', 0, 'Afternoon', 10),
(3, 'Megha T B edited.jpg', 'priya jose', 'meghatb@gmail.com', '24', '8089186044', 'Md. california', 'Pediatrics Department', 'In child Physical ', '2019-10-25', '100000', 'doctor', 'None', 'Priya100', 'Priya100', '883627', '429475', 'renai Medicity', 'Forenoon', 15, 'None', 0);

-- --------------------------------------------------------

--
-- Table structure for table `adddpt`
--

CREATE TABLE IF NOT EXISTS `adddpt` (
  `sl_no` int(11) NOT NULL AUTO_INCREMENT,
  `dptname` varchar(100) NOT NULL,
  `dptid` varchar(20) NOT NULL,
  `dpthead` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `drlist` varchar(300) NOT NULL,
  `details` varchar(500) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `hos_name` varchar(100) NOT NULL,
  PRIMARY KEY (`sl_no`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `adddpt`
--

INSERT INTO `adddpt` (`sl_no`, `dptname`, `dptid`, `dpthead`, `phone`, `drlist`, `details`, `hos_id`, `hos_name`) VALUES
(1, 'Cardiology', '1030', 'roy mathew', '8089186044', 'raj, thomas', 'Cardiology  is a branch of medicine that deals with the disorders of the heart as well as some parts of the circulatory system. The field includes medical diagnosis and treatment of congenital heart defects, coronary artery disease, heart failure, valvular heart disease and electrophysiology. Physicians who specialize in this field of medicine are called cardiologists, a specialty of internal medicine. Pediatric cardiologists are pediatricians who specialize in cardiology. Physicians who special', '429475', 'renai Medicity'),
(2, 'Pediatrics Department', '1189', 'Beneeta ', '8089186044', 'raj, aneeta', 'Pediatrics (also spelled paediatrics or pædiatrics) is the branch of medicine that involves the medical care of infants, children, and adolescents. The American Academy of Pediatrics recommends people be under pediatric care up to the age of 21,[1] thought usually only minors under 18 are required to be under pediatric care. A medical doctor who specializes in this area is known as a pediatrician, or paediatrician. The word pediatrics and its cognates mean "healer of children"; they derive from ', '429475', 'renai Medicity'),
(3, 'Gynecology', '2467', 'sumesh', '8089186044', 'Radha Madhav, rani', 'Investigates and treats problems relating to the female urinary tract and reproductive organs, such as Endometriosis, infertility and incontinence.', '429475', 'renai Medicity');

-- --------------------------------------------------------

--
-- Table structure for table `addpat`
--

CREATE TABLE IF NOT EXISTS `addpat` (
  `img` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `age` varchar(10) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` varchar(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `address` varchar(200) NOT NULL,
  `votersid` varchar(100) NOT NULL,
  `adharno` varchar(100) NOT NULL,
  `licno` varchar(100) NOT NULL,
  `blood` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `cnf_password` varchar(100) NOT NULL,
  `g_id` varchar(500) NOT NULL,
  `designation` varchar(100) NOT NULL,
  PRIMARY KEY (`g_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addpat`
--

INSERT INTO `addpat` (`img`, `name`, `email`, `age`, `gender`, `dob`, `phone`, `address`, `votersid`, `adharno`, `licno`, `blood`, `password`, `cnf_password`, `g_id`, `designation`) VALUES
('Megha photo 40kb_4ph6D1z.jpg', 'celina suman paul', 'meghatb@gmail.com', '25', 'Female', '2019-10-25', '8089186044', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '2423', '2384394593', '34923u', 'A+', 'Suman100', 'Suman100', '253825', 'patient'),
('Megha T B edited_cfZU9J1.jpg', 'Dilsha M Deleep', 'dilshamdeleep20@gmail.com', '23', 'Female', '1995-12-04', '8089186044', 'Thembadath House, thaikkattukara(p.o), Ambattukavu, Aluva\r\n', '33781329', '1223673839', '23633ry8', 'A+', 'Dilsha10', 'Dilsha10', '595228', 'patient'),
('Megha T B edited_CQ3LxXC.jpg', 'lakshmi', 'meghatb@gmail.com', '23', 'Female', '2019-10-02', '8089186044', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '33781329', '2356287', '23633ry8', 'A+', 'Lakshmi1', 'Lakshmi1', '631585', 'patient'),
('Megha T B crop_y9CV4Am.jpg', 'Aneeja', 'meghatb@gmail.com', '23', 'Female', '2019-10-29', '8089186044', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '33781329', '576345729', '34923u', 'A+', 'Aneeja10', 'Aneeja10', '885271', 'patient');

-- --------------------------------------------------------

--
-- Table structure for table `addstaff`
--

CREATE TABLE IF NOT EXISTS `addstaff` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `img_files` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `age` varchar(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `department` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `salary` varchar(100) NOT NULL,
  `files` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `cnf_password` varchar(100) NOT NULL,
  `g_id` varchar(100) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `hos_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `addstaff`
--

INSERT INTO `addstaff` (`id`, `img_files`, `name`, `email`, `age`, `phone`, `department`, `date`, `designation`, `salary`, `files`, `password`, `cnf_password`, `g_id`, `hos_id`, `hos_name`) VALUES
(1, 'Megha T B crop.jpg', 'Anu Joy', 'meghatb@gmail.com', '23', '8089186044', 'Gynecology', '2019-10-24', 'nurse', '10000', 'None', 'Anu10000', 'Anu10000', '210004', '429475', 'renai Medicity'),
(2, 'Megha T B_sfW5p6T.jpg', 'Meenu ', 'meghatb@gmail.com', '23', '8089186044', 'Cardiology', '2019-10-24', 'staff', '100000', 'None', 'Meenu100', 'Meenu100', '465376', '429475', 'renai Medicity');

-- --------------------------------------------------------

--
-- Table structure for table `dr_leave`
--

CREATE TABLE IF NOT EXISTS `dr_leave` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `dr_id` varchar(100) NOT NULL,
  `leave` varchar(50) NOT NULL,
  `date_from` varchar(100) NOT NULL,
  `date_to` varchar(100) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `dr_leave`
--


-- --------------------------------------------------------

--
-- Table structure for table `dr_prescribe`
--

CREATE TABLE IF NOT EXISTS `dr_prescribe` (
  `presc_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `pt_id` varchar(100) NOT NULL,
  `date_from` varchar(100) NOT NULL,
  `disease` varchar(200) NOT NULL,
  `status` varchar(500) NOT NULL,
  `med1` varchar(100) NOT NULL,
  `day1` varchar(20) NOT NULL,
  `test` varchar(500) NOT NULL,
  `dr_id` varchar(100) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  PRIMARY KEY (`presc_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `dr_prescribe`
--

INSERT INTO `dr_prescribe` (`presc_id`, `name`, `pt_id`, `date_from`, `disease`, `status`, `med1`, `day1`, `test`, `dr_id`, `hos_id`) VALUES
(1, 'Dilsha M Deleep', '595228', '2019-10-25', 'Feaver', '100 degree celcius', '', '', '', '910510', '429475');

-- --------------------------------------------------------

--
-- Table structure for table `dr_suggest`
--

CREATE TABLE IF NOT EXISTS `dr_suggest` (
  `name` varchar(100) NOT NULL,
  `dr_id` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dr_suggest`
--


-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `g_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `g_id`, `name`, `password`, `designation`, `hos_id`) VALUES
(3, '429475', 'renai Medicity', 'Renai100', 'hospital', 'NULL'),
(4, '607891', 'PVS Memmorial Hospital', 'Pvsmemmorial100', 'hospital', 'NULL'),
(5, '354265', 'aaa', 'Aaaaaa100', 'hospital', 'NULL'),
(6, '910510', 'roy mathew', 'Roy10000', 'doctor', '429475'),
(7, '379411', 'Teneena james', 'Teneena1', 'doctor', '429475'),
(8, '883627', 'priya jose', 'Priya100', 'doctor', '429475'),
(9, '210004', 'Anu Joy', 'Anu10000', 'nurse', '429475'),
(10, '465376', 'Meenu ', 'Meenu100', 'staff', '429475'),
(11, '595228', 'Dilsha M Deleep', 'Dilsha10', 'patient', 'null'),
(12, '253825', 'celina suman paul', 'Suman100', 'patient', 'NULL'),
(16, '885271', 'Aneeja', 'Aneeja10', 'patient', 'NULL'),
(17, '631585', 'lakshmi', 'Lakshmi1', 'patient', 'NULL');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE IF NOT EXISTS `medicine` (
  `med_id` int(100) NOT NULL AUTO_INCREMENT,
  `presc_id` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `forenoon` varchar(20) NOT NULL,
  `afternoon` varchar(20) NOT NULL,
  `timing` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  PRIMARY KEY (`med_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`med_id`, `presc_id`, `name`, `forenoon`, `afternoon`, `timing`, `review`) VALUES
(1, '1', 'Dolo 600 mg', 'Forenoon', 'Afternoon', '1-1-1', 'for 30 days');

-- --------------------------------------------------------

--
-- Table structure for table `pt_book`
--

CREATE TABLE IF NOT EXISTS `pt_book` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `curr_dt` datetime NOT NULL,
  `department` varchar(100) NOT NULL,
  `doctor_id` varchar(100) NOT NULL,
  `hospital_id` varchar(100) NOT NULL,
  `patient` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `patient_id` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `token` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `pt_book`
--

INSERT INTO `pt_book` (`id`, `curr_dt`, `department`, `doctor_id`, `hospital_id`, `patient`, `date`, `name`, `patient_id`, `phone`, `token`) VALUES
(1, '2019-10-25 00:00:00', 'Cardiology', '910510', '429475', 'New Patient', '2019-10-25', 'Dilsha M Deleep', '595228', '8089186044', '1'),
(2, '2019-10-25 00:00:00', 'Cardiology', '910510', '429475', 'Returning Patient', '2019-10-25', 'celina suman paul', '253825', '8089186044', '2'),
(3, '2019-10-26 00:00:00', 'Pediatrics Department', '883627', '429475', 'New Patient', '2019-10-27', 'Meenu ', '465376', '8089186044', '1');

-- --------------------------------------------------------

--
-- Table structure for table `pt_contact`
--

CREATE TABLE IF NOT EXISTS `pt_contact` (
  `name` varchar(100) NOT NULL,
  `id` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(500) NOT NULL,
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pt_contact`
--


-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE IF NOT EXISTS `register` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `hos_id` int(50) NOT NULL,
  `address` varchar(300) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `site` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `cnf_password` varchar(20) NOT NULL,
  `g_id` int(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `hos_id`, `address`, `phone`, `site`, `password`, `cnf_password`, `g_id`, `designation`) VALUES
(3, 'Renai Medicity', 276398, 'Post Box No. 2259, Mamangalam, Palarivattom. P O, Cochin, Kerala, India – 682 025', '8089186044', 'meghatb@gmail.com', 'Renai100', 'Renai100', 429475, 'hospital'),
(4, 'PVS Memmorial Hospital', 3894, 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'meghatb@gmail.com', 'Pvsmemmorial100', 'Pvsmemmorial100', 607891, 'hospital');

-- --------------------------------------------------------

--
-- Table structure for table `relative`
--

CREATE TABLE IF NOT EXISTS `relative` (
  `g_id` varchar(100) NOT NULL,
  `relative1` varchar(100) NOT NULL,
  `relation1` varchar(100) NOT NULL,
  `address1` varchar(200) NOT NULL,
  `phone1` varchar(100) NOT NULL,
  `relative2` varchar(100) NOT NULL,
  `relation2` varchar(100) NOT NULL,
  `address2` varchar(200) NOT NULL,
  `phone2` varchar(100) NOT NULL,
  `patient_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `relative`
--

INSERT INTO `relative` (`g_id`, `relative1`, `relation1`, `address1`, `phone1`, `relative2`, `relation2`, `address2`, `phone2`, `patient_name`) VALUES
('885271', 'anu', 'sister', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'ani', 'None', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'Aneeja'),
('631585', 'appu', 'sister', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'rani', 'None', 'Banerji Rd, Opp Gokulam park, Kaloor, Ernakulam, Kerala 682017', '8089186044', 'lakshmi');

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE IF NOT EXISTS `schedule` (
  `sunday` varchar(100) NOT NULL,
  `sf_time` varchar(100) NOT NULL,
  `sf_token` varchar(100) NOT NULL,
  `sa_time` varchar(100) NOT NULL,
  `sa_token` varchar(100) NOT NULL,
  `monday` varchar(100) NOT NULL,
  `mf_time` varchar(100) NOT NULL,
  `mf_token` varchar(100) NOT NULL,
  `ma_time` varchar(100) NOT NULL,
  `ma_token` varchar(100) NOT NULL,
  `tuesday` varchar(100) NOT NULL,
  `tf_time` int(11) NOT NULL,
  `tf_token` int(11) NOT NULL,
  `ta_time` int(11) NOT NULL,
  `ta_token` int(11) NOT NULL,
  `wednesday` int(11) NOT NULL,
  `wf_time` int(11) NOT NULL,
  `wf_token` int(11) NOT NULL,
  `wa_time` int(11) NOT NULL,
  `wa_token` int(11) NOT NULL,
  `thursday` int(11) NOT NULL,
  `thf_time` int(11) NOT NULL,
  `thf_token` int(11) NOT NULL,
  `tha_time` int(11) NOT NULL,
  `tha_token` int(11) NOT NULL,
  `friday` int(11) NOT NULL,
  `ff_time` int(11) NOT NULL,
  `ff_token` int(11) NOT NULL,
  `fa_time` int(11) NOT NULL,
  `fa_token` int(11) NOT NULL,
  `saturday` int(11) NOT NULL,
  `saf_time` int(11) NOT NULL,
  `saf_token` int(11) NOT NULL,
  `saa_time` int(11) NOT NULL,
  `saa_token` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `schedule`
--


-- --------------------------------------------------------

--
-- Table structure for table `st_leave`
--

CREATE TABLE IF NOT EXISTS `st_leave` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `st_id` int(100) NOT NULL,
  `leave` varchar(100) NOT NULL,
  `date_from` varchar(100) NOT NULL,
  `date_to` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `reason` varchar(200) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `st_leave`
--

INSERT INTO `st_leave` (`id`, `name`, `st_id`, `leave`, `date_from`, `date_to`, `subject`, `reason`, `hos_id`, `designation`, `status`) VALUES
(1, 'Meenu ', 465376, 'one', '2019-10-23', 'None', 'personal Matter', 'aaaaa', '429475', 'staff', 'Approved'),
(4, 'Meenu ', 465376, 'one', '2019-10-23', 'None', 'personal Matter', 'aaaaa', '429475', 'staff', 'Approved'),
(5, 'Meenu ', 465376, 'one', '2019-10-23', 'None', 'personal Matter', 'aaaaa', '429475', 'staff', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE IF NOT EXISTS `test` (
  `test_id` int(100) NOT NULL AUTO_INCREMENT,
  `presc_id` varchar(100) NOT NULL,
  `test` varchar(200) NOT NULL,
  `results` varchar(200) NOT NULL,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`test_id`, `presc_id`, `test`, `results`) VALUES
(1, '1', 'Blood Test', 'Simple_qKqHwpO.java'),
(2, '1', 'ESR Test', 'dbconnection_yMKRTky.java'),
(3, '1', 'Platelets Count', '');
