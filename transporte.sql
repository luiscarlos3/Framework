-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-02-2021 a las 18:33:37
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `transporte`
--
CREATE DATABASE IF NOT EXISTS `transporte` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `transporte`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camion`
--

CREATE TABLE `camion` (
  `matricula` varchar(11) NOT NULL,
  `modelo` year(4) NOT NULL,
  `tipo` varchar(20) NOT NULL DEFAULT 'CAMION',
  `potencia` varchar(11) NOT NULL,
  `doc_camionero` varchar(12) NOT NULL,
  `registro_matricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `camion`
--

INSERT INTO `camion` VALUES('atx234', 1997, 'volqueta', '255', '3445', 244);
INSERT INTO `camion` VALUES('ijq24d', 2003, 'turbo', '255', '3445', 244);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camionero`
--

CREATE TABLE `camionero` (
  `documento` varchar(12) NOT NULL,
  `nombre_camionero` varchar(30) NOT NULL,
  `apellido_camionero` varchar(45) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `direccion_camionero` varchar(50) NOT NULL,
  `salario` double(10,0) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `ciudad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `camionero`
--

INSERT INTO `camionero` VALUES('1100789123', 'luis', 'silva', '12344', 'avenida ', 5000000, '1961-05-02', 914);
INSERT INTO `camionero` VALUES('3445', 'luis', 'silva', '12345', 'calle', 4000, '1961-02-02', 573);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `codigo` int(11) NOT NULL,
  `nombre_departamento` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` VALUES(5, 'ANTIOQUIA');
INSERT INTO `departamento` VALUES(8, 'ATLÁNTICO');
INSERT INTO `departamento` VALUES(11, 'BOGOTÁ, D.C.');
INSERT INTO `departamento` VALUES(13, 'BOLÍVAR');
INSERT INTO `departamento` VALUES(15, 'BOYACÁ');
INSERT INTO `departamento` VALUES(17, 'CALDAS');
INSERT INTO `departamento` VALUES(18, 'CAQUETÁ');
INSERT INTO `departamento` VALUES(19, 'CAUCA');
INSERT INTO `departamento` VALUES(20, 'CESAR');
INSERT INTO `departamento` VALUES(23, 'CÓRDOBA');
INSERT INTO `departamento` VALUES(25, 'CUNDINAMARCA');
INSERT INTO `departamento` VALUES(27, 'CHOCÓ');
INSERT INTO `departamento` VALUES(41, 'HUILA');
INSERT INTO `departamento` VALUES(44, 'LA GUAJIRA');
INSERT INTO `departamento` VALUES(47, 'MAGDALENA');
INSERT INTO `departamento` VALUES(50, 'META');
INSERT INTO `departamento` VALUES(52, 'NARIÑO');
INSERT INTO `departamento` VALUES(54, 'NORTE DE SANTANDER');
INSERT INTO `departamento` VALUES(63, 'QUINDIO');
INSERT INTO `departamento` VALUES(66, 'RISARALDA');
INSERT INTO `departamento` VALUES(68, 'SANTANDER');
INSERT INTO `departamento` VALUES(70, 'SUCRE');
INSERT INTO `departamento` VALUES(73, 'TOLIMA');
INSERT INTO `departamento` VALUES(76, 'VALLE DEL CAUCA');
INSERT INTO `departamento` VALUES(81, 'ARAUCA');
INSERT INTO `departamento` VALUES(85, 'CASANARE');
INSERT INTO `departamento` VALUES(86, 'PUTUMAYO');
INSERT INTO `departamento` VALUES(88, 'ARCHIPIÉLAGO DE SAN ');
INSERT INTO `departamento` VALUES(91, 'AMAZONAS');
INSERT INTO `departamento` VALUES(94, 'GUAINÍA');
INSERT INTO `departamento` VALUES(95, 'GUAVIARE');
INSERT INTO `departamento` VALUES(97, 'VAUPÉS');
INSERT INTO `departamento` VALUES(99, 'VICHADA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `destinatario`
--

CREATE TABLE `destinatario` (
  `documento` varchar(12) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `teléfono` varchar(10) NOT NULL,
  `direccion_destinatario` varchar(50) DEFAULT NULL,
  `ciudad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `destinatario`
--

INSERT INTO `destinatario` VALUES('110012', 'manuel maria', 'soto', '31245612', 'avenida las peñitas', 573);
INSERT INTO `destinatario` VALUES('1100234', 'jose miguel', 'blanco', '312456890', 'el poblado', 244);
INSERT INTO `destinatario` VALUES('1100456789', 'jose luis', 'beltran aguilar', '3124567812', 'calle falsa 123', 244);
INSERT INTO `destinatario` VALUES('110234567', 'jose', 'guzman', '304678901', 'avenida siempre viva', 914);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `envio`
--

