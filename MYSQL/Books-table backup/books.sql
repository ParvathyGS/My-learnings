-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 05, 2019 at 05:59 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.2.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `ID` int(11) NOT NULL,
  `BOOK_NAME` varchar(100) NOT NULL,
  `BOOK_TITLE` varchar(100) DEFAULT NULL,
  `AUTHOR_NAME` varchar(100) DEFAULT NULL,
  `AUTHOR_COUNTRY` varchar(100) DEFAULT NULL,
  `YEAR` int(11) DEFAULT NULL,
  `PRICE` float DEFAULT NULL
) ;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`ID`, `BOOK_NAME`, `BOOK_TITLE`, `AUTHOR_NAME`, `AUTHOR_COUNTRY`, `YEAR`, `PRICE`) VALUES
(100, 'ABCD', 'XYZ', 'HJIK', 'AUH', 2013, 500),
(101, 'ABCDEF', 'EXPENSIVE', 'HJIKLM', 'NZ', 2013, 3500),
(102, 'QSTU', 'STUV', 'HJIK', 'US', 2019, 1500),
(103, 'DEFG', 'EXPENSIVE', 'CHETAN BHAGAT', 'AUS', 2013, 4500),
(104, 'ABFRCD', 'RGXYZ', 'HJIK', 'NZ', 2013, 500),
(105, 'QSTU', 'EXPENSIVE', 'FGHY', 'US', 2018, 4550),
(107, 'ABCDEF', 'EXPENSIVE', 'HJIKLM', 'NZ', 2003, 3500);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
