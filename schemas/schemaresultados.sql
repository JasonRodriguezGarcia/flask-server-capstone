DROP TABLE IF EXISTS `ofertas_resultados`;
CREATE TABLE `ofertas_resultados` (
  `ofertas_resultados_id_resultado` INTEGER NOT NULL,
  `ofertas_resultados_id_oferta` INTEGER NOT NULL,
  `ofertas_resultados_id_trabajador` INTEGER NOT NULL,
  `ofertas_resultados_trabajador_estado` TEXT(10) NOT NULL,
  `ofertas_resultados_contratado` BOOLEAN NOT NULL,
  PRIMARY KEY (`ofertas_resultados_id_resultado`),
  UNIQUE (`ofertas_resultados_id_resultado`),
  FOREIGN KEY (`ofertas_resultados_id_oferta`) REFERENCES `ofertas` (`ofertas_id_oferta`) ON DELETE CASCADE, -- ON UPDATE CASCADE
  FOREIGN KEY (`ofertas_resultados_id_trabajador`) REFERENCES `trabajadores` (`trabajadores_id_trabajador`) ON DELETE CASCADE -- ON UPDATE CASCADE
); --ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
