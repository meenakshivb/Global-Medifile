-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 18, 2019 at 05:47 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medifile`
--

-- --------------------------------------------------------

--
-- Table structure for table `adddoc`
--

CREATE TABLE `adddoc` (
  `id` int(100) NOT NULL,
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
  `after_token` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adddoc`
--

INSERT INTO `adddoc` (`id`, `img_files`, `name`, `email`, `age`, `phone`, `qualification`, `department`, `spacialization`, `date`, `salary`, `designation`, `files`, `password`, `cnf_password`, `g_id`, `hos_id`, `hos_name`, `forenoon`, `fore_token`, `afternoon`, `after_token`) VALUES
(1, 'images_XFBvkBL.jpg', 'roy', 'roy@gmail.com', '24', '8089186044', 'md. california', 'cardiac department', 'md in cardiac science', '2019/10/04 10:25', '1000', 'doctor', 'None', 'roy', 'roy', '842575', '706597', 'Renai Medicity', '', 0, '', 0),
(2, 'Megha photo 40kb_eYW3qFX.jpg', 'Martin christy', 'meghatb@gmail.com', '23', '8089186044', 'skd', 'cardiac department', 'sdfnslk', '2019-10-10', '1111', 'doctor', 'None', 'aaa', 'aaa', '986737', '706597', 'Renai Medicity', '', 0, '', 0),
(3, 'Megha photo 40kb_J5Seq2y.jpg', 'neena', 'meghatb@gmail.com', '23', '8089186044', 'skd', 'cardiac department', 'sdfnslk', '2019-10-11', '1111', 'doctor', 'None', 'neena', 'neena', '314338', '706597', 'Renai Medicity', 'Forenoon', 0, 'None', 0),
(6, 'Megha photo 40kb_HHdlvqi.jpg', 'celina suman paul', 'meghatb@gmail.com', '23', '8089186044', 'skd', 'cardiac department', 'sdfnslk', '2019-10-10', '1111', 'doctor', 'None', 'celina', 'celina', '842104', '706597', 'Renai Medicity', 'Forenoon', 10, 'None', 0),
(7, '8173.jpg', 'Megha babu', 'meghatb@gmail.com', '24', '8089186044', 'Med from California', 'pediatric Department', 'pediatric diseases.', '2019-10-23', '1236458', 'doctor', 'None', 'aA111111', 'aA111111', '915187', '706597', 'Renai Medicity', 'Forenoon', 10, 'None', 0);

-- --------------------------------------------------------

--
-- Table structure for table `adddpt`
--

