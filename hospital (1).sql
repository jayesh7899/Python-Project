-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2022 at 09:44 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `AppId` varchar(20) NOT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(20) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Age` varchar(20) DEFAULT NULL,
  `Weight` varchar(20) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `Disease` varchar(20) DEFAULT NULL,
  `DrName` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`AppId`, `Date`, `Name`, `Address`, `Gender`, `Age`, `Weight`, `Mobile`, `Disease`, `DrName`) VALUES
('1', '2-3-2021', 'TUSHAR MALI', 'CHALISGAO', 'Male', '21', '68', '9999995757', 'GG', 'Dr.Prashant Mahajan'),
('2', '18-3-2021', 'CHANDAN BHOSALE', 'PUNE', 'Male', '32', '57', '9979797997', 'JJU', 'Dr.Bhaghwat Mahajan'),
('3', '7-8-2021', 'VINIT MAHALE', 'JANAKI NAGAR', 'Male', '23', '45', '994744666633', 'FEVAR', 'Dr.Bhaghwat Mahajan'),
('4', '5-9-2020', 'KOMAL PATIL', 'SADOBA NAGAR', 'Male', '24', '46', '90877765554', 'KKK', 'Dr.Bhaghwat Mahajan');

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `Pid` varchar(20) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Mobile` varchar(20) NOT NULL,
  `Disease` varchar(20) NOT NULL,
  `Room` varchar(20) NOT NULL,
  `Charge` varchar(20) NOT NULL,
  `Noofdays` varchar(20) NOT NULL,
  `Deposite` varchar(20) NOT NULL,
  `Payamount` varchar(20) NOT NULL,
  `Totalamount` varchar(20) NOT NULL,
  `Dept` varchar(20) NOT NULL,
  `Policyno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`Pid`, `Date`, `Name`, `Mobile`, `Disease`, `Room`, `Charge`, `Noofdays`, `Deposite`, `Payamount`, `Totalamount`, `Dept`, `Policyno`) VALUES
('1', '2-3-2021', 'TUSHAR PAWAR', '9999995757', 'GG', 'Special', '1000', '6', '5000', '1000', '1000', 'PRIVATE', '7778888292'),
('2', '18-3-2021', 'CHANDAN BHOSALE', '9979797997', 'JJU', 'Special', '1500', '3', '4000', '500', '500', 'Private', '123456788890');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `Did` varchar(20) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(20) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `Experience` varchar(20) DEFAULT NULL,
  `Qualification` varchar(20) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Salary` varchar(20) DEFAULT NULL,
  `Specilization` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`Did`, `Date`, `Name`, `Address`, `Mobile`, `Experience`, `Qualification`, `Gender`, `Salary`, `Specilization`) VALUES
('1', '66', 'gg', 'gg', '8888888888', '77', 'Male', 'Female', '78', 'Male'),
('2', '77', 'hh', 'hjj', '9000000000', '2 hh', 'Male', 'Male', '77', 'Male'),
('3', '66', 'yyy', 'hh', '9999999999', '22', 'Male', 'Male', '67', 'Male'),
('4', '5-SEP', 'LOKESH MAHAJAN', 'JANAKI NAGAR', '9768556889', '2', 'Male', 'Male', '34444', 'Male'),
('5', '2-3-2021', 'BHAVESH PATIL', 'KALYAN', '8999595959', '3 ', 'MBBS', 'Male', '23000', 'KKK');

-- --------------------------------------------------------

--
-- Table structure for table `genaral`
--

