-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 05, 2019 at 05:56 AM
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
-- Table structure for table `agents`
--

CREATE TABLE `agents` (
  `AGENT_ID` int(11) NOT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  `CITY` varchar(100) DEFAULT NULL,
  `COMMISION` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `agents`
--

INSERT INTO `agents` (`AGENT_ID`, `NAME`, `CITY`, `COMMISION`) VALUES
(1, 'ABC', 'TVM', 50000),
(2, 'EFG', 'ATL', 15000),
(3, 'XYZ', 'KZM', 45000),
(4, 'STU', 'ATL', 35000),
(5, 'MNO', 'KZM', 50000),
(9, 'GHI', 'ALP', 95000);

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

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `CUSTOMER_ID` int(11) NOT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  `CITY` varchar(100) DEFAULT NULL,
  `AGENT_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`CUSTOMER_ID`, `NAME`, `CITY`, `AGENT_ID`) VALUES
(1, 'BINI', 'TVM', 8),
(3, 'ARUN', 'TVM', 1),
(4, 'CINU', 'KZM', 3),
(5, 'ANU', 'ATL', 5),
(8, 'RIYA', 'TVM', 9),
(9, 'ANITHA', 'TVM', 3);

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `Doc_Id` int(11) NOT NULL,
  `DocName` varchar(100) DEFAULT NULL,
  `DocYear` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `documents`
--

INSERT INTO `documents` (`Doc_Id`, `DocName`, `DocYear`) VALUES
(101, 'CSE', 2011),
(102, 'ECE', 2001),
(103, 'EEE', 1991),
(104, 'EEC', 1991),
(105, 'EMC', 2007);

-- --------------------------------------------------------

--
-- Table structure for table `newspaper`
--

CREATE TABLE `newspaper` (
  `Id` int(11) NOT NULL,
  `PaperName` varchar(100) DEFAULT NULL,
  `PaperLang` int(11) DEFAULT NULL,
  `Doc_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `newspaper`
--

INSERT INTO `newspaper` (`Id`, `PaperName`, `PaperLang`, `Doc_Id`) VALUES
(105, 'ABC', 1, 101),
(106, 'xyz', 2, 110),
(103, 'stu', 2, 111),
(107, 'PQR', 3, 107),
(110, 'QRS', 1, 102),
(111, 'OPR', 1, 103);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `ORDER_ID` int(11) NOT NULL,
  `CUSTOMER_ID` int(11) DEFAULT NULL,
  `AGENT_ID` int(11) DEFAULT NULL,
  `PURCHASE_AMT` float DEFAULT NULL,
  `ORDER_DATE` date DEFAULT NULL,
  `NO_OF_ITEMS` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`ORDER_ID`, `CUSTOMER_ID`, `AGENT_ID`, `PURCHASE_AMT`, `ORDER_DATE`, `NO_OF_ITEMS`) VALUES
(1, 1, 4, 11000, '2001-02-10', 9),
(3, 1, 2, 5000, '2011-12-14', 5),
(4, 2, 3, 15000, '1998-10-02', 15),
(8, 4, 9, 45000, '2017-06-21', 11);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `PRODUCT_ID` int(11) NOT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  `PRICE` float DEFAULT NULL,
  `AGENT_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`PRODUCT_ID`, `NAME`, `PRICE`, `AGENT_ID`) VALUES
(101, 'PENDRIVE', 500, 3),
(102, 'LAPTOP', 45000, 5),
(103, 'HARDDISK', 1500, 2),
(104, 'SMARTTV', 65000, 2),
(105, 'MOUSE', 700, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl`
--

CREATE TABLE `tbl` (
  `id` int(11) NOT NULL,
  `description` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_books`
--

CREATE TABLE `user_books` (
  `ID` int(11) NOT NULL,
  `USER_NAME` varchar(100) DEFAULT NULL,
  `BOOK_ID` int(11) DEFAULT NULL,
  `USER_COUNTRY` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_books`
--

INSERT INTO `user_books` (`ID`, `USER_NAME`, `BOOK_ID`, `USER_COUNTRY`) VALUES
(101, 'arun', 1001, 'auh'),
(102, 'anu', 1003, 'aus'),
(103, 'riya', 1002, 'nz'),
(104, 'tinu', 1009, 'us'),
(109, 'miya', 1008, 'aus'),
(110, 'nivaan', 1111, 'aus');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agents`
--
ALTER TABLE `agents`
  ADD PRIMARY KEY (`AGENT_ID`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CUSTOMER_ID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`ORDER_ID`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`PRODUCT_ID`);

--
-- Indexes for table `tbl`
--
ALTER TABLE `tbl`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agents`
--
ALTER TABLE `agents`
  MODIFY `AGENT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `CUSTOMER_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `ORDER_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl`
--
ALTER TABLE `tbl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