CREATE TABLE `adddpt` (
  `sl_no` int(11) NOT NULL,
  `dptname` varchar(100) NOT NULL,
  `dptid` varchar(20) NOT NULL,
  `dpthead` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `drlist` varchar(300) NOT NULL,
  `details` varchar(500) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `hos_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adddpt`
--

INSERT INTO `adddpt` (`sl_no`, `dptname`, `dptid`, `dpthead`, `phone`, `drlist`, `details`, `hos_id`, `hos_name`) VALUES
(1, 'cardiac department', '7477', 'roy', '8089186044', '8089186044', 'cardiac department', '706597', 'Renai Medicity'),
(2, 'pediatric Department', '9532', 'Sajitha Babu', '12424235', 'thomas joseph, manoharan, jaya', 'the department that deals with the diseases related with children.', '706597', 'Renai Medicity'),
(3, 'neurology department', '5149', 'tk babu', '8089186044', '', '', '706597', 'Renai Medicity');

-- --------------------------------------------------------

--
-- Table structure for table `addpat`
--

CREATE TABLE `addpat` (
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
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addpat`
--

INSERT INTO `addpat` (`img`, `name`, `email`, `age`, `gender`, `dob`, `phone`, `address`, `votersid`, `adharno`, `licno`, `blood`, `password`, `cnf_password`, `g_id`, `designation`) VALUES
('dsc0743-233x300_5o57TD0.jpg', 'Anna', 'meghatb@gmail.com', '1', 'Female', '2019/10/11', '8089186044', 'Thembadath House', '122435', '12423637', '23te34', 'A-', 'ann', 'anna', '759973', 'patient'),
('UK-Passport-4_ejulgTw.jpg', 'divya', 'meghatb@gmail.com', '23', 'Female', '2019-10-02', '8089186044', 'Karimbil house, Thaikkattukara po, aluva', '122435', '32153264', 'w21', 'B-', 'divya', 'divya', '885904', 'patient'),
('UK-Passport-4_NXSMFR5.jpg', 'meera', 'meeramadhu1009@gmail.com', '24', 'Female', '2019/10/25', '7025378566', 'Thembadath house', '122435', '124356475', 'w21', 'A+', 'meera', 'meera', '994351', 'patient'),
('passport-picture-asian-young-woman-260nw-1016732269_sUUGgM7.webp', 'megha', 'meghatb@gmail.com', '24', 'Female', '2019-10-02', '8089186044', 'Karimbil house, Thaikkattukara po, aluva', '1', '12', '22', 'A+', 'megha', 'megha', '955630', 'patient'),
('Megha photo 40kb_Dx1ooM4.jpg', 'Suman', 'meghatb@gmail.com', '24', 'Female', '2019-10-17', '8089186044', 'asdd', '', '1263513746236', '', 'B-', 'suman', 'suman', '387691', 'patient'),
('Megha photo 40kb_CK4jPop.jpg', 'Suman', 'meghatb@gmail.com', '23', 'Female', '2019-10-10', '8089186044', 'sdff', '', '23142642', '', 'B-', 'aaa', 'aaa', '772750', 'patient'),
('Megha photo 40kb_a4C6xIk.jpg', 'Suman', 'meghatb@gmail.com', '23', 'Female', '2019-10-10', '8089186044', 'sdff', '', '23142642', '', 'B-', 'aaa', 'aaa', '188737', 'patient'),
('gmail.png', 'wqhk', 'a@gmail.com', '12', 'Female', '2019-10-18', '63257', 'khd', 'dsfhfg', '384876', 'dhgfusb', 'A+', 'aA11111111', 'aA11111111', '552790', 'patient'),
('footer-logo.png', 'weq`', 'a@gmail.com', '12', 'Female', '2019-10-08', '354', 'erqw', 'dsfhfg', '43778', 'dagvd', 'A+', 'aA111111', 'aA111111', '934939', 'patient'),
('footer-logo_B7o2oxD.png', 'wqhk', 'a@gmail.com', '12', 'Female', '2019-10-25', '12422', 'khd', 'dsfhfg', '124141', '', 'A-', 'aA111111', 'aA111111', '324481', 'patient'),
('dsc0743-233x300_EeT49MA.jpg', 'Adam ', 'meghatb@gmail.com', '2', 'Male', '2019-10-18', '8089186044', 'Thembadath House, padmamadom, qtr, Thaikkattukara. p.o, Ambattukavu, Aluva-683106', 'wfeytqf', '1246158', 'sjdgk', 'A+', 'aA111111', 'aA111111', '258145', 'patient');

-- --------------------------------------------------------

--
-- Table structure for table `addstaff`
--

CREATE TABLE `addstaff` (
  `id` int(100) NOT NULL,
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
  `hos_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addstaff`
--

INSERT INTO `addstaff` (`id`, `img_files`, `name`, `email`, `age`, `phone`, `department`, `date`, `designation`, `salary`, `files`, `password`, `cnf_password`, `g_id`, `hos_id`, `hos_name`) VALUES
(1, 'Megha photo 40kb_FYPSyWG.jpg', 'tenina', 'meghatb@gmail.com', '23', '8089186044', 'cardiac department', '2019-10-30', 'staff', '1111', 'None', 'aaa', 'aaa', '951322', '706597', 'Renai Medicity'),
(2, 'kissclipart-icon-male-clipart-computer-icons-clip-art-90e68d248346ebef.png', 'divya ', 'meghatb@gmail.com', '12', '8089186044', 'cardiac department', '2019-10-24', 'staff', '10000', 'None', 'aA111111', 'aA111111', '634750', '706597', 'Renai Medicity');

-- --------------------------------------------------------

--
-- Table structure for table `dr_leave`
--

CREATE TABLE `dr_leave` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `dr_id` varchar(100) NOT NULL,
  `leave` varchar(50) NOT NULL,
  `date_from` varchar(100) NOT NULL,
  `date_to` varchar(100) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dr_leave`
--

INSERT INTO `dr_leave` (`id`, `name`, `dr_id`, `leave`, `date_from`, `date_to`, `subject`, `reason`, `hos_id`, `status`) VALUES
(4, 'roy', '842575', 'one', '2019-10-30', 'None', 'Feaver', 'vsmhzgvw', '706597', 'Approved'),
(5, 'roy', '842575', 'one', '2019-10-16', 'None', 'Feaver', 'snkasdbws', '706597', 'Approved'),
(6, 'roy', '842575', 'one', '2019-12-01', 'None', 'Feaversa', 'sd,m', '706597', 'Approved'),
(7, 'roy', '842575', 'multiple', '2019-10-11', '2019-10-14', 'Family get together', 'dear sir I have a family get together in the above mentioned dates. i request  you to grant me the leave', '706597', ''),
(8, 'roy', '842575', 'multiple', '2019-10-11', '2019-10-14', 'Family get together', 'dear sir I have a family get together in the above mentioned dates. i request  you to grant me the leave', '706597', ''),
(9, 'roy', '842575', 'multiple', '2019-10-11', '2019-10-14', 'Family get together', 'dear sir I have a family get together in the above mentioned dates. i request  you to grant me the leave', '706597', '');

-- --------------------------------------------------------

--
-- Table structure for table `dr_prescribe`
--

CREATE TABLE `dr_prescribe` (
  `presc_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `pt_id` varchar(100) NOT NULL,
  `date_from` varchar(100) NOT NULL,
  `disease` varchar(200) NOT NULL,
  `status` varchar(500) NOT NULL,
  `med1` varchar(100) NOT NULL,
  `day1` varchar(20) NOT NULL,
  `test` varchar(500) NOT NULL,
  `dr_id` varchar(100) NOT NULL,
  `hos_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dr_prescribe`
--

INSERT INTO `dr_prescribe` (`presc_id`, `name`, `pt_id`, `date_from`, `disease`, `status`, `med1`, `day1`, `test`, `dr_id`, `hos_id`) VALUES
(1, 'Suman', '387691', '2019-10-14', 'a', 'asfa', 'sdfs', '2', 'xsxgsfgsfh', '842575', '706597'),
(2, 'Suman', '387691', '2019-10-14', 'a', 'asfa', 'sdfs', '2', 'xsxgsfgsfh', '842575', '706597'),
(3, 'Suman', '387691', '2019-10-14', 'a', 'asfa', 'sdfs', '2', 'xsxgsfgsfh', '842575', '706597'),
(4, 'Suman', '387691', '2019-10-14', 'a', 'asfa', 'sdfs', '2', 'xsxgsfgsfh', '842575', '706597'),
(5, 'Suman', '387691', '2019-10-15', '', '', 'None', 'None', 'None', '842575', '706597'),
(17, 'Suman', '387691', '2019-10-15', 'dfasf', 'asdfa', 'None', 'None', 'asfd', '842575', '706597'),
(18, 'Suman', '387691', '2019-10-15', 'fsdf', 'sgsf', 'None', 'None', 'sfdgs', '842575', '706597'),
(20, 'Suman', '387691', '2019-10-15', 'Feaver', '100 degree selcius fever', 'None', 'None', 'ghdf', '842575', '706597'),
(22, 'Suman', '387691', '2019-10-15', 'fsdf', 'fsh', 'None', 'None', '', '842575', '706597'),
(23, 'meera', '994351', '2019-10-17', 'Feaver', '1101 degree', '', '', '', '842575', '706597');

-- --------------------------------------------------------

--
-- Table structure for table `dr_suggest`
--

CREATE TABLE `dr_suggest` (
  `name` varchar(100) NOT NULL,
  `dr_id` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(100) NOT NULL,
  `g_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `hos_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `g_id`, `name`, `password`, `designation`, `hos_id`) VALUES
(1, '706597', 'Renai Medicity', 'renai', 'hospital', 'NULL'),
(2, '759973', 'Anna', 'ann', 'patient', 'null'),
(3, '885904', 'divya', 'divya', 'patient', 'NULL'),
(4, '994351', 'meera', 'meera', 'patient', 'null'),
(5, '842575', 'roy', 'roy', 'doctor', '706597'),
(6, '642349', 'Aster', 'aster', 'hospital', 'NULL'),
(7, '955630', 'megha', 'megha', 'patient', 'NULL'),
(8, '533590', 'pvs', 'pvs', 'hospital', 'NULL'),
(9, '457093', 'aaa', 'aaa', 'hospital', 'NULL'),
(14, '144637', 'aster medicity', 'aster', 'hospital', 'NULL'),
(15, '387691', 'Suman', 'suman', 'patient', 'NULL'),
(17, '986737', 'Martin christy', 'aaa', 'doctor', '706597'),
(18, '951322', 'tenina', 'aaa', 'staff', '706597'),
(19, '314338', 'neena', 'neena', 'doctor', '706597'),
(20, '350344', 'aneeta joy', 'aneeta', 'doctor', '706597'),
(22, '842104', 'celina suman paul', 'celina', 'doctor', '706597'),
(23, '582304', 'PVS Memorial Hospital', 'pvs', 'hospital', 'NULL'),
(43, '890881', 'Karothkuzhi Hospital', 'kar', 'hospital', 'NULL'),
(47, '766249', 'Rajagiri Hospital', 'rajagiri', 'hospital', 'NULL'),
(48, '689104', 'aster medicity', 'aa', 'hospital', 'NULL'),
(49, '228292', 'Lissy Hospital', 'lissy', 'hospital', 'NULL'),
(50, '366763', 'Lissy Hospital', 'lissy', 'hospital', 'NULL'),
(51, '246781', 'aster medicity', 'aaaaa', 'hospital', 'NULL'),
(52, '463081', 'weq`', 'aA111111', 'hospital', 'NULL'),
(53, '552790', 'wqhk', 'aA11111111', 'patient', 'NULL'),
(54, '934939', 'weq`', 'aA111111', 'patient', 'NULL'),
(55, '324481', 'wqhk', 'aA111111', 'patient', 'NULL'),
(56, '634750', 'divya ', 'aA111111', 'staff', '706597'),
(57, '915187', 'Megha babu', 'aA111111', 'doctor', '706597'),
(58, '258145', 'Adam ', 'aA111111', 'patient', 'null');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `med_id` int(100) NOT NULL,
  `presc_id` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `forenoon` varchar(20) NOT NULL,
  `afternoon` varchar(20) NOT NULL,
  `timing` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`med_id`, `presc_id`, `name`, `forenoon`, `afternoon`, `timing`, `review`) VALUES
(1, '22', 'paracetamol 600 gm', 'None', 'Afternoon', '1-1-1', 'for 30 days'),
(2, '22', 'dolo', 'Forenoon', 'None', '1-1-1', ''),
(3, '22', 'dolo2142', 'None', 'Afternoon', '1-1-1', 'hjg');

-- --------------------------------------------------------

--
-- Table structure for table `pt_book`
--

CREATE TABLE `pt_book` (
  `id` int(100) NOT NULL,
  `curr_dt` datetime NOT NULL,
  `department` varchar(100) NOT NULL,
  `doctor_id` varchar(100) NOT NULL,
  `hospital_id` varchar(100) NOT NULL,
  `patient` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `patient_id` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `token` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pt_book`
--

INSERT INTO `pt_book` (`id`, `curr_dt`, `department`, `doctor_id`, `hospital_id`, `patient`, `date`, `name`, `patient_id`, `phone`, `token`) VALUES
(2, '2019-10-10 00:00:00', 'cardiac department', '842575', '706597', 'New Patient', '2019-10-18', 'meera', '994351', '8089186044', '1'),
(3, '2019-10-10 00:00:00', 'cardiac department', '842575', '706597', 'New Patient', '2019-10-21', 'meera', '994351', '8089186044', '1'),
(17, '2019-10-11 00:00:00', 'cardiac department', '842575', '706597', 'New Patient', '2019-10-19', 'meera', '994351', '8089186044', '1'),
(18, '2019-10-11 00:00:00', 'cardiac department', '842575', '706597', 'New Patient', '2019-10-12', 'meera', '994351', '8089186044', '1'),
(19, '2019-10-11 00:00:00', 'cardiac department', '842575', '706597', 'New Patient', '2019-10-18', 'Suman', '387691', '8089186044', '2');

-- --------------------------------------------------------

--
-- Table structure for table `pt_contact`
--

CREATE TABLE `pt_contact` (
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

INSERT INTO `pt_contact` (`name`, `id`, `email`, `phone`, `subject`, `message`, `designation`) VALUES
('Renai Medicity', '842575', 'meghatb@gmail.com', '8089186044', 'aaaa', 'aaaa', 'hospital');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `hos_id` int(50) NOT NULL,
  `address` varchar(300) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `site` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `cnf_password` varchar(20) NOT NULL,
  `g_id` int(100) NOT NULL,
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `hos_id`, `address`, `phone`, `site`, `password`, `cnf_password`, `g_id`, `designation`) VALUES
(1, 'Renai Medicity', 12334, 'Renai medicity, Palarivattam. ernakulam', '9074368129', 'meghatb@gmail.com', 'renai', 'renai', 706597, 'hospital'),
(2, 'Aster', 1234, 'Renai medicity, Palarivattam. ernakulam', '8089186044', 'meghatb@gmail.com', 'aster', 'aster', 642349, 'hospital'),
(3, 'pvs', 46656, 'Renai medicity, Palarivattam. ernakulam', '8089186044', 'meghatb@gmail.com', 'pvs', 'pvs', 533590, 'hospital'),
(4, 'aaa', 2214, 'asdd', '1234567788', 'nsoam@gmail.com', 'aaa', 'aaa', 556837, 'hospital'),
(12, 'aster medicity', 111, 'qwwf', '8089186044', 'meghatb@gmail.com', 'aster', 'aster', 144637, 'hospital'),
(13, 'PVS Memorial Hospital', 251346, 'PVS Memorial Hospital, Klaoor', '832872', 'meghatb@gmail.com', 'pvs', 'pvs', 582304, 'hospital'),
(33, 'Karothkuzhi Hospital', 148638, 'Karothkuzhi Hospital, aluva', '8089186044', 'meghatb@gmail.com', 'kar', 'kar', 890881, 'hospital'),
(37, 'Rajagiri Hospital', 632587, 'Rajagiri Hospital, Kalamasserry', '8089186044', 'meghatb@gmail.com', 'rajagiri', 'rajagiri', 766249, 'hospital'),
(38, 'aster medicity', 323, 'asdd', '8089186044', 'meghatb@gmail.com', 'aa', 'dwdq', 689104, 'hospital'),
(39, 'Lissy Hospital', 16481708, 'PVS Memorial Hospital, Klaoor', '124697', 'meghatb@gmail.com', 'lissy', 'lkjsd', 228292, 'hospital'),
(40, 'Lissy Hospital', 16481708, 'PVS Memorial Hospital, Klaoor', '124697', 'meghatb@gmail.com', 'lissy', 'lkjsd', 366763, 'hospital'),
(41, 'aster medicity', 24, 'asf', '8089186044', 'meghatb@gmail.com', 'aaaaa', 'aaaaa', 246781, 'hospital'),
(42, 'weq`', 234, 'ewr', '235', 'wew@gmail.com', 'aA111111', 'aA111111', 463081, 'hospital');

-- --------------------------------------------------------

--
-- Table structure for table `st_leave`
--

CREATE TABLE `st_leave` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `st_id` int(100) NOT NULL,
  `leave` varchar(100) NOT NULL,
  `date_from` varchar(100) NOT NULL,
  `date_to` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `reason` varchar(200) NOT NULL,
  `hos_id` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `test_id` int(100) NOT NULL,
  `presc_id` varchar(100) NOT NULL,
  `test` varchar(200) NOT NULL,
  `results` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`test_id`, `presc_id`, `test`, `results`) VALUES
(1, '22', 'Blood test', ''),
(2, '22', 'ESR test', ''),
(3, '22', 'Blood test', ''),
(4, '22', 'Blood test235346', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adddoc`
--
ALTER TABLE `adddoc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adddpt`
--
ALTER TABLE `adddpt`
  ADD PRIMARY KEY (`sl_no`);

--
-- Indexes for table `addstaff`
--
ALTER TABLE `addstaff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dr_leave`
--
ALTER TABLE `dr_leave`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dr_prescribe`
--
ALTER TABLE `dr_prescribe`
  ADD PRIMARY KEY (`presc_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`med_id`);

--
-- Indexes for table `pt_book`
--
ALTER TABLE `pt_book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `st_leave`
--
ALTER TABLE `st_leave`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`test_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adddoc`
--
ALTER TABLE `adddoc`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `adddpt`
--
ALTER TABLE `adddpt`
  MODIFY `sl_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `addstaff`
--
ALTER TABLE `addstaff`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `dr_leave`
--
ALTER TABLE `dr_leave`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `dr_prescribe`
--
ALTER TABLE `dr_prescribe`
  MODIFY `presc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `med_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pt_book`
--
ALTER TABLE `pt_book`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `st_leave`
--
ALTER TABLE `st_leave`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `test_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
