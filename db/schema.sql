-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 27-10-2021 a las 12:40:26
-- Versión del servidor: 10.3.31-MariaDB-0ubuntu0.20.04.1
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo38`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `colors`
--

CREATE TABLE `colors` (
  `id` int(11) NOT NULL,
  `value` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `colors`
--

INSERT INTO `colors` (`id`, `value`) VALUES
(1, 'Royal Blue'),
(2, 'Snow'),
(3, 'Salmon'),
(4, 'Azure'),
(5, 'DarkOliveGreen'),
(6, 'DeepPink'),
(7, 'Gold'),
(8, 'MidnightBlue'),
(9, 'SkyBlue');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `config`
--

CREATE TABLE `config` (
  `id` int(11) NOT NULL,
  `elements_per_page` int(11) DEFAULT NULL,
  `sort_users` varchar(30) DEFAULT NULL,
  `sort_meeting_points` varchar(30) DEFAULT NULL,
  `palette_private_id` int(11) DEFAULT NULL,
  `palette_public_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `config`
--

INSERT INTO `config` (`id`, `elements_per_page`, `sort_users`, `sort_meeting_points`, `palette_private_id`, `palette_public_id`) VALUES
(1, 3, 'last_name', 'name', 3, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `meeting_points`
--

CREATE TABLE `meeting_points` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `direction` varchar(100) DEFAULT NULL,
  `coordinates` varchar(100) DEFAULT NULL,
  `state` tinyint(1) DEFAULT NULL,
  `telephone` varchar(30) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `meeting_points`
--

INSERT INTO `meeting_points` (`id`, `name`, `direction`, `coordinates`, `state`, `telephone`, `email`) VALUES
(8, 'refugio_1', '116, 1411', '84.7938, -38.0691', 1, '296631452511', 'darw@gmail.com'),
(9, 'refugio_2', '1, 195', '49.0077, 17.6468', 1, '424264', 'sdada@gmail.com'),
(10, 'escuela_19', '85, 900', '-13.4562, -107.1375', 1, '2131231', 'sadas@gmail.com'),
(11, 'escuela_32', '20, 280', '24.4480, 160.8784', 0, '123123', 'Tomad0@hotmail.com'),
(12, 'escuela_19', '123123', '123123, 123113', 1, '11111111', 'email1@email1.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `palettes`
--

CREATE TABLE `palettes` (
  `id` int(11) NOT NULL,
  `color1_id` int(11) DEFAULT NULL,
  `color2_id` int(11) DEFAULT NULL,
  `color3_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `palettes`
--

INSERT INTO `palettes` (`id`, `color1_id`, `color2_id`, `color3_id`) VALUES
(3, 5, 2, 4),
(4, 6, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permits`
--

CREATE TABLE `permits` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `permits`
--

INSERT INTO `permits` (`id`, `name`) VALUES
(1, 'user_index'),
(2, 'config_index'),
(3, 'user_modify'),
(4, 'points_index'),
(5, 'points_modify'),
(6, 'points_new'),
(7, 'points_create'),
(8, 'points_show'),
(9, 'points_delete'),
(10, 'config_modify'),
(11, 'user_new'),
(12, 'user_block'),
(13, 'user_unblock'),
(14, 'user_delete'),
(15, 'user_assign_role'),
(16, 'user_unassign_role'),
(17, 'user_create');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `private_palett_has_color`
--

CREATE TABLE `private_palett_has_color` (
  `config_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `public_palett_has_color`
--

CREATE TABLE `public_palett_has_color` (
  `config_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'operator');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `role_has_permit`
--

CREATE TABLE `role_has_permit` (
  `role_id` int(11) DEFAULT NULL,
  `permit_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `role_has_permit`
--

INSERT INTO `role_has_permit` (`role_id`, `permit_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(2, 4),
(2, 8),
(2, 5),
(2, 6),
(2, 7),
(1, 17);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `username`, `email`, `password`, `active`, `created_at`) VALUES
(1, 'cosme', 'fulanito', 'admin', 'admin@admin.com', '123123', 1, '2021-10-13 16:30:13'),
(2, 'zosme', 'zulanito', 'zozme', 'zozme@gmail.com', '234234', 0, '2021-10-17 11:46:56'),
(3, 'pepe', 'pepe', 'pepe', 'pepe@pepe.com', '123123', 1, '2021-10-21 12:33:07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_has_role`
--

CREATE TABLE `user_has_role` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_has_role`
--

INSERT INTO `user_has_role` (`user_id`, `role_id`) VALUES
(1, 1),
(2, 2),
(3, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `colors`
--
ALTER TABLE `colors`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `config`
--
ALTER TABLE `config`
  ADD PRIMARY KEY (`id`),
  ADD KEY `palette_private_id` (`palette_private_id`),
  ADD KEY `palette_public_id` (`palette_public_id`);

--
-- Indices de la tabla `meeting_points`
--
ALTER TABLE `meeting_points`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `palettes`
--
ALTER TABLE `palettes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `color1_id` (`color1_id`),
  ADD KEY `color2_id` (`color2_id`),
  ADD KEY `color3_id` (`color3_id`);

--
-- Indices de la tabla `permits`
--
ALTER TABLE `permits`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `private_palett_has_color`
--
ALTER TABLE `private_palett_has_color`
  ADD KEY `config_id` (`config_id`),
  ADD KEY `color_id` (`color_id`);

--
-- Indices de la tabla `public_palett_has_color`
--
ALTER TABLE `public_palett_has_color`
  ADD KEY `config_id` (`config_id`),
  ADD KEY `color_id` (`color_id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `role_has_permit`
--
ALTER TABLE `role_has_permit`
  ADD KEY `role_id` (`role_id`),
  ADD KEY `permit_id` (`permit_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `user_has_role`
--
ALTER TABLE `user_has_role`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `colors`
--
ALTER TABLE `colors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `config`
--
ALTER TABLE `config`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `meeting_points`
--
ALTER TABLE `meeting_points`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `palettes`
--
ALTER TABLE `palettes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `permits`
--
ALTER TABLE `permits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `config`
--
ALTER TABLE `config`
  ADD CONSTRAINT `config_ibfk_1` FOREIGN KEY (`palette_private_id`) REFERENCES `palettes` (`id`),
  ADD CONSTRAINT `config_ibfk_2` FOREIGN KEY (`palette_public_id`) REFERENCES `palettes` (`id`);

--
-- Filtros para la tabla `palettes`
--
ALTER TABLE `palettes`
  ADD CONSTRAINT `palettes_ibfk_1` FOREIGN KEY (`color1_id`) REFERENCES `colors` (`id`),
  ADD CONSTRAINT `palettes_ibfk_2` FOREIGN KEY (`color2_id`) REFERENCES `colors` (`id`),
  ADD CONSTRAINT `palettes_ibfk_3` FOREIGN KEY (`color3_id`) REFERENCES `colors` (`id`);

--
-- Filtros para la tabla `private_palett_has_color`
--
ALTER TABLE `private_palett_has_color`
  ADD CONSTRAINT `private_palett_has_color_ibfk_1` FOREIGN KEY (`config_id`) REFERENCES `config` (`id`),
  ADD CONSTRAINT `private_palett_has_color_ibfk_2` FOREIGN KEY (`color_id`) REFERENCES `colors` (`id`);

--
-- Filtros para la tabla `public_palett_has_color`
--
ALTER TABLE `public_palett_has_color`
  ADD CONSTRAINT `public_palett_has_color_ibfk_1` FOREIGN KEY (`config_id`) REFERENCES `config` (`id`),
  ADD CONSTRAINT `public_palett_has_color_ibfk_2` FOREIGN KEY (`color_id`) REFERENCES `colors` (`id`);

--
-- Filtros para la tabla `role_has_permit`
--
ALTER TABLE `role_has_permit`
  ADD CONSTRAINT `role_has_permit_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `role_has_permit_ibfk_2` FOREIGN KEY (`permit_id`) REFERENCES `permits` (`id`);

--
-- Filtros para la tabla `user_has_role`
--
ALTER TABLE `user_has_role`
  ADD CONSTRAINT `user_has_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `user_has_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