CREATE TABLE `envio` (
  `id_envio` int(11) NOT NULL,
  `envio_camionero` varchar(12) NOT NULL,
  `envio_destinatario` varchar(12) NOT NULL,
  `envio_remitente` varchar(12) NOT NULL,
  `direccion` varchar(80) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `fecha_envio` datetime NOT NULL,
  `fecha_llegada` date NOT NULL,
  `id_paquete` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `envio`
--

INSERT INTO `envio` VALUES(2147483647, '3445', '1100234', '110244567', 'avenida san blas', 'enviado', '2021-02-05 22:50:21', '2021-02-07', '7649762064');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipios`
--

CREATE TABLE `municipios` (
  `id_municipio` int(6) NOT NULL,
  `municipio` varchar(255) NOT NULL,
  `departamento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `municipios`
--

INSERT INTO `municipios` VALUES(1, 'Abriaquí', 5);
INSERT INTO `municipios` VALUES(2, 'Acacías', 50);
INSERT INTO `municipios` VALUES(3, 'Acandí', 27);
INSERT INTO `municipios` VALUES(4, 'Acevedo', 41);
INSERT INTO `municipios` VALUES(5, 'Achí', 13);
INSERT INTO `municipios` VALUES(6, 'Agrado', 41);
INSERT INTO `municipios` VALUES(7, 'Agua de Dios', 25);
INSERT INTO `municipios` VALUES(8, 'Aguachica', 20);
INSERT INTO `municipios` VALUES(9, 'Aguada', 68);
INSERT INTO `municipios` VALUES(10, 'Aguadas', 17);
INSERT INTO `municipios` VALUES(11, 'Aguazul', 85);
INSERT INTO `municipios` VALUES(12, 'Agustín Codazzi', 20);
INSERT INTO `municipios` VALUES(13, 'Aipe', 41);
INSERT INTO `municipios` VALUES(14, 'Albania', 18);
INSERT INTO `municipios` VALUES(15, 'Albania', 44);
INSERT INTO `municipios` VALUES(16, 'Albania', 68);
INSERT INTO `municipios` VALUES(17, 'Albán', 25);
INSERT INTO `municipios` VALUES(18, 'Albán (San José)', 52);
INSERT INTO `municipios` VALUES(19, 'Alcalá', 76);
INSERT INTO `municipios` VALUES(20, 'Alejandria', 5);
INSERT INTO `municipios` VALUES(21, 'Algarrobo', 47);
INSERT INTO `municipios` VALUES(22, 'Algeciras', 41);
INSERT INTO `municipios` VALUES(23, 'Almaguer', 19);
INSERT INTO `municipios` VALUES(24, 'Almeida', 15);
INSERT INTO `municipios` VALUES(25, 'Alpujarra', 73);
INSERT INTO `municipios` VALUES(26, 'Altamira', 41);
INSERT INTO `municipios` VALUES(27, 'Alto Baudó (Pie de Pato)', 27);
INSERT INTO `municipios` VALUES(28, 'Altos del Rosario', 13);
INSERT INTO `municipios` VALUES(29, 'Alvarado', 73);
INSERT INTO `municipios` VALUES(30, 'Amagá', 5);
INSERT INTO `municipios` VALUES(31, 'Amalfi', 5);
INSERT INTO `municipios` VALUES(32, 'Ambalema', 73);
INSERT INTO `municipios` VALUES(33, 'Anapoima', 25);
INSERT INTO `municipios` VALUES(34, 'Ancuya', 52);
INSERT INTO `municipios` VALUES(35, 'Andalucía', 76);
INSERT INTO `municipios` VALUES(36, 'Andes', 5);
INSERT INTO `municipios` VALUES(37, 'Angelópolis', 5);
INSERT INTO `municipios` VALUES(38, 'Angostura', 5);
INSERT INTO `municipios` VALUES(39, 'Anolaima', 25);
INSERT INTO `municipios` VALUES(40, 'Anorí', 5);
INSERT INTO `municipios` VALUES(41, 'Anserma', 17);
INSERT INTO `municipios` VALUES(42, 'Ansermanuevo', 76);
INSERT INTO `municipios` VALUES(43, 'Anzoátegui', 73);
INSERT INTO `municipios` VALUES(44, 'Anzá', 5);
INSERT INTO `municipios` VALUES(45, 'Apartadó', 5);
INSERT INTO `municipios` VALUES(46, 'Apulo', 25);
INSERT INTO `municipios` VALUES(47, 'Apía', 66);
INSERT INTO `municipios` VALUES(48, 'Aquitania', 15);
INSERT INTO `municipios` VALUES(49, 'Aracataca', 47);
INSERT INTO `municipios` VALUES(50, 'Aranzazu', 17);
INSERT INTO `municipios` VALUES(51, 'Aratoca', 68);
INSERT INTO `municipios` VALUES(52, 'Arauca', 81);
INSERT INTO `municipios` VALUES(53, 'Arauquita', 81);
INSERT INTO `municipios` VALUES(54, 'Arbeláez', 25);
INSERT INTO `municipios` VALUES(55, 'Arboleda (Berruecos)', 52);
INSERT INTO `municipios` VALUES(56, 'Arboledas', 54);
INSERT INTO `municipios` VALUES(57, 'Arboletes', 5);
INSERT INTO `municipios` VALUES(58, 'Arcabuco', 15);
INSERT INTO `municipios` VALUES(59, 'Arenal', 13);
INSERT INTO `municipios` VALUES(60, 'Argelia', 5);
INSERT INTO `municipios` VALUES(61, 'Argelia', 19);
INSERT INTO `municipios` VALUES(62, 'Argelia', 76);
INSERT INTO `municipios` VALUES(63, 'Ariguaní (El Difícil)', 47);
INSERT INTO `municipios` VALUES(64, 'Arjona', 13);
INSERT INTO `municipios` VALUES(65, 'Armenia', 5);
INSERT INTO `municipios` VALUES(66, 'Armenia', 63);
INSERT INTO `municipios` VALUES(67, 'Armero (Guayabal)', 73);
INSERT INTO `municipios` VALUES(68, 'Arroyohondo', 13);
INSERT INTO `municipios` VALUES(69, 'Astrea', 20);
INSERT INTO `municipios` VALUES(70, 'Ataco', 73);
INSERT INTO `municipios` VALUES(71, 'Atrato (Yuto)', 27);
INSERT INTO `municipios` VALUES(72, 'Ayapel', 23);
INSERT INTO `municipios` VALUES(73, 'Bagadó', 27);
INSERT INTO `municipios` VALUES(74, 'Bahía Solano (Mútis)', 27);
INSERT INTO `municipios` VALUES(75, 'Bajo Baudó (Pizarro)', 27);
INSERT INTO `municipios` VALUES(76, 'Balboa', 19);
INSERT INTO `municipios` VALUES(77, 'Balboa', 66);
INSERT INTO `municipios` VALUES(78, 'Baranoa', 8);
INSERT INTO `municipios` VALUES(79, 'Baraya', 41);
INSERT INTO `municipios` VALUES(80, 'Barbacoas', 52);
INSERT INTO `municipios` VALUES(81, 'Barbosa', 5);
INSERT INTO `municipios` VALUES(82, 'Barbosa', 68);
INSERT INTO `municipios` VALUES(83, 'Barichara', 68);
INSERT INTO `municipios` VALUES(84, 'Barranca de Upía', 50);
INSERT INTO `municipios` VALUES(85, 'Barrancabermeja', 68);
INSERT INTO `municipios` VALUES(86, 'Barrancas', 44);
INSERT INTO `municipios` VALUES(87, 'Barranco de Loba', 13);
INSERT INTO `municipios` VALUES(88, 'Barranquilla', 8);
INSERT INTO `municipios` VALUES(89, 'Becerríl', 20);
INSERT INTO `municipios` VALUES(90, 'Belalcázar', 17);
INSERT INTO `municipios` VALUES(91, 'Bello', 5);
INSERT INTO `municipios` VALUES(92, 'Belmira', 5);
INSERT INTO `municipios` VALUES(93, 'Beltrán', 25);
INSERT INTO `municipios` VALUES(94, 'Belén', 15);
INSERT INTO `municipios` VALUES(95, 'Belén', 52);
INSERT INTO `municipios` VALUES(96, 'Belén de Bajirá', 27);
INSERT INTO `municipios` VALUES(97, 'Belén de Umbría', 66);
INSERT INTO `municipios` VALUES(98, 'Belén de los Andaquíes', 18);
INSERT INTO `municipios` VALUES(99, 'Berbeo', 15);
INSERT INTO `municipios` VALUES(100, 'Betania', 5);
INSERT INTO `municipios` VALUES(101, 'Beteitiva', 15);
INSERT INTO `municipios` VALUES(102, 'Betulia', 5);
INSERT INTO `municipios` VALUES(103, 'Betulia', 68);
INSERT INTO `municipios` VALUES(104, 'Bituima', 25);
INSERT INTO `municipios` VALUES(105, 'Boavita', 15);
INSERT INTO `municipios` VALUES(106, 'Bochalema', 54);
INSERT INTO `municipios` VALUES(107, 'Bogotá D.C.', 11);
INSERT INTO `municipios` VALUES(108, 'Bojacá', 25);
INSERT INTO `municipios` VALUES(109, 'Bojayá (Bellavista)', 27);
INSERT INTO `municipios` VALUES(110, 'Bolívar', 5);
INSERT INTO `municipios` VALUES(111, 'Bolívar', 19);
INSERT INTO `municipios` VALUES(112, 'Bolívar', 68);
INSERT INTO `municipios` VALUES(113, 'Bolívar', 76);
INSERT INTO `municipios` VALUES(114, 'Bosconia', 20);
INSERT INTO `municipios` VALUES(115, 'Boyacá', 15);
INSERT INTO `municipios` VALUES(116, 'Briceño', 5);
INSERT INTO `municipios` VALUES(117, 'Briceño', 15);
INSERT INTO `municipios` VALUES(118, 'Bucaramanga', 68);
INSERT INTO `municipios` VALUES(119, 'Bucarasica', 54);
INSERT INTO `municipios` VALUES(120, 'Buenaventura', 76);
INSERT INTO `municipios` VALUES(121, 'Buenavista', 15);
INSERT INTO `municipios` VALUES(122, 'Buenavista', 23);
INSERT INTO `municipios` VALUES(123, 'Buenavista', 63);
INSERT INTO `municipios` VALUES(124, 'Buenavista', 70);
INSERT INTO `municipios` VALUES(125, 'Buenos Aires', 19);
INSERT INTO `municipios` VALUES(126, 'Buesaco', 52);
INSERT INTO `municipios` VALUES(127, 'Buga', 76);
INSERT INTO `municipios` VALUES(128, 'Bugalagrande', 76);
INSERT INTO `municipios` VALUES(129, 'Burítica', 5);
INSERT INTO `municipios` VALUES(130, 'Busbanza', 15);
INSERT INTO `municipios` VALUES(131, 'Cabrera', 25);
INSERT INTO `municipios` VALUES(132, 'Cabrera', 68);
INSERT INTO `municipios` VALUES(133, 'Cabuyaro', 50);
INSERT INTO `municipios` VALUES(134, 'Cachipay', 25);
INSERT INTO `municipios` VALUES(135, 'Caicedo', 5);
INSERT INTO `municipios` VALUES(136, 'Caicedonia', 76);
INSERT INTO `municipios` VALUES(137, 'Caimito', 70);
INSERT INTO `municipios` VALUES(138, 'Cajamarca', 73);
INSERT INTO `municipios` VALUES(139, 'Cajibío', 19);
INSERT INTO `municipios` VALUES(140, 'Cajicá', 25);
INSERT INTO `municipios` VALUES(141, 'Calamar', 13);
INSERT INTO `municipios` VALUES(142, 'Calamar', 95);
INSERT INTO `municipios` VALUES(143, 'Calarcá', 63);
INSERT INTO `municipios` VALUES(144, 'Caldas', 5);
INSERT INTO `municipios` VALUES(145, 'Caldas', 15);
INSERT INTO `municipios` VALUES(146, 'Caldono', 19);
INSERT INTO `municipios` VALUES(147, 'California', 68);
INSERT INTO `municipios` VALUES(148, 'Calima (Darién)', 76);
INSERT INTO `municipios` VALUES(149, 'Caloto', 19);
INSERT INTO `municipios` VALUES(150, 'Calí', 76);
INSERT INTO `municipios` VALUES(151, 'Campamento', 5);
INSERT INTO `municipios` VALUES(152, 'Campo de la Cruz', 8);
INSERT INTO `municipios` VALUES(153, 'Campoalegre', 41);
INSERT INTO `municipios` VALUES(154, 'Campohermoso', 15);
INSERT INTO `municipios` VALUES(155, 'Canalete', 23);
INSERT INTO `municipios` VALUES(156, 'Candelaria', 8);
INSERT INTO `municipios` VALUES(157, 'Candelaria', 76);
INSERT INTO `municipios` VALUES(158, 'Cantagallo', 13);
INSERT INTO `municipios` VALUES(159, 'Cantón de San Pablo', 27);
INSERT INTO `municipios` VALUES(160, 'Caparrapí', 25);
INSERT INTO `municipios` VALUES(161, 'Capitanejo', 68);
INSERT INTO `municipios` VALUES(162, 'Caracolí', 5);
INSERT INTO `municipios` VALUES(163, 'Caramanta', 5);
INSERT INTO `municipios` VALUES(164, 'Carcasí', 68);
INSERT INTO `municipios` VALUES(165, 'Carepa', 5);
INSERT INTO `municipios` VALUES(166, 'Carmen de Apicalá', 73);
INSERT INTO `municipios` VALUES(167, 'Carmen de Carupa', 25);
INSERT INTO `municipios` VALUES(168, 'Carmen de Viboral', 5);
INSERT INTO `municipios` VALUES(169, 'Carmen del Darién (CURBARADÓ)', 27);
INSERT INTO `municipios` VALUES(170, 'Carolina', 5);
INSERT INTO `municipios` VALUES(171, 'Cartagena', 13);
INSERT INTO `municipios` VALUES(172, 'Cartagena del Chairá', 18);
INSERT INTO `municipios` VALUES(173, 'Cartago', 76);
INSERT INTO `municipios` VALUES(174, 'Carurú', 97);
INSERT INTO `municipios` VALUES(175, 'Casabianca', 73);
INSERT INTO `municipios` VALUES(176, 'Castilla la Nueva', 50);
INSERT INTO `municipios` VALUES(177, 'Caucasia', 5);
INSERT INTO `municipios` VALUES(178, 'Cañasgordas', 5);
INSERT INTO `municipios` VALUES(179, 'Cepita', 68);
INSERT INTO `municipios` VALUES(180, 'Cereté', 23);
INSERT INTO `municipios` VALUES(181, 'Cerinza', 15);
INSERT INTO `municipios` VALUES(182, 'Cerrito', 68);
INSERT INTO `municipios` VALUES(183, 'Cerro San Antonio', 47);
INSERT INTO `municipios` VALUES(184, 'Chachaguí', 52);
INSERT INTO `municipios` VALUES(185, 'Chaguaní', 25);
INSERT INTO `municipios` VALUES(186, 'Chalán', 70);
INSERT INTO `municipios` VALUES(187, 'Chaparral', 73);
INSERT INTO `municipios` VALUES(188, 'Charalá', 68);
INSERT INTO `municipios` VALUES(189, 'Charta', 68);
INSERT INTO `municipios` VALUES(190, 'Chigorodó', 5);
INSERT INTO `municipios` VALUES(191, 'Chima', 68);
INSERT INTO `municipios` VALUES(192, 'Chimichagua', 20);
INSERT INTO `municipios` VALUES(193, 'Chimá', 23);
INSERT INTO `municipios` VALUES(194, 'Chinavita', 15);
INSERT INTO `municipios` VALUES(195, 'Chinchiná', 17);
INSERT INTO `municipios` VALUES(196, 'Chinácota', 54);
INSERT INTO `municipios` VALUES(197, 'Chinú', 23);
INSERT INTO `municipios` VALUES(198, 'Chipaque', 25);
INSERT INTO `municipios` VALUES(199, 'Chipatá', 68);
INSERT INTO `municipios` VALUES(200, 'Chiquinquirá', 15);
INSERT INTO `municipios` VALUES(201, 'Chiriguaná', 20);
INSERT INTO `municipios` VALUES(202, 'Chiscas', 15);
INSERT INTO `municipios` VALUES(203, 'Chita', 15);
INSERT INTO `municipios` VALUES(204, 'Chitagá', 54);
INSERT INTO `municipios` VALUES(205, 'Chitaraque', 15);
INSERT INTO `municipios` VALUES(206, 'Chivatá', 15);
INSERT INTO `municipios` VALUES(207, 'Chivolo', 47);
INSERT INTO `municipios` VALUES(208, 'Choachí', 25);
INSERT INTO `municipios` VALUES(209, 'Chocontá', 25);
INSERT INTO `municipios` VALUES(210, 'Chámeza', 85);
INSERT INTO `municipios` VALUES(211, 'Chía', 25);
INSERT INTO `municipios` VALUES(212, 'Chíquiza', 15);
INSERT INTO `municipios` VALUES(213, 'Chívor', 15);
INSERT INTO `municipios` VALUES(214, 'Cicuco', 13);
INSERT INTO `municipios` VALUES(215, 'Cimitarra', 68);
INSERT INTO `municipios` VALUES(216, 'Circasia', 63);
INSERT INTO `municipios` VALUES(217, 'Cisneros', 5);
INSERT INTO `municipios` VALUES(218, 'Ciénaga', 15);
INSERT INTO `municipios` VALUES(219, 'Ciénaga', 47);
INSERT INTO `municipios` VALUES(220, 'Ciénaga de Oro', 23);
INSERT INTO `municipios` VALUES(221, 'Clemencia', 13);
INSERT INTO `municipios` VALUES(222, 'Cocorná', 5);
INSERT INTO `municipios` VALUES(223, 'Coello', 73);
INSERT INTO `municipios` VALUES(224, 'Cogua', 25);
INSERT INTO `municipios` VALUES(225, 'Colombia', 41);
INSERT INTO `municipios` VALUES(226, 'Colosó (Ricaurte)', 70);
INSERT INTO `municipios` VALUES(227, 'Colón', 86);
INSERT INTO `municipios` VALUES(228, 'Colón (Génova)', 52);
INSERT INTO `municipios` VALUES(229, 'Concepción', 5);
INSERT INTO `municipios` VALUES(230, 'Concepción', 68);
INSERT INTO `municipios` VALUES(231, 'Concordia', 5);
INSERT INTO `municipios` VALUES(232, 'Concordia', 47);
INSERT INTO `municipios` VALUES(233, 'Condoto', 27);
INSERT INTO `municipios` VALUES(234, 'Confines', 68);
INSERT INTO `municipios` VALUES(235, 'Consaca', 52);
INSERT INTO `municipios` VALUES(236, 'Contadero', 52);
INSERT INTO `municipios` VALUES(237, 'Contratación', 68);
INSERT INTO `municipios` VALUES(238, 'Convención', 54);
INSERT INTO `municipios` VALUES(239, 'Copacabana', 5);
INSERT INTO `municipios` VALUES(240, 'Coper', 15);
INSERT INTO `municipios` VALUES(241, 'Cordobá', 63);
INSERT INTO `municipios` VALUES(242, 'Corinto', 19);
INSERT INTO `municipios` VALUES(243, 'Coromoro', 68);
INSERT INTO `municipios` VALUES(244, 'Corozal', 70);
INSERT INTO `municipios` VALUES(245, 'Corrales', 15);
INSERT INTO `municipios` VALUES(246, 'Cota', 25);
INSERT INTO `municipios` VALUES(247, 'Cotorra', 23);
INSERT INTO `municipios` VALUES(248, 'Covarachía', 15);
INSERT INTO `municipios` VALUES(249, 'Coveñas', 70);
INSERT INTO `municipios` VALUES(250, 'Coyaima', 73);
INSERT INTO `municipios` VALUES(251, 'Cravo Norte', 81);
INSERT INTO `municipios` VALUES(252, 'Cuaspud (Carlosama)', 52);
INSERT INTO `municipios` VALUES(253, 'Cubarral', 50);
INSERT INTO `municipios` VALUES(254, 'Cubará', 15);
INSERT INTO `municipios` VALUES(255, 'Cucaita', 15);
INSERT INTO `municipios` VALUES(256, 'Cucunubá', 25);
INSERT INTO `municipios` VALUES(257, 'Cucutilla', 54);
INSERT INTO `municipios` VALUES(258, 'Cuitiva', 15);
INSERT INTO `municipios` VALUES(259, 'Cumaral', 50);
INSERT INTO `municipios` VALUES(260, 'Cumaribo', 99);
INSERT INTO `municipios` VALUES(261, 'Cumbal', 52);
INSERT INTO `municipios` VALUES(262, 'Cumbitara', 52);
INSERT INTO `municipios` VALUES(263, 'Cunday', 73);
INSERT INTO `municipios` VALUES(264, 'Curillo', 18);
INSERT INTO `municipios` VALUES(265, 'Curití', 68);
INSERT INTO `municipios` VALUES(266, 'Curumaní', 20);
INSERT INTO `municipios` VALUES(267, 'Cáceres', 5);
INSERT INTO `municipios` VALUES(268, 'Cáchira', 54);
INSERT INTO `municipios` VALUES(269, 'Cácota', 54);
INSERT INTO `municipios` VALUES(270, 'Cáqueza', 25);
INSERT INTO `municipios` VALUES(271, 'Cértegui', 27);
INSERT INTO `municipios` VALUES(272, 'Cómbita', 15);
INSERT INTO `municipios` VALUES(273, 'Córdoba', 13);
INSERT INTO `municipios` VALUES(274, 'Córdoba', 52);
INSERT INTO `municipios` VALUES(275, 'Cúcuta', 54);
INSERT INTO `municipios` VALUES(276, 'Dabeiba', 5);
INSERT INTO `municipios` VALUES(277, 'Dagua', 76);
INSERT INTO `municipios` VALUES(278, 'Dibulla', 44);
INSERT INTO `municipios` VALUES(279, 'Distracción', 44);
INSERT INTO `municipios` VALUES(280, 'Dolores', 73);
INSERT INTO `municipios` VALUES(281, 'Don Matías', 5);
INSERT INTO `municipios` VALUES(282, 'Dos Quebradas', 66);
INSERT INTO `municipios` VALUES(283, 'Duitama', 15);
INSERT INTO `municipios` VALUES(284, 'Durania', 54);
INSERT INTO `municipios` VALUES(285, 'Ebéjico', 5);
INSERT INTO `municipios` VALUES(286, 'El Bagre', 5);
INSERT INTO `municipios` VALUES(287, 'El Banco', 47);
INSERT INTO `municipios` VALUES(288, 'El Cairo', 76);
INSERT INTO `municipios` VALUES(289, 'El Calvario', 50);
INSERT INTO `municipios` VALUES(290, 'El Carmen', 54);
INSERT INTO `municipios` VALUES(291, 'El Carmen', 68);
INSERT INTO `municipios` VALUES(292, 'El Carmen de Atrato', 27);
INSERT INTO `municipios` VALUES(293, 'El Carmen de Bolívar', 13);
INSERT INTO `municipios` VALUES(294, 'El Castillo', 50);
INSERT INTO `municipios` VALUES(295, 'El Cerrito', 76);
INSERT INTO `municipios` VALUES(296, 'El Charco', 52);
INSERT INTO `municipios` VALUES(297, 'El Cocuy', 15);
INSERT INTO `municipios` VALUES(298, 'El Colegio', 25);
INSERT INTO `municipios` VALUES(299, 'El Copey', 20);
INSERT INTO `municipios` VALUES(300, 'El Doncello', 18);
INSERT INTO `municipios` VALUES(301, 'El Dorado', 50);
INSERT INTO `municipios` VALUES(302, 'El Dovio', 76);
INSERT INTO `municipios` VALUES(303, 'El Espino', 15);
INSERT INTO `municipios` VALUES(304, 'El Guacamayo', 68);
INSERT INTO `municipios` VALUES(305, 'El Guamo', 13);
INSERT INTO `municipios` VALUES(306, 'El Molino', 44);
INSERT INTO `municipios` VALUES(307, 'El Paso', 20);
INSERT INTO `municipios` VALUES(308, 'El Paujil', 18);
INSERT INTO `municipios` VALUES(309, 'El Peñol', 52);
INSERT INTO `municipios` VALUES(310, 'El Peñon', 13);
INSERT INTO `municipios` VALUES(311, 'El Peñon', 68);
INSERT INTO `municipios` VALUES(312, 'El Peñón', 25);
INSERT INTO `municipios` VALUES(313, 'El Piñon', 47);
INSERT INTO `municipios` VALUES(314, 'El Playón', 68);
INSERT INTO `municipios` VALUES(315, 'El Retorno', 95);
INSERT INTO `municipios` VALUES(316, 'El Retén', 47);
INSERT INTO `municipios` VALUES(317, 'El Roble', 70);
INSERT INTO `municipios` VALUES(318, 'El Rosal', 25);
INSERT INTO `municipios` VALUES(319, 'El Rosario', 52);
INSERT INTO `municipios` VALUES(320, 'El Tablón de Gómez', 52);
INSERT INTO `municipios` VALUES(321, 'El Tambo', 19);
INSERT INTO `municipios` VALUES(322, 'El Tambo', 52);
INSERT INTO `municipios` VALUES(323, 'El Tarra', 54);
INSERT INTO `municipios` VALUES(324, 'El Zulia', 54);
INSERT INTO `municipios` VALUES(325, 'El Águila', 76);
INSERT INTO `municipios` VALUES(326, 'Elías', 41);
INSERT INTO `municipios` VALUES(327, 'Encino', 68);
INSERT INTO `municipios` VALUES(328, 'Enciso', 68);
INSERT INTO `municipios` VALUES(329, 'Entrerríos', 5);
INSERT INTO `municipios` VALUES(330, 'Envigado', 5);
INSERT INTO `municipios` VALUES(331, 'Espinal', 73);
INSERT INTO `municipios` VALUES(332, 'Facatativá', 25);
INSERT INTO `municipios` VALUES(333, 'Falan', 73);
INSERT INTO `municipios` VALUES(334, 'Filadelfia', 17);
INSERT INTO `municipios` VALUES(335, 'Filandia', 63);
INSERT INTO `municipios` VALUES(336, 'Firavitoba', 15);
INSERT INTO `municipios` VALUES(337, 'Flandes', 73);
INSERT INTO `municipios` VALUES(338, 'Florencia', 18);
INSERT INTO `municipios` VALUES(339, 'Florencia', 19);
INSERT INTO `municipios` VALUES(340, 'Floresta', 15);
INSERT INTO `municipios` VALUES(341, 'Florida', 76);
INSERT INTO `municipios` VALUES(342, 'Floridablanca', 68);
INSERT INTO `municipios` VALUES(343, 'Florián', 68);
INSERT INTO `municipios` VALUES(344, 'Fonseca', 44);
INSERT INTO `municipios` VALUES(345, 'Fortúl', 81);
INSERT INTO `municipios` VALUES(346, 'Fosca', 25);
INSERT INTO `municipios` VALUES(347, 'Francisco Pizarro', 52);
INSERT INTO `municipios` VALUES(348, 'Fredonia', 5);
INSERT INTO `municipios` VALUES(349, 'Fresno', 73);
INSERT INTO `municipios` VALUES(350, 'Frontino', 5);
INSERT INTO `municipios` VALUES(351, 'Fuente de Oro', 50);
INSERT INTO `municipios` VALUES(352, 'Fundación', 47);
INSERT INTO `municipios` VALUES(353, 'Funes', 52);
INSERT INTO `municipios` VALUES(354, 'Funza', 25);
INSERT INTO `municipios` VALUES(355, 'Fusagasugá', 25);
INSERT INTO `municipios` VALUES(356, 'Fómeque', 25);
INSERT INTO `municipios` VALUES(357, 'Fúquene', 25);
INSERT INTO `municipios` VALUES(358, 'Gachalá', 25);
INSERT INTO `municipios` VALUES(359, 'Gachancipá', 25);
INSERT INTO `municipios` VALUES(360, 'Gachantivá', 15);
INSERT INTO `municipios` VALUES(361, 'Gachetá', 25);
INSERT INTO `municipios` VALUES(362, 'Galapa', 8);
INSERT INTO `municipios` VALUES(363, 'Galeras (Nueva Granada)', 70);
INSERT INTO `municipios` VALUES(364, 'Galán', 68);
INSERT INTO `municipios` VALUES(365, 'Gama', 25);
INSERT INTO `municipios` VALUES(366, 'Gamarra', 20);
INSERT INTO `municipios` VALUES(367, 'Garagoa', 15);
INSERT INTO `municipios` VALUES(368, 'Garzón', 41);
INSERT INTO `municipios` VALUES(369, 'Gigante', 41);
INSERT INTO `municipios` VALUES(370, 'Ginebra', 76);
INSERT INTO `municipios` VALUES(371, 'Giraldo', 5);
INSERT INTO `municipios` VALUES(372, 'Girardot', 25);
INSERT INTO `municipios` VALUES(373, 'Girardota', 5);
INSERT INTO `municipios` VALUES(374, 'Girón', 68);
INSERT INTO `municipios` VALUES(375, 'Gonzalez', 20);
INSERT INTO `municipios` VALUES(376, 'Gramalote', 54);
INSERT INTO `municipios` VALUES(377, 'Granada', 5);
INSERT INTO `municipios` VALUES(378, 'Granada', 25);
INSERT INTO `municipios` VALUES(379, 'Granada', 50);
INSERT INTO `municipios` VALUES(380, 'Guaca', 68);
INSERT INTO `municipios` VALUES(381, 'Guacamayas', 15);
INSERT INTO `municipios` VALUES(382, 'Guacarí', 76);
INSERT INTO `municipios` VALUES(383, 'Guachavés', 52);
INSERT INTO `municipios` VALUES(384, 'Guachené', 19);
INSERT INTO `municipios` VALUES(385, 'Guachetá', 25);
INSERT INTO `municipios` VALUES(386, 'Guachucal', 52);
INSERT INTO `municipios` VALUES(387, 'Guadalupe', 5);
INSERT INTO `municipios` VALUES(388, 'Guadalupe', 41);
INSERT INTO `municipios` VALUES(389, 'Guadalupe', 68);
INSERT INTO `municipios` VALUES(390, 'Guaduas', 25);
INSERT INTO `municipios` VALUES(391, 'Guaitarilla', 52);
INSERT INTO `municipios` VALUES(392, 'Gualmatán', 52);
INSERT INTO `municipios` VALUES(393, 'Guamal', 47);
INSERT INTO `municipios` VALUES(394, 'Guamal', 50);
INSERT INTO `municipios` VALUES(395, 'Guamo', 73);
INSERT INTO `municipios` VALUES(396, 'Guapota', 68);
INSERT INTO `municipios` VALUES(397, 'Guapí', 19);
INSERT INTO `municipios` VALUES(398, 'Guaranda', 70);
INSERT INTO `municipios` VALUES(399, 'Guarne', 5);
INSERT INTO `municipios` VALUES(400, 'Guasca', 25);
INSERT INTO `municipios` VALUES(401, 'Guatapé', 5);
INSERT INTO `municipios` VALUES(402, 'Guataquí', 25);
INSERT INTO `municipios` VALUES(403, 'Guatavita', 25);
INSERT INTO `municipios` VALUES(404, 'Guateque', 15);
INSERT INTO `municipios` VALUES(405, 'Guavatá', 68);
INSERT INTO `municipios` VALUES(406, 'Guayabal de Siquima', 25);
INSERT INTO `municipios` VALUES(407, 'Guayabetal', 25);
INSERT INTO `municipios` VALUES(408, 'Guayatá', 15);
INSERT INTO `municipios` VALUES(409, 'Guepsa', 68);
INSERT INTO `municipios` VALUES(410, 'Guicán', 15);
INSERT INTO `municipios` VALUES(411, 'Gutiérrez', 25);
INSERT INTO `municipios` VALUES(412, 'Guática', 66);
INSERT INTO `municipios` VALUES(413, 'Gámbita', 68);
INSERT INTO `municipios` VALUES(414, 'Gámeza', 15);
INSERT INTO `municipios` VALUES(415, 'Génova', 63);
INSERT INTO `municipios` VALUES(416, 'Gómez Plata', 5);
INSERT INTO `municipios` VALUES(417, 'Hacarí', 54);
INSERT INTO `municipios` VALUES(418, 'Hatillo de Loba', 13);
INSERT INTO `municipios` VALUES(419, 'Hato', 68);
INSERT INTO `municipios` VALUES(420, 'Hato Corozal', 85);
INSERT INTO `municipios` VALUES(421, 'Hatonuevo', 44);
INSERT INTO `municipios` VALUES(422, 'Heliconia', 5);
INSERT INTO `municipios` VALUES(423, 'Herrán', 54);
INSERT INTO `municipios` VALUES(424, 'Herveo', 73);
INSERT INTO `municipios` VALUES(425, 'Hispania', 5);
INSERT INTO `municipios` VALUES(426, 'Hobo', 41);
INSERT INTO `municipios` VALUES(427, 'Honda', 73);
INSERT INTO `municipios` VALUES(428, 'Ibagué', 73);
INSERT INTO `municipios` VALUES(429, 'Icononzo', 73);
INSERT INTO `municipios` VALUES(430, 'Iles', 52);
INSERT INTO `municipios` VALUES(431, 'Imúes', 52);
INSERT INTO `municipios` VALUES(432, 'Inzá', 19);
INSERT INTO `municipios` VALUES(433, 'Inírida', 94);
INSERT INTO `municipios` VALUES(434, 'Ipiales', 52);
INSERT INTO `municipios` VALUES(435, 'Isnos', 41);
INSERT INTO `municipios` VALUES(436, 'Istmina', 27);
INSERT INTO `municipios` VALUES(437, 'Itagüí', 5);
INSERT INTO `municipios` VALUES(438, 'Ituango', 5);
INSERT INTO `municipios` VALUES(439, 'Izá', 15);
INSERT INTO `municipios` VALUES(440, 'Jambaló', 19);
INSERT INTO `municipios` VALUES(441, 'Jamundí', 76);
INSERT INTO `municipios` VALUES(442, 'Jardín', 5);
INSERT INTO `municipios` VALUES(443, 'Jenesano', 15);
INSERT INTO `municipios` VALUES(444, 'Jericó', 5);
INSERT INTO `municipios` VALUES(445, 'Jericó', 15);
INSERT INTO `municipios` VALUES(446, 'Jerusalén', 25);
INSERT INTO `municipios` VALUES(447, 'Jesús María', 68);
INSERT INTO `municipios` VALUES(448, 'Jordán', 68);
INSERT INTO `municipios` VALUES(449, 'Juan de Acosta', 8);
INSERT INTO `municipios` VALUES(450, 'Junín', 25);
INSERT INTO `municipios` VALUES(451, 'Juradó', 27);
INSERT INTO `municipios` VALUES(452, 'La Apartada y La Frontera', 23);
INSERT INTO `municipios` VALUES(453, 'La Argentina', 41);
INSERT INTO `municipios` VALUES(454, 'La Belleza', 68);
INSERT INTO `municipios` VALUES(455, 'La Calera', 25);
INSERT INTO `municipios` VALUES(456, 'La Capilla', 15);
INSERT INTO `municipios` VALUES(457, 'La Ceja', 5);
INSERT INTO `municipios` VALUES(458, 'La Celia', 66);
INSERT INTO `municipios` VALUES(459, 'La Cruz', 52);
INSERT INTO `municipios` VALUES(460, 'La Cumbre', 76);
INSERT INTO `municipios` VALUES(461, 'La Dorada', 17);
INSERT INTO `municipios` VALUES(462, 'La Esperanza', 54);
INSERT INTO `municipios` VALUES(463, 'La Estrella', 5);
INSERT INTO `municipios` VALUES(464, 'La Florida', 52);
INSERT INTO `municipios` VALUES(465, 'La Gloria', 20);
INSERT INTO `municipios` VALUES(466, 'La Jagua de Ibirico', 20);
INSERT INTO `municipios` VALUES(467, 'La Jagua del Pilar', 44);
INSERT INTO `municipios` VALUES(468, 'La Llanada', 52);
INSERT INTO `municipios` VALUES(469, 'La Macarena', 50);
INSERT INTO `municipios` VALUES(470, 'La Merced', 17);
INSERT INTO `municipios` VALUES(471, 'La Mesa', 25);
INSERT INTO `municipios` VALUES(472, 'La Montañita', 18);
INSERT INTO `municipios` VALUES(473, 'La Palma', 25);
INSERT INTO `municipios` VALUES(474, 'La Paz', 68);
INSERT INTO `municipios` VALUES(475, 'La Paz (Robles)', 20);
INSERT INTO `municipios` VALUES(476, 'La Peña', 25);
INSERT INTO `municipios` VALUES(477, 'La Pintada', 5);
INSERT INTO `municipios` VALUES(478, 'La Plata', 41);
INSERT INTO `municipios` VALUES(479, 'La Playa', 54);
INSERT INTO `municipios` VALUES(480, 'La Primavera', 99);
INSERT INTO `municipios` VALUES(481, 'La Salina', 85);
INSERT INTO `municipios` VALUES(482, 'La Sierra', 19);
INSERT INTO `municipios` VALUES(483, 'La Tebaida', 63);
INSERT INTO `municipios` VALUES(484, 'La Tola', 52);
INSERT INTO `municipios` VALUES(485, 'La Unión', 5);
INSERT INTO `municipios` VALUES(486, 'La Unión', 52);
INSERT INTO `municipios` VALUES(487, 'La Unión', 70);
INSERT INTO `municipios` VALUES(488, 'La Unión', 76);
INSERT INTO `municipios` VALUES(489, 'La Uvita', 15);
INSERT INTO `municipios` VALUES(490, 'La Vega', 19);
INSERT INTO `municipios` VALUES(491, 'La Vega', 25);
INSERT INTO `municipios` VALUES(492, 'La Victoria', 15);
INSERT INTO `municipios` VALUES(493, 'La Victoria', 17);
INSERT INTO `municipios` VALUES(494, 'La Victoria', 76);
INSERT INTO `municipios` VALUES(495, 'La Virginia', 66);
INSERT INTO `municipios` VALUES(496, 'Labateca', 54);
INSERT INTO `municipios` VALUES(497, 'Labranzagrande', 15);
INSERT INTO `municipios` VALUES(498, 'Landázuri', 68);
INSERT INTO `municipios` VALUES(499, 'Lebrija', 68);
INSERT INTO `municipios` VALUES(500, 'Leiva', 52);
INSERT INTO `municipios` VALUES(501, 'Lejanías', 50);
INSERT INTO `municipios` VALUES(502, 'Lenguazaque', 25);
INSERT INTO `municipios` VALUES(503, 'Leticia', 91);
INSERT INTO `municipios` VALUES(504, 'Liborina', 5);
INSERT INTO `municipios` VALUES(505, 'Linares', 52);
INSERT INTO `municipios` VALUES(506, 'Lloró', 27);
INSERT INTO `municipios` VALUES(507, 'Lorica', 23);
INSERT INTO `municipios` VALUES(508, 'Los Córdobas', 23);
INSERT INTO `municipios` VALUES(509, 'Los Palmitos', 70);
INSERT INTO `municipios` VALUES(510, 'Los Patios', 54);
INSERT INTO `municipios` VALUES(511, 'Los Santos', 68);
INSERT INTO `municipios` VALUES(512, 'Lourdes', 54);
INSERT INTO `municipios` VALUES(513, 'Luruaco', 8);
INSERT INTO `municipios` VALUES(514, 'Lérida', 73);
INSERT INTO `municipios` VALUES(515, 'Líbano', 73);
INSERT INTO `municipios` VALUES(516, 'López (Micay)', 19);
INSERT INTO `municipios` VALUES(517, 'Macanal', 15);
INSERT INTO `municipios` VALUES(518, 'Macaravita', 68);
INSERT INTO `municipios` VALUES(519, 'Maceo', 5);
INSERT INTO `municipios` VALUES(520, 'Machetá', 25);
INSERT INTO `municipios` VALUES(521, 'Madrid', 25);
INSERT INTO `municipios` VALUES(522, 'Magangué', 13);
INSERT INTO `municipios` VALUES(523, 'Magüi (Payán)', 52);
INSERT INTO `municipios` VALUES(524, 'Mahates', 13);
INSERT INTO `municipios` VALUES(525, 'Maicao', 44);
INSERT INTO `municipios` VALUES(526, 'Majagual', 70);
INSERT INTO `municipios` VALUES(527, 'Malambo', 8);
INSERT INTO `municipios` VALUES(528, 'Mallama (Piedrancha)', 52);
INSERT INTO `municipios` VALUES(529, 'Manatí', 8);
INSERT INTO `municipios` VALUES(530, 'Manaure', 44);
INSERT INTO `municipios` VALUES(531, 'Manaure Balcón del Cesar', 20);
INSERT INTO `municipios` VALUES(532, 'Manizales', 17);
INSERT INTO `municipios` VALUES(533, 'Manta', 25);
INSERT INTO `municipios` VALUES(534, 'Manzanares', 17);
INSERT INTO `municipios` VALUES(535, 'Maní', 85);
INSERT INTO `municipios` VALUES(536, 'Mapiripan', 50);
INSERT INTO `municipios` VALUES(537, 'Margarita', 13);
INSERT INTO `municipios` VALUES(538, 'Marinilla', 5);
INSERT INTO `municipios` VALUES(539, 'Maripí', 15);
INSERT INTO `municipios` VALUES(540, 'Mariquita', 73);
INSERT INTO `municipios` VALUES(541, 'Marmato', 17);
INSERT INTO `municipios` VALUES(542, 'Marquetalia', 17);
INSERT INTO `municipios` VALUES(543, 'Marsella', 66);
INSERT INTO `municipios` VALUES(544, 'Marulanda', 17);
INSERT INTO `municipios` VALUES(545, 'María la Baja', 13);
INSERT INTO `municipios` VALUES(546, 'Matanza', 68);
INSERT INTO `municipios` VALUES(547, 'Medellín', 5);
INSERT INTO `municipios` VALUES(548, 'Medina', 25);
INSERT INTO `municipios` VALUES(549, 'Medio Atrato', 27);
INSERT INTO `municipios` VALUES(550, 'Medio Baudó', 27);
INSERT INTO `municipios` VALUES(551, 'Medio San Juan (ANDAGOYA)', 27);
INSERT INTO `municipios` VALUES(552, 'Melgar', 73);
INSERT INTO `municipios` VALUES(553, 'Mercaderes', 19);
INSERT INTO `municipios` VALUES(554, 'Mesetas', 50);
INSERT INTO `municipios` VALUES(555, 'Milán', 18);
INSERT INTO `municipios` VALUES(556, 'Miraflores', 15);
INSERT INTO `municipios` VALUES(557, 'Miraflores', 95);
INSERT INTO `municipios` VALUES(558, 'Miranda', 19);
INSERT INTO `municipios` VALUES(559, 'Mistrató', 66);
INSERT INTO `municipios` VALUES(560, 'Mitú', 97);
INSERT INTO `municipios` VALUES(561, 'Mocoa', 86);
INSERT INTO `municipios` VALUES(562, 'Mogotes', 68);
INSERT INTO `municipios` VALUES(563, 'Molagavita', 68);
INSERT INTO `municipios` VALUES(564, 'Momil', 23);
INSERT INTO `municipios` VALUES(565, 'Mompós', 13);
INSERT INTO `municipios` VALUES(566, 'Mongua', 15);
INSERT INTO `municipios` VALUES(567, 'Monguí', 15);
INSERT INTO `municipios` VALUES(568, 'Moniquirá', 15);
INSERT INTO `municipios` VALUES(569, 'Montebello', 5);
INSERT INTO `municipios` VALUES(570, 'Montecristo', 13);
INSERT INTO `municipios` VALUES(571, 'Montelíbano', 23);
INSERT INTO `municipios` VALUES(572, 'Montenegro', 63);
INSERT INTO `municipios` VALUES(573, 'Monteria', 23);
INSERT INTO `municipios` VALUES(574, 'Monterrey', 85);
INSERT INTO `municipios` VALUES(575, 'Morales', 13);
INSERT INTO `municipios` VALUES(576, 'Morales', 19);
INSERT INTO `municipios` VALUES(577, 'Morelia', 18);
INSERT INTO `municipios` VALUES(578, 'Morroa', 70);
INSERT INTO `municipios` VALUES(579, 'Mosquera', 25);
INSERT INTO `municipios` VALUES(580, 'Mosquera', 52);
INSERT INTO `municipios` VALUES(581, 'Motavita', 15);
INSERT INTO `municipios` VALUES(582, 'Moñitos', 23);
INSERT INTO `municipios` VALUES(583, 'Murillo', 73);
INSERT INTO `municipios` VALUES(584, 'Murindó', 5);
INSERT INTO `municipios` VALUES(585, 'Mutatá', 5);
INSERT INTO `municipios` VALUES(586, 'Mutiscua', 54);
INSERT INTO `municipios` VALUES(587, 'Muzo', 15);
INSERT INTO `municipios` VALUES(588, 'Málaga', 68);
INSERT INTO `municipios` VALUES(589, 'Nariño', 5);
INSERT INTO `municipios` VALUES(590, 'Nariño', 25);
INSERT INTO `municipios` VALUES(591, 'Nariño', 52);
INSERT INTO `municipios` VALUES(592, 'Natagaima', 73);
INSERT INTO `municipios` VALUES(593, 'Nechí', 5);
INSERT INTO `municipios` VALUES(594, 'Necoclí', 5);
INSERT INTO `municipios` VALUES(595, 'Neira', 17);
INSERT INTO `municipios` VALUES(596, 'Neiva', 41);
INSERT INTO `municipios` VALUES(597, 'Nemocón', 25);
INSERT INTO `municipios` VALUES(598, 'Nilo', 25);
INSERT INTO `municipios` VALUES(599, 'Nimaima', 25);
INSERT INTO `municipios` VALUES(600, 'Nobsa', 15);
INSERT INTO `municipios` VALUES(601, 'Nocaima', 25);
INSERT INTO `municipios` VALUES(602, 'Norcasia', 17);
INSERT INTO `municipios` VALUES(603, 'Norosí', 13);
INSERT INTO `municipios` VALUES(604, 'Novita', 27);
INSERT INTO `municipios` VALUES(605, 'Nueva Granada', 47);
INSERT INTO `municipios` VALUES(606, 'Nuevo Colón', 15);
INSERT INTO `municipios` VALUES(607, 'Nunchía', 85);
INSERT INTO `municipios` VALUES(608, 'Nuquí', 27);
INSERT INTO `municipios` VALUES(609, 'Nátaga', 41);
INSERT INTO `municipios` VALUES(610, 'Obando', 76);
INSERT INTO `municipios` VALUES(611, 'Ocamonte', 68);
INSERT INTO `municipios` VALUES(612, 'Ocaña', 54);
INSERT INTO `municipios` VALUES(613, 'Oiba', 68);
INSERT INTO `municipios` VALUES(614, 'Oicatá', 15);
INSERT INTO `municipios` VALUES(615, 'Olaya', 5);
INSERT INTO `municipios` VALUES(616, 'Olaya Herrera', 52);
INSERT INTO `municipios` VALUES(617, 'Onzaga', 68);
INSERT INTO `municipios` VALUES(618, 'Oporapa', 41);
INSERT INTO `municipios` VALUES(619, 'Orito', 86);
INSERT INTO `municipios` VALUES(620, 'Orocué', 85);
INSERT INTO `municipios` VALUES(621, 'Ortega', 73);
INSERT INTO `municipios` VALUES(622, 'Ospina', 52);
INSERT INTO `municipios` VALUES(623, 'Otanche', 15);
INSERT INTO `municipios` VALUES(624, 'Ovejas', 70);
INSERT INTO `municipios` VALUES(625, 'Pachavita', 15);
INSERT INTO `municipios` VALUES(626, 'Pacho', 25);
INSERT INTO `municipios` VALUES(627, 'Padilla', 19);
INSERT INTO `municipios` VALUES(628, 'Paicol', 41);
INSERT INTO `municipios` VALUES(629, 'Pailitas', 20);
INSERT INTO `municipios` VALUES(630, 'Paime', 25);
INSERT INTO `municipios` VALUES(631, 'Paipa', 15);
INSERT INTO `municipios` VALUES(632, 'Pajarito', 15);
INSERT INTO `municipios` VALUES(633, 'Palermo', 41);
INSERT INTO `municipios` VALUES(634, 'Palestina', 17);
INSERT INTO `municipios` VALUES(635, 'Palestina', 41);
INSERT INTO `municipios` VALUES(636, 'Palmar', 68);
INSERT INTO `municipios` VALUES(637, 'Palmar de Varela', 8);
INSERT INTO `municipios` VALUES(638, 'Palmas del Socorro', 68);
INSERT INTO `municipios` VALUES(639, 'Palmira', 76);
INSERT INTO `municipios` VALUES(640, 'Palmito', 70);
INSERT INTO `municipios` VALUES(641, 'Palocabildo', 73);
INSERT INTO `municipios` VALUES(642, 'Pamplona', 54);
INSERT INTO `municipios` VALUES(643, 'Pamplonita', 54);
INSERT INTO `municipios` VALUES(644, 'Pandi', 25);
INSERT INTO `municipios` VALUES(645, 'Panqueba', 15);
INSERT INTO `municipios` VALUES(646, 'Paratebueno', 25);
INSERT INTO `municipios` VALUES(647, 'Pasca', 25);
INSERT INTO `municipios` VALUES(648, 'Patía (El Bordo)', 19);
INSERT INTO `municipios` VALUES(649, 'Pauna', 15);
INSERT INTO `municipios` VALUES(650, 'Paya', 15);
INSERT INTO `municipios` VALUES(651, 'Paz de Ariporo', 85);
INSERT INTO `municipios` VALUES(652, 'Paz de Río', 15);
INSERT INTO `municipios` VALUES(653, 'Pedraza', 47);
INSERT INTO `municipios` VALUES(654, 'Pelaya', 20);
INSERT INTO `municipios` VALUES(655, 'Pensilvania', 17);
INSERT INTO `municipios` VALUES(656, 'Peque', 5);
INSERT INTO `municipios` VALUES(657, 'Pereira', 66);
INSERT INTO `municipios` VALUES(658, 'Pesca', 15);
INSERT INTO `municipios` VALUES(659, 'Peñol', 5);
INSERT INTO `municipios` VALUES(660, 'Piamonte', 19);
INSERT INTO `municipios` VALUES(661, 'Pie de Cuesta', 68);
INSERT INTO `municipios` VALUES(662, 'Piedras', 73);
INSERT INTO `municipios` VALUES(663, 'Piendamó', 19);
INSERT INTO `municipios` VALUES(664, 'Pijao', 63);
INSERT INTO `municipios` VALUES(665, 'Pijiño', 47);
INSERT INTO `municipios` VALUES(666, 'Pinchote', 68);
INSERT INTO `municipios` VALUES(667, 'Pinillos', 13);
INSERT INTO `municipios` VALUES(668, 'Piojo', 8);
INSERT INTO `municipios` VALUES(669, 'Pisva', 15);
INSERT INTO `municipios` VALUES(670, 'Pital', 41);
INSERT INTO `municipios` VALUES(671, 'Pitalito', 41);
INSERT INTO `municipios` VALUES(672, 'Pivijay', 47);
INSERT INTO `municipios` VALUES(673, 'Planadas', 73);
INSERT INTO `municipios` VALUES(674, 'Planeta Rica', 23);
INSERT INTO `municipios` VALUES(675, 'Plato', 47);
INSERT INTO `municipios` VALUES(676, 'Policarpa', 52);
INSERT INTO `municipios` VALUES(677, 'Polonuevo', 8);
INSERT INTO `municipios` VALUES(678, 'Ponedera', 8);
INSERT INTO `municipios` VALUES(679, 'Popayán', 19);
INSERT INTO `municipios` VALUES(680, 'Pore', 85);
INSERT INTO `municipios` VALUES(681, 'Potosí', 52);
INSERT INTO `municipios` VALUES(682, 'Pradera', 76);
INSERT INTO `municipios` VALUES(683, 'Prado', 73);
INSERT INTO `municipios` VALUES(684, 'Providencia', 52);
INSERT INTO `municipios` VALUES(685, 'Providencia', 88);
INSERT INTO `municipios` VALUES(686, 'Pueblo Bello', 20);
INSERT INTO `municipios` VALUES(687, 'Pueblo Nuevo', 23);
INSERT INTO `municipios` VALUES(688, 'Pueblo Rico', 66);
INSERT INTO `municipios` VALUES(689, 'Pueblorrico', 5);
INSERT INTO `municipios` VALUES(690, 'Puebloviejo', 47);
INSERT INTO `municipios` VALUES(691, 'Puente Nacional', 68);
INSERT INTO `municipios` VALUES(692, 'Puerres', 52);
INSERT INTO `municipios` VALUES(693, 'Puerto Asís', 86);
INSERT INTO `municipios` VALUES(694, 'Puerto Berrío', 5);
INSERT INTO `municipios` VALUES(695, 'Puerto Boyacá', 15);
INSERT INTO `municipios` VALUES(696, 'Puerto Caicedo', 86);
INSERT INTO `municipios` VALUES(697, 'Puerto Carreño', 99);
INSERT INTO `municipios` VALUES(698, 'Puerto Colombia', 8);
INSERT INTO `municipios` VALUES(699, 'Puerto Concordia', 50);
INSERT INTO `municipios` VALUES(700, 'Puerto Escondido', 23);
INSERT INTO `municipios` VALUES(701, 'Puerto Gaitán', 50);
INSERT INTO `municipios` VALUES(702, 'Puerto Guzmán', 86);
INSERT INTO `municipios` VALUES(703, 'Puerto Leguízamo', 86);
INSERT INTO `municipios` VALUES(704, 'Puerto Libertador', 23);
INSERT INTO `municipios` VALUES(705, 'Puerto Lleras', 50);
INSERT INTO `municipios` VALUES(706, 'Puerto López', 50);
INSERT INTO `municipios` VALUES(707, 'Puerto Nare', 5);
INSERT INTO `municipios` VALUES(708, 'Puerto Nariño', 91);
INSERT INTO `municipios` VALUES(709, 'Puerto Parra', 68);
INSERT INTO `municipios` VALUES(710, 'Puerto Rico', 18);
INSERT INTO `municipios` VALUES(711, 'Puerto Rico', 50);
INSERT INTO `municipios` VALUES(712, 'Puerto Rondón', 81);
INSERT INTO `municipios` VALUES(713, 'Puerto Salgar', 25);
INSERT INTO `municipios` VALUES(714, 'Puerto Santander', 54);
INSERT INTO `municipios` VALUES(715, 'Puerto Tejada', 19);
INSERT INTO `municipios` VALUES(716, 'Puerto Triunfo', 5);
INSERT INTO `municipios` VALUES(717, 'Puerto Wilches', 68);
INSERT INTO `municipios` VALUES(718, 'Pulí', 25);
INSERT INTO `municipios` VALUES(719, 'Pupiales', 52);
INSERT INTO `municipios` VALUES(720, 'Puracé (Coconuco)', 19);
INSERT INTO `municipios` VALUES(721, 'Purificación', 73);
INSERT INTO `municipios` VALUES(722, 'Purísima', 23);
INSERT INTO `municipios` VALUES(723, 'Pácora', 17);
INSERT INTO `municipios` VALUES(724, 'Páez', 15);
INSERT INTO `municipios` VALUES(725, 'Páez (Belalcazar)', 19);
INSERT INTO `municipios` VALUES(726, 'Páramo', 68);
INSERT INTO `municipios` VALUES(727, 'Quebradanegra', 25);
INSERT INTO `municipios` VALUES(728, 'Quetame', 25);
INSERT INTO `municipios` VALUES(729, 'Quibdó', 27);
INSERT INTO `municipios` VALUES(730, 'Quimbaya', 63);
INSERT INTO `municipios` VALUES(731, 'Quinchía', 66);
INSERT INTO `municipios` VALUES(732, 'Quipama', 15);
INSERT INTO `municipios` VALUES(733, 'Quipile', 25);
INSERT INTO `municipios` VALUES(734, 'Ragonvalia', 54);
INSERT INTO `municipios` VALUES(735, 'Ramiriquí', 15);
INSERT INTO `municipios` VALUES(736, 'Recetor', 85);
INSERT INTO `municipios` VALUES(737, 'Regidor', 13);
INSERT INTO `municipios` VALUES(738, 'Remedios', 5);
INSERT INTO `municipios` VALUES(739, 'Remolino', 47);
INSERT INTO `municipios` VALUES(740, 'Repelón', 8);
INSERT INTO `municipios` VALUES(741, 'Restrepo', 50);
INSERT INTO `municipios` VALUES(742, 'Restrepo', 76);
INSERT INTO `municipios` VALUES(743, 'Retiro', 5);
INSERT INTO `municipios` VALUES(744, 'Ricaurte', 25);
INSERT INTO `municipios` VALUES(745, 'Ricaurte', 52);
INSERT INTO `municipios` VALUES(746, 'Rio Negro', 68);
INSERT INTO `municipios` VALUES(747, 'Rioblanco', 73);
INSERT INTO `municipios` VALUES(748, 'Riofrío', 76);
INSERT INTO `municipios` VALUES(749, 'Riohacha', 44);
INSERT INTO `municipios` VALUES(750, 'Risaralda', 17);
INSERT INTO `municipios` VALUES(751, 'Rivera', 41);
INSERT INTO `municipios` VALUES(752, 'Roberto Payán (San José)', 52);
INSERT INTO `municipios` VALUES(753, 'Roldanillo', 76);
INSERT INTO `municipios` VALUES(754, 'Roncesvalles', 73);
INSERT INTO `municipios` VALUES(755, 'Rondón', 15);
INSERT INTO `municipios` VALUES(756, 'Rosas', 19);
INSERT INTO `municipios` VALUES(757, 'Rovira', 73);
INSERT INTO `municipios` VALUES(758, 'Ráquira', 15);
INSERT INTO `municipios` VALUES(759, 'Río Iró', 27);
INSERT INTO `municipios` VALUES(760, 'Río Quito', 27);
INSERT INTO `municipios` VALUES(761, 'Río Sucio', 17);
INSERT INTO `municipios` VALUES(762, 'Río Viejo', 13);
INSERT INTO `municipios` VALUES(763, 'Río de oro', 20);
INSERT INTO `municipios` VALUES(764, 'Ríonegro', 5);
INSERT INTO `municipios` VALUES(765, 'Ríosucio', 27);
INSERT INTO `municipios` VALUES(766, 'Sabana de Torres', 68);
INSERT INTO `municipios` VALUES(767, 'Sabanagrande', 8);
INSERT INTO `municipios` VALUES(768, 'Sabanalarga', 5);
INSERT INTO `municipios` VALUES(769, 'Sabanalarga', 8);
INSERT INTO `municipios` VALUES(770, 'Sabanalarga', 85);
INSERT INTO `municipios` VALUES(771, 'Sabanas de San Angel (SAN ANGEL)', 47);
INSERT INTO `municipios` VALUES(772, 'Sabaneta', 5);
INSERT INTO `municipios` VALUES(773, 'Saboyá', 15);
INSERT INTO `municipios` VALUES(774, 'Sahagún', 23);
INSERT INTO `municipios` VALUES(775, 'Saladoblanco', 41);
INSERT INTO `municipios` VALUES(776, 'Salamina', 17);
INSERT INTO `municipios` VALUES(777, 'Salamina', 47);
INSERT INTO `municipios` VALUES(778, 'Salazar', 54);
INSERT INTO `municipios` VALUES(779, 'Saldaña', 73);
INSERT INTO `municipios` VALUES(780, 'Salento', 63);
INSERT INTO `municipios` VALUES(781, 'Salgar', 5);
INSERT INTO `municipios` VALUES(782, 'Samacá', 15);
INSERT INTO `municipios` VALUES(783, 'Samaniego', 52);
INSERT INTO `municipios` VALUES(784, 'Samaná', 17);
INSERT INTO `municipios` VALUES(785, 'Sampués', 70);
INSERT INTO `municipios` VALUES(786, 'San Agustín', 41);
INSERT INTO `municipios` VALUES(787, 'San Alberto', 20);
INSERT INTO `municipios` VALUES(788, 'San Andrés', 68);
INSERT INTO `municipios` VALUES(789, 'San Andrés Sotavento', 23);
INSERT INTO `municipios` VALUES(790, 'San Andrés de Cuerquía', 5);
INSERT INTO `municipios` VALUES(791, 'San Antero', 23);
INSERT INTO `municipios` VALUES(792, 'San Antonio', 73);
INSERT INTO `municipios` VALUES(793, 'San Antonio de Tequendama', 25);
INSERT INTO `municipios` VALUES(794, 'San Benito', 68);
INSERT INTO `municipios` VALUES(795, 'San Benito Abad', 70);
INSERT INTO `municipios` VALUES(796, 'San Bernardo', 25);
INSERT INTO `municipios` VALUES(797, 'San Bernardo', 52);
INSERT INTO `municipios` VALUES(798, 'San Bernardo del Viento', 23);
INSERT INTO `municipios` VALUES(799, 'San Calixto', 54);
INSERT INTO `municipios` VALUES(800, 'San Carlos', 5);
INSERT INTO `municipios` VALUES(801, 'San Carlos', 23);
INSERT INTO `municipios` VALUES(802, 'San Carlos de Guaroa', 50);
INSERT INTO `municipios` VALUES(803, 'San Cayetano', 25);
INSERT INTO `municipios` VALUES(804, 'San Cayetano', 54);
INSERT INTO `municipios` VALUES(805, 'San Cristobal', 13);
INSERT INTO `municipios` VALUES(806, 'San Diego', 20);
INSERT INTO `municipios` VALUES(807, 'San Eduardo', 15);
INSERT INTO `municipios` VALUES(808, 'San Estanislao', 13);
INSERT INTO `municipios` VALUES(809, 'San Fernando', 13);
INSERT INTO `municipios` VALUES(810, 'San Francisco', 5);
INSERT INTO `municipios` VALUES(811, 'San Francisco', 25);
INSERT INTO `municipios` VALUES(812, 'San Francisco', 86);
INSERT INTO `municipios` VALUES(813, 'San Gíl', 68);
INSERT INTO `municipios` VALUES(814, 'San Jacinto', 13);
INSERT INTO `municipios` VALUES(815, 'San Jacinto del Cauca', 13);
INSERT INTO `municipios` VALUES(816, 'San Jerónimo', 5);
INSERT INTO `municipios` VALUES(817, 'San Joaquín', 68);
INSERT INTO `municipios` VALUES(818, 'San José', 17);
INSERT INTO `municipios` VALUES(819, 'San José de Miranda', 68);
INSERT INTO `municipios` VALUES(820, 'San José de Montaña', 5);
INSERT INTO `municipios` VALUES(821, 'San José de Pare', 15);
INSERT INTO `municipios` VALUES(822, 'San José de Uré', 23);
INSERT INTO `municipios` VALUES(823, 'San José del Fragua', 18);
INSERT INTO `municipios` VALUES(824, 'San José del Guaviare', 95);
INSERT INTO `municipios` VALUES(825, 'San José del Palmar', 27);
INSERT INTO `municipios` VALUES(826, 'San Juan de Arama', 50);
INSERT INTO `municipios` VALUES(827, 'San Juan de Betulia', 70);
INSERT INTO `municipios` VALUES(828, 'San Juan de Nepomuceno', 13);
INSERT INTO `municipios` VALUES(829, 'San Juan de Pasto', 52);
INSERT INTO `municipios` VALUES(830, 'San Juan de Río Seco', 25);
INSERT INTO `municipios` VALUES(831, 'San Juan de Urabá', 5);
INSERT INTO `municipios` VALUES(832, 'San Juan del Cesar', 44);
INSERT INTO `municipios` VALUES(833, 'San Juanito', 50);
INSERT INTO `municipios` VALUES(834, 'San Lorenzo', 52);
INSERT INTO `municipios` VALUES(835, 'San Luis', 73);
INSERT INTO `municipios` VALUES(836, 'San Luís', 5);
INSERT INTO `municipios` VALUES(837, 'San Luís de Gaceno', 15);
INSERT INTO `municipios` VALUES(838, 'San Luís de Palenque', 85);
INSERT INTO `municipios` VALUES(839, 'San Marcos', 70);
INSERT INTO `municipios` VALUES(840, 'San Martín', 20);
INSERT INTO `municipios` VALUES(841, 'San Martín', 50);
INSERT INTO `municipios` VALUES(842, 'San Martín de Loba', 13);
INSERT INTO `municipios` VALUES(843, 'San Mateo', 15);
INSERT INTO `municipios` VALUES(844, 'San Miguel', 68);
INSERT INTO `municipios` VALUES(845, 'San Miguel', 86);
INSERT INTO `municipios` VALUES(846, 'San Miguel de Sema', 15);
INSERT INTO `municipios` VALUES(847, 'San Onofre', 70);
INSERT INTO `municipios` VALUES(848, 'San Pablo', 13);
INSERT INTO `municipios` VALUES(849, 'San Pablo', 52);
INSERT INTO `municipios` VALUES(850, 'San Pablo de Borbur', 15);
INSERT INTO `municipios` VALUES(851, 'San Pedro', 5);
INSERT INTO `municipios` VALUES(852, 'San Pedro', 70);
INSERT INTO `municipios` VALUES(853, 'San Pedro', 76);
INSERT INTO `municipios` VALUES(854, 'San Pedro de Cartago', 52);
INSERT INTO `municipios` VALUES(855, 'San Pedro de Urabá', 5);
INSERT INTO `municipios` VALUES(856, 'San Pelayo', 23);
INSERT INTO `municipios` VALUES(857, 'San Rafael', 5);
INSERT INTO `municipios` VALUES(858, 'San Roque', 5);
INSERT INTO `municipios` VALUES(859, 'San Sebastián', 19);
INSERT INTO `municipios` VALUES(860, 'San Sebastián de Buenavista', 47);
INSERT INTO `municipios` VALUES(861, 'San Vicente', 5);
INSERT INTO `municipios` VALUES(862, 'San Vicente del Caguán', 18);
INSERT INTO `municipios` VALUES(863, 'San Vicente del Chucurí', 68);
INSERT INTO `municipios` VALUES(864, 'San Zenón', 47);
INSERT INTO `municipios` VALUES(865, 'Sandoná', 52);
INSERT INTO `municipios` VALUES(866, 'Santa Ana', 47);
INSERT INTO `municipios` VALUES(867, 'Santa Bárbara', 5);
INSERT INTO `municipios` VALUES(868, 'Santa Bárbara', 68);
INSERT INTO `municipios` VALUES(869, 'Santa Bárbara (Iscuandé)', 52);
INSERT INTO `municipios` VALUES(870, 'Santa Bárbara de Pinto', 47);
INSERT INTO `municipios` VALUES(871, 'Santa Catalina', 13);
INSERT INTO `municipios` VALUES(872, 'Santa Fé de Antioquia', 5);
INSERT INTO `municipios` VALUES(873, 'Santa Genoveva de Docorodó', 27);
INSERT INTO `municipios` VALUES(874, 'Santa Helena del Opón', 68);
INSERT INTO `municipios` VALUES(875, 'Santa Isabel', 73);
INSERT INTO `municipios` VALUES(876, 'Santa Lucía', 8);
INSERT INTO `municipios` VALUES(877, 'Santa Marta', 47);
INSERT INTO `municipios` VALUES(878, 'Santa María', 15);
INSERT INTO `municipios` VALUES(879, 'Santa María', 41);
INSERT INTO `municipios` VALUES(880, 'Santa Rosa', 13);
INSERT INTO `municipios` VALUES(881, 'Santa Rosa', 19);
INSERT INTO `municipios` VALUES(882, 'Santa Rosa de Cabal', 66);
INSERT INTO `municipios` VALUES(883, 'Santa Rosa de Osos', 5);
INSERT INTO `municipios` VALUES(884, 'Santa Rosa de Viterbo', 15);
INSERT INTO `municipios` VALUES(885, 'Santa Rosa del Sur', 13);
INSERT INTO `municipios` VALUES(886, 'Santa Rosalía', 99);
INSERT INTO `municipios` VALUES(887, 'Santa Sofía', 15);
INSERT INTO `municipios` VALUES(888, 'Santana', 15);
INSERT INTO `municipios` VALUES(889, 'Santander de Quilichao', 19);
INSERT INTO `municipios` VALUES(890, 'Santiago', 54);
INSERT INTO `municipios` VALUES(891, 'Santiago', 86);
INSERT INTO `municipios` VALUES(892, 'Santo Domingo', 5);
INSERT INTO `municipios` VALUES(893, 'Santo Tomás', 8);
INSERT INTO `municipios` VALUES(894, 'Santuario', 5);
INSERT INTO `municipios` VALUES(895, 'Santuario', 66);
INSERT INTO `municipios` VALUES(896, 'Sapuyes', 52);
INSERT INTO `municipios` VALUES(897, 'Saravena', 81);
INSERT INTO `municipios` VALUES(898, 'Sardinata', 54);
INSERT INTO `municipios` VALUES(899, 'Sasaima', 25);
INSERT INTO `municipios` VALUES(900, 'Sativanorte', 15);
INSERT INTO `municipios` VALUES(901, 'Sativasur', 15);
INSERT INTO `municipios` VALUES(902, 'Segovia', 5);
INSERT INTO `municipios` VALUES(903, 'Sesquilé', 25);
INSERT INTO `municipios` VALUES(904, 'Sevilla', 76);
INSERT INTO `municipios` VALUES(905, 'Siachoque', 15);
INSERT INTO `municipios` VALUES(906, 'Sibaté', 25);
INSERT INTO `municipios` VALUES(907, 'Sibundoy', 86);
INSERT INTO `municipios` VALUES(908, 'Silos', 54);
INSERT INTO `municipios` VALUES(909, 'Silvania', 25);
INSERT INTO `municipios` VALUES(910, 'Silvia', 19);
INSERT INTO `municipios` VALUES(911, 'Simacota', 68);
INSERT INTO `municipios` VALUES(912, 'Simijaca', 25);
INSERT INTO `municipios` VALUES(913, 'Simití', 13);
INSERT INTO `municipios` VALUES(914, 'Sincelejo', 70);
INSERT INTO `municipios` VALUES(915, 'Sincé', 70);
INSERT INTO `municipios` VALUES(916, 'Sipí', 27);
INSERT INTO `municipios` VALUES(917, 'Sitionuevo', 47);
INSERT INTO `municipios` VALUES(918, 'Soacha', 25);
INSERT INTO `municipios` VALUES(919, 'Soatá', 15);
INSERT INTO `municipios` VALUES(920, 'Socha', 15);
INSERT INTO `municipios` VALUES(921, 'Socorro', 68);
INSERT INTO `municipios` VALUES(922, 'Socotá', 15);
INSERT INTO `municipios` VALUES(923, 'Sogamoso', 15);
INSERT INTO `municipios` VALUES(924, 'Solano', 18);
INSERT INTO `municipios` VALUES(925, 'Soledad', 8);
INSERT INTO `municipios` VALUES(926, 'Solita', 18);
INSERT INTO `municipios` VALUES(927, 'Somondoco', 15);
INSERT INTO `municipios` VALUES(928, 'Sonsón', 5);
INSERT INTO `municipios` VALUES(929, 'Sopetrán', 5);
INSERT INTO `municipios` VALUES(930, 'Soplaviento', 13);
INSERT INTO `municipios` VALUES(931, 'Sopó', 25);
INSERT INTO `municipios` VALUES(932, 'Sora', 15);
INSERT INTO `municipios` VALUES(933, 'Soracá', 15);
INSERT INTO `municipios` VALUES(934, 'Sotaquirá', 15);
INSERT INTO `municipios` VALUES(935, 'Sotara (Paispamba)', 19);
INSERT INTO `municipios` VALUES(936, 'Sotomayor (Los Andes)', 52);
INSERT INTO `municipios` VALUES(937, 'Suaita', 68);
INSERT INTO `municipios` VALUES(938, 'Suan', 8);
INSERT INTO `municipios` VALUES(939, 'Suaza', 41);
INSERT INTO `municipios` VALUES(940, 'Subachoque', 25);
INSERT INTO `municipios` VALUES(941, 'Sucre', 19);
INSERT INTO `municipios` VALUES(942, 'Sucre', 68);
INSERT INTO `municipios` VALUES(943, 'Sucre', 70);
INSERT INTO `municipios` VALUES(944, 'Suesca', 25);
INSERT INTO `municipios` VALUES(945, 'Supatá', 25);
INSERT INTO `municipios` VALUES(946, 'Supía', 17);
INSERT INTO `municipios` VALUES(947, 'Suratá', 68);
INSERT INTO `municipios` VALUES(948, 'Susa', 25);
INSERT INTO `municipios` VALUES(949, 'Susacón', 15);
INSERT INTO `municipios` VALUES(950, 'Sutamarchán', 15);
INSERT INTO `municipios` VALUES(951, 'Sutatausa', 25);
INSERT INTO `municipios` VALUES(952, 'Sutatenza', 15);
INSERT INTO `municipios` VALUES(953, 'Suárez', 19);
INSERT INTO `municipios` VALUES(954, 'Suárez', 73);
INSERT INTO `municipios` VALUES(955, 'Sácama', 85);
INSERT INTO `municipios` VALUES(956, 'Sáchica', 15);
INSERT INTO `municipios` VALUES(957, 'Tabio', 25);
INSERT INTO `municipios` VALUES(958, 'Tadó', 27);
INSERT INTO `municipios` VALUES(959, 'Talaigua Nuevo', 13);
INSERT INTO `municipios` VALUES(960, 'Tamalameque', 20);
INSERT INTO `municipios` VALUES(961, 'Tame', 81);
INSERT INTO `municipios` VALUES(962, 'Taminango', 52);
INSERT INTO `municipios` VALUES(963, 'Tangua', 52);
INSERT INTO `municipios` VALUES(964, 'Taraira', 97);
INSERT INTO `municipios` VALUES(965, 'Tarazá', 5);
INSERT INTO `municipios` VALUES(966, 'Tarqui', 41);
INSERT INTO `municipios` VALUES(967, 'Tarso', 5);
INSERT INTO `municipios` VALUES(968, 'Tasco', 15);
INSERT INTO `municipios` VALUES(969, 'Tauramena', 85);
INSERT INTO `municipios` VALUES(970, 'Tausa', 25);
INSERT INTO `municipios` VALUES(971, 'Tello', 41);
INSERT INTO `municipios` VALUES(972, 'Tena', 25);
INSERT INTO `municipios` VALUES(973, 'Tenerife', 47);
INSERT INTO `municipios` VALUES(974, 'Tenjo', 25);
INSERT INTO `municipios` VALUES(975, 'Tenza', 15);
INSERT INTO `municipios` VALUES(976, 'Teorama', 54);
INSERT INTO `municipios` VALUES(977, 'Teruel', 41);
INSERT INTO `municipios` VALUES(978, 'Tesalia', 41);
INSERT INTO `municipios` VALUES(979, 'Tibacuy', 25);
INSERT INTO `municipios` VALUES(980, 'Tibaná', 15);
INSERT INTO `municipios` VALUES(981, 'Tibasosa', 15);
INSERT INTO `municipios` VALUES(982, 'Tibirita', 25);
INSERT INTO `municipios` VALUES(983, 'Tibú', 54);
INSERT INTO `municipios` VALUES(984, 'Tierralta', 23);
INSERT INTO `municipios` VALUES(985, 'Timaná', 41);
INSERT INTO `municipios` VALUES(986, 'Timbiquí', 19);
INSERT INTO `municipios` VALUES(987, 'Timbío', 19);
INSERT INTO `municipios` VALUES(988, 'Tinjacá', 15);
INSERT INTO `municipios` VALUES(989, 'Tipacoque', 15);
INSERT INTO `municipios` VALUES(990, 'Tiquisio (Puerto Rico)', 13);
INSERT INTO `municipios` VALUES(991, 'Titiribí', 5);
INSERT INTO `municipios` VALUES(992, 'Toca', 15);
INSERT INTO `municipios` VALUES(993, 'Tocaima', 25);
INSERT INTO `municipios` VALUES(994, 'Tocancipá', 25);
INSERT INTO `municipios` VALUES(995, 'Toguí', 15);
INSERT INTO `municipios` VALUES(996, 'Toledo', 5);
INSERT INTO `municipios` VALUES(997, 'Toledo', 54);
INSERT INTO `municipios` VALUES(998, 'Tolú', 70);
INSERT INTO `municipios` VALUES(999, 'Tolú Viejo', 70);
INSERT INTO `municipios` VALUES(1000, 'Tona', 68);
INSERT INTO `municipios` VALUES(1001, 'Topagá', 15);
INSERT INTO `municipios` VALUES(1002, 'Topaipí', 25);
INSERT INTO `municipios` VALUES(1003, 'Toribío', 19);
INSERT INTO `municipios` VALUES(1004, 'Toro', 76);
INSERT INTO `municipios` VALUES(1005, 'Tota', 15);
INSERT INTO `municipios` VALUES(1006, 'Totoró', 19);
INSERT INTO `municipios` VALUES(1007, 'Trinidad', 85);
INSERT INTO `municipios` VALUES(1008, 'Trujillo', 76);
INSERT INTO `municipios` VALUES(1009, 'Tubará', 8);
INSERT INTO `municipios` VALUES(1010, 'Tuchín', 23);
INSERT INTO `municipios` VALUES(1011, 'Tulúa', 76);
INSERT INTO `municipios` VALUES(1012, 'Tumaco', 52);
INSERT INTO `municipios` VALUES(1013, 'Tunja', 15);
INSERT INTO `municipios` VALUES(1014, 'Tunungua', 15);
INSERT INTO `municipios` VALUES(1015, 'Turbaco', 13);
INSERT INTO `municipios` VALUES(1016, 'Turbaná', 13);
INSERT INTO `municipios` VALUES(1017, 'Turbo', 5);
INSERT INTO `municipios` VALUES(1018, 'Turmequé', 15);
INSERT INTO `municipios` VALUES(1019, 'Tuta', 15);
INSERT INTO `municipios` VALUES(1020, 'Tutasá', 15);
INSERT INTO `municipios` VALUES(1021, 'Támara', 85);
INSERT INTO `municipios` VALUES(1022, 'Támesis', 5);
INSERT INTO `municipios` VALUES(1023, 'Túquerres', 52);
INSERT INTO `municipios` VALUES(1024, 'Ubalá', 25);
INSERT INTO `municipios` VALUES(1025, 'Ubaque', 25);
INSERT INTO `municipios` VALUES(1026, 'Ubaté', 25);
INSERT INTO `municipios` VALUES(1027, 'Ulloa', 76);
INSERT INTO `municipios` VALUES(1028, 'Une', 25);
INSERT INTO `municipios` VALUES(1029, 'Unguía', 27);
INSERT INTO `municipios` VALUES(1030, 'Unión Panamericana (ÁNIMAS)', 27);
INSERT INTO `municipios` VALUES(1031, 'Uramita', 5);
INSERT INTO `municipios` VALUES(1032, 'Uribe', 50);
INSERT INTO `municipios` VALUES(1033, 'Uribia', 44);
INSERT INTO `municipios` VALUES(1034, 'Urrao', 5);
INSERT INTO `municipios` VALUES(1035, 'Urumita', 44);
INSERT INTO `municipios` VALUES(1036, 'Usiacuri', 8);
INSERT INTO `municipios` VALUES(1037, 'Valdivia', 5);
INSERT INTO `municipios` VALUES(1038, 'Valencia', 23);
INSERT INTO `municipios` VALUES(1039, 'Valle de San José', 68);
INSERT INTO `municipios` VALUES(1040, 'Valle de San Juan', 73);
INSERT INTO `municipios` VALUES(1041, 'Valle del Guamuez', 86);
INSERT INTO `municipios` VALUES(1042, 'Valledupar', 20);
INSERT INTO `municipios` VALUES(1043, 'Valparaiso', 5);
INSERT INTO `municipios` VALUES(1044, 'Valparaiso', 18);
INSERT INTO `municipios` VALUES(1045, 'Vegachí', 5);
INSERT INTO `municipios` VALUES(1046, 'Venadillo', 73);
INSERT INTO `municipios` VALUES(1047, 'Venecia', 5);
INSERT INTO `municipios` VALUES(1048, 'Venecia (Ospina Pérez)', 25);
INSERT INTO `municipios` VALUES(1049, 'Ventaquemada', 15);
INSERT INTO `municipios` VALUES(1050, 'Vergara', 25);
INSERT INTO `municipios` VALUES(1051, 'Versalles', 76);
INSERT INTO `municipios` VALUES(1052, 'Vetas', 68);
INSERT INTO `municipios` VALUES(1053, 'Viani', 25);
INSERT INTO `municipios` VALUES(1054, 'Vigía del Fuerte', 5);
INSERT INTO `municipios` VALUES(1055, 'Vijes', 76);
INSERT INTO `municipios` VALUES(1056, 'Villa Caro', 54);
INSERT INTO `municipios` VALUES(1057, 'Villa Rica', 19);
INSERT INTO `municipios` VALUES(1058, 'Villa de Leiva', 15);
INSERT INTO `municipios` VALUES(1059, 'Villa del Rosario', 54);
INSERT INTO `municipios` VALUES(1060, 'Villagarzón', 86);
INSERT INTO `municipios` VALUES(1061, 'Villagómez', 25);
INSERT INTO `municipios` VALUES(1062, 'Villahermosa', 73);
INSERT INTO `municipios` VALUES(1063, 'Villamaría', 17);
INSERT INTO `municipios` VALUES(1064, 'Villanueva', 13);
INSERT INTO `municipios` VALUES(1065, 'Villanueva', 44);
INSERT INTO `municipios` VALUES(1066, 'Villanueva', 68);
INSERT INTO `municipios` VALUES(1067, 'Villanueva', 85);
INSERT INTO `municipios` VALUES(1068, 'Villapinzón', 25);
INSERT INTO `municipios` VALUES(1069, 'Villarrica', 73);
INSERT INTO `municipios` VALUES(1070, 'Villavicencio', 50);
INSERT INTO `municipios` VALUES(1071, 'Villavieja', 41);
INSERT INTO `municipios` VALUES(1072, 'Villeta', 25);
INSERT INTO `municipios` VALUES(1073, 'Viotá', 25);
INSERT INTO `municipios` VALUES(1074, 'Viracachá', 15);
INSERT INTO `municipios` VALUES(1075, 'Vista Hermosa', 50);
INSERT INTO `municipios` VALUES(1076, 'Viterbo', 17);
INSERT INTO `municipios` VALUES(1077, 'Vélez', 68);
INSERT INTO `municipios` VALUES(1078, 'Yacopí', 25);
INSERT INTO `municipios` VALUES(1079, 'Yacuanquer', 52);
INSERT INTO `municipios` VALUES(1080, 'Yaguará', 41);
INSERT INTO `municipios` VALUES(1081, 'Yalí', 5);
INSERT INTO `municipios` VALUES(1082, 'Yarumal', 5);
INSERT INTO `municipios` VALUES(1083, 'Yolombó', 5);
INSERT INTO `municipios` VALUES(1084, 'Yondó (Casabe)', 5);
INSERT INTO `municipios` VALUES(1085, 'Yopal', 85);
INSERT INTO `municipios` VALUES(1086, 'Yotoco', 76);
INSERT INTO `municipios` VALUES(1087, 'Yumbo', 76);
INSERT INTO `municipios` VALUES(1088, 'Zambrano', 13);
INSERT INTO `municipios` VALUES(1089, 'Zapatoca', 68);
INSERT INTO `municipios` VALUES(1090, 'Zapayán (PUNTA DE PIEDRAS)', 47);
INSERT INTO `municipios` VALUES(1091, 'Zaragoza', 5);
INSERT INTO `municipios` VALUES(1092, 'Zarzal', 76);
INSERT INTO `municipios` VALUES(1093, 'Zetaquirá', 15);
INSERT INTO `municipios` VALUES(1094, 'Zipacón', 25);
INSERT INTO `municipios` VALUES(1095, 'Zipaquirá', 25);
INSERT INTO `municipios` VALUES(1096, 'Zona Bananera (PRADO - SEVILLA)', 47);
INSERT INTO `municipios` VALUES(1097, 'Ábrego', 54);
INSERT INTO `municipios` VALUES(1098, 'Íquira', 41);
INSERT INTO `municipios` VALUES(1099, 'Úmbita', 15);
INSERT INTO `municipios` VALUES(1100, 'Útica', 25);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paquete`
--

CREATE TABLE `paquete` (
  `codigo` varchar(15) NOT NULL,
  `descripcion` varchar(150) NOT NULL,
  `peso_kg` double NOT NULL,
  `cod_remitente` varchar(12) NOT NULL,
  `cod_destinatario` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `paquete`
--

INSERT INTO `paquete` VALUES('7649762064', 'una caja de contiene materiales de oficina', 80, '110244567', '110012');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `poblacion`
--

CREATE TABLE `poblacion` (
  `codigo` varchar(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `codigo_provincia` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `poblacion`
--

INSERT INTO `poblacion` VALUES('9001', 'caucasia', '23');
INSERT INTO `poblacion` VALUES('9002', 'puerto berrio', '20');
INSERT INTO `poblacion` VALUES('9003', 'segovia', '21');
INSERT INTO `poblacion` VALUES('9004', 'santa rosa de osos', '22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provincia`
--

CREATE TABLE `provincia` (
  `codigo` varchar(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `codigo_depto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `provincia`
--

INSERT INTO `provincia` VALUES('20', 'magdalena medio', 5);
INSERT INTO `provincia` VALUES('21', 'Nordeste', 5);
INSERT INTO `provincia` VALUES('22', 'Norte', 5);
INSERT INTO `provincia` VALUES('23', 'bajo cauca', 5);
INSERT INTO `provincia` VALUES('24', 'oriente', 5);
INSERT INTO `provincia` VALUES('25', 'Suroeste', 5);
INSERT INTO `provincia` VALUES('26', 'occidente', 5);
INSERT INTO `provincia` VALUES('27', 'uraba', 5);
INSERT INTO `provincia` VALUES('28', 'valle de aburra', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `remitente`
--

CREATE TABLE `remitente` (
  `documento` varchar(12) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `teléfono` varchar(10) NOT NULL,
  `direccion_remitente` varchar(50) DEFAULT NULL,
  `ciudad` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `remitente`
--

INSERT INTO `remitente` VALUES('110244567', 'luis miguel', 'garcia moreno', '312445123', 'barrio la esperanza', '914');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ruta_entrega_paquete`
--

CREATE TABLE `ruta_entrega_paquete` (
  `id_ruta` int(11) NOT NULL,
  `doc_camionero` varchar(12) NOT NULL,
  `matricula_camion` varchar(11) NOT NULL,
  `fec_ini_entrega` datetime NOT NULL,
  `fec_fin_entrega` datetime NOT NULL,
  `estado` varchar(10) NOT NULL DEFAULT '1' COMMENT '(0) entregado - (1) no entregado',
  `ciudad` int(11) NOT NULL,
  `envio_ruta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ruta_entrega_paquete`
--

INSERT INTO `ruta_entrega_paquete` VALUES(2147483647, '3445', 'ijq24d', '2021-02-08 18:32:50', '2021-12-02 18:32:50', 'salida', 244, 2147483647);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `camion`
--
ALTER TABLE `camion`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `doc_camionero` (`doc_camionero`),
  ADD KEY `registro_matricula` (`registro_matricula`);

--
-- Indices de la tabla `camionero`
--
ALTER TABLE `camionero`
  ADD PRIMARY KEY (`documento`),
  ADD KEY `camionero_ibfk_1` (`ciudad`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `destinatario`
--
ALTER TABLE `destinatario`
  ADD PRIMARY KEY (`documento`),
  ADD KEY `ciudad` (`ciudad`);

--
-- Indices de la tabla `envio`
--
ALTER TABLE `envio`
  ADD PRIMARY KEY (`id_envio`),
  ADD KEY `envio_camionero` (`envio_camionero`),
  ADD KEY `envio_destinatario` (`envio_destinatario`),
  ADD KEY `envio_ibfk_3` (`id_paquete`),
  ADD KEY `envio_remitente` (`envio_remitente`);

--
-- Indices de la tabla `municipios`
--
ALTER TABLE `municipios`
  ADD PRIMARY KEY (`id_municipio`),
  ADD KEY `departamento_id` (`departamento_id`);

--
-- Indices de la tabla `paquete`
--
ALTER TABLE `paquete`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `cod_destinatario` (`cod_destinatario`),
  ADD KEY `cod_remitente` (`cod_remitente`);

--
-- Indices de la tabla `poblacion`
--
ALTER TABLE `poblacion`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `codigo_provincia` (`codigo_provincia`);

--
-- Indices de la tabla `provincia`
--
ALTER TABLE `provincia`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `codigo_depto` (`codigo_depto`);

--
-- Indices de la tabla `remitente`
--
ALTER TABLE `remitente`
  ADD PRIMARY KEY (`documento`);

--
-- Indices de la tabla `ruta_entrega_paquete`
--
ALTER TABLE `ruta_entrega_paquete`
  ADD PRIMARY KEY (`id_ruta`),
  ADD KEY `matricula_camion` (`matricula_camion`),
  ADD KEY `ciudad` (`ciudad`),
  ADD KEY `envio_ruta` (`envio_ruta`),
  ADD KEY `ruta_entrega_paquete_ibfk_1` (`doc_camionero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT de la tabla `envio`
--
ALTER TABLE `envio`
  MODIFY `id_envio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT de la tabla `municipios`
--
ALTER TABLE `municipios`
  MODIFY `id_municipio` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1101;

--
-- AUTO_INCREMENT de la tabla `ruta_entrega_paquete`
--
ALTER TABLE `ruta_entrega_paquete`
  MODIFY `id_ruta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `camion`
--
ALTER TABLE `camion`
  ADD CONSTRAINT `camion_ibfk_1` FOREIGN KEY (`doc_camionero`) REFERENCES `camionero` (`documento`),
  ADD CONSTRAINT `camion_ibfk_2` FOREIGN KEY (`registro_matricula`) REFERENCES `municipios` (`id_municipio`);

--
-- Filtros para la tabla `camionero`
--
ALTER TABLE `camionero`
  ADD CONSTRAINT `camionero_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `municipios` (`id_municipio`);

--
-- Filtros para la tabla `destinatario`
--
ALTER TABLE `destinatario`
  ADD CONSTRAINT `destinatario_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `municipios` (`id_municipio`);

--
-- Filtros para la tabla `envio`
--
ALTER TABLE `envio`
  ADD CONSTRAINT `envio_ibfk_1` FOREIGN KEY (`envio_camionero`) REFERENCES `camionero` (`documento`),
  ADD CONSTRAINT `envio_ibfk_2` FOREIGN KEY (`envio_destinatario`) REFERENCES `destinatario` (`documento`),
  ADD CONSTRAINT `envio_ibfk_3` FOREIGN KEY (`id_paquete`) REFERENCES `paquete` (`codigo`),
  ADD CONSTRAINT `envio_ibfk_4` FOREIGN KEY (`envio_remitente`) REFERENCES `remitente` (`documento`);

--
-- Filtros para la tabla `municipios`
--
ALTER TABLE `municipios`
  ADD CONSTRAINT `municipios_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`codigo`);

--
-- Filtros para la tabla `paquete`
--
ALTER TABLE `paquete`
  ADD CONSTRAINT `paquete_ibfk_2` FOREIGN KEY (`cod_destinatario`) REFERENCES `destinatario` (`documento`),
  ADD CONSTRAINT `paquete_ibfk_3` FOREIGN KEY (`cod_remitente`) REFERENCES `remitente` (`documento`);

--
-- Filtros para la tabla `poblacion`
--
ALTER TABLE `poblacion`
  ADD CONSTRAINT `poblacion_ibfk_1` FOREIGN KEY (`codigo_provincia`) REFERENCES `provincia` (`codigo`);

--
-- Filtros para la tabla `provincia`
--
ALTER TABLE `provincia`
  ADD CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`codigo_depto`) REFERENCES `departamento` (`codigo`);

--
-- Filtros para la tabla `ruta_entrega_paquete`
--
ALTER TABLE `ruta_entrega_paquete`
  ADD CONSTRAINT `ruta_entrega_paquete_ibfk_1` FOREIGN KEY (`doc_camionero`) REFERENCES `camionero` (`documento`),
  ADD CONSTRAINT `ruta_entrega_paquete_ibfk_2` FOREIGN KEY (`matricula_camion`) REFERENCES `camion` (`matricula`),
  ADD CONSTRAINT `ruta_entrega_paquete_ibfk_3` FOREIGN KEY (`ciudad`) REFERENCES `municipios` (`id_municipio`),
  ADD CONSTRAINT `ruta_entrega_paquete_ibfk_4` FOREIGN KEY (`envio_ruta`) REFERENCES `envio` (`id_envio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