CREATE TABLE `genaral` (
  `Genid` varchar(20) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Room` varchar(20) NOT NULL,
  `Bed` varchar(20) NOT NULL,
  `Rate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `genaral`
--

INSERT INTO `genaral` (`Genid`, `Date`, `Room`, `Bed`, `Rate`) VALUES
('1', '22-1-2022', '10', '14', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `icu`
--

CREATE TABLE `icu` (
  `Icuid` varchar(20) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Room` varchar(20) NOT NULL,
  `Bed` varchar(20) NOT NULL,
  `Rate` varchar(20) NOT NULL,
  `Oxycharge` varchar(20) NOT NULL,
  `Ventilator` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `icu`
--

INSERT INTO `icu` (`Icuid`, `Date`, `Room`, `Bed`, `Rate`, `Oxycharge`, `Ventilator`) VALUES
('1', '19-9-2021', '15', '10', '4000', '2000', '3000');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `Pid` varchar(20) DEFAULT NULL,
  `Blood` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `Age` varchar(20) DEFAULT NULL,
  `Disease` varchar(20) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`Pid`, `Blood`, `Name`, `Address`, `Mobile`, `Age`, `Disease`, `Gender`) VALUES
('2', 'A', 'PARESH MALI', 'JANKI NAGAR', '9988888885', '24', 'ALLAGY', 'Male'),
('3', 'A', 'LOAKESH PATIL', 'JANAKI NAGAR JALGAON', '8999615924', '23', 'ALLARGY', 'Male'),
('4', 'A PSITIVE', 'LOKESH PATIL', 'MUMBAI', '68888797997', '23', 'COVID 19', 'Male'),
('5', 'B POSIVIVE', 'KALPESH MALI', 'PUNE', '4868979005', '25', 'D', 'Male'),
('6', 'A positive', 'payal rajaput', 'khadakpada', '89688677775', '25', 'iahdhh', 'Female');

-- --------------------------------------------------------

--
-- Table structure for table `patientadmit`
--

CREATE TABLE `patientadmit` (
  `AdmitId` varchar(20) NOT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(20) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Disease` varchar(20) DEFAULT NULL,
  `DrName` varchar(20) DEFAULT NULL,
  `Room` varchar(20) DEFAULT NULL,
  `Charge` varchar(20) DEFAULT NULL,
  `Damount` varchar(20) DEFAULT NULL,
  `Dept` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patientadmit`
--

INSERT INTO `patientadmit` (`AdmitId`, `Date`, `Name`, `Address`, `Mobile`, `Gender`, `Disease`, `DrName`, `Room`, `Charge`, `Damount`, `Dept`) VALUES
('1', '2-3-2021', 'TUSHAR MALI', 'CHALISGAO', '9999995757', 'Male', 'GG', 'Dr.Prashant Mahajan', 'Genaral', '1000', '1500', 'Private'),
('2', '18-3-2021', 'CHANDAN BHOSALE', 'PUNE', '9979797997', 'Male', 'JJU', 'Dr.Bhaghwat Mahajan', 'Special', '1500', '4000', 'Private'),
('3', '7-8-2021', 'VINIT MAHALE', 'JANAKI NAGAR', '994744666633', 'Male', 'FEVAR', 'Dr.Bhaghwat Mahajan', 'Special', '1500', '4000', 'Private');

-- --------------------------------------------------------

--
-- Table structure for table `special`
--

CREATE TABLE `special` (
  `speid` varchar(20) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Room` varchar(20) NOT NULL,
  `Bed` varchar(20) NOT NULL,
  `Rate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `special`
--

INSERT INTO `special` (`speid`, `Date`, `Room`, `Bed`, `Rate`) VALUES
('1', '8-3-2021', '10', '7', '1500');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `Sid` varchar(20) NOT NULL,
  `DOJ` varchar(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Address` varchar(20) NOT NULL,
  `Mobile` varchar(20) NOT NULL,
  `Exp` varchar(20) NOT NULL,
  `Qualification` varchar(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Salary` varchar(20) NOT NULL,
  `Age` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`Sid`, `DOJ`, `Name`, `Address`, `Mobile`, `Exp`, `Qualification`, `Gender`, `Salary`, `Age`) VALUES
('1', '2-7-2021', 'MAYUR LOHAR', 'JOSHI PETH', '8999999994', '4 ', 'BSC', 'Male', '13000', '25'),
('2', '9-3-2021', 'KAJAL MAHAJAN', 'JALGAON', '9969699600', '2', 'BSC', 'Female', '10000', '21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`AppId`);

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`Pid`);

--
-- Indexes for table `patientadmit`
--
ALTER TABLE `patientadmit`
  ADD PRIMARY KEY (`AdmitId`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`Sid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
