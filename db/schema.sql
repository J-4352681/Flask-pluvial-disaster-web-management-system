-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 14-10-2021 a las 07:54:41
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

create database proyecto;

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
(4, 'Azure');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `config`
--

CREATE TABLE `config` (
  `id` int(11) NOT NULL,
  `elements_per_page` int(11) DEFAULT NULL,
  `sort_users` varchar(30) DEFAULT NULL,
  `sort_meeting_points` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `config`
--

INSERT INTO `config` (`id`, `elements_per_page`, `sort_users`, `sort_meeting_points`) VALUES
(1, 16, 'username', 'name');

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
(1, 'user_index');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `private_palett_has_color`
--

CREATE TABLE `private_palett_has_color` (
  `config_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `private_palett_has_color`
--

INSERT INTO `private_palett_has_color` (`config_id`, `color_id`) VALUES
(1, 1),
(1, 2),
(1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `public_palett_has_color`
--

CREATE TABLE `public_palett_has_color` (
  `config_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `public_palett_has_color`
--

INSERT INTO `public_palett_has_color` (`config_id`, `color_id`) VALUES
(1, 1),
(1, 2),
(1, 4);

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
(1, 'admin');

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
(1, 1);

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
(1, 'cosme', 'fulanito', 'admin@', 'admin', '123123', 1, '2021-10-13 16:30:13');

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
(1, 1);

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
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `config`
--
ALTER TABLE `config`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `permits`
--
ALTER TABLE `permits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

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
