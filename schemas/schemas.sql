-- CREATING TABLES AND RELATIONSHIPS 

DROP TABLE IF EXISTS `carnets`;
CREATE TABLE `carnets` (
  `carnets_id_carnet` INTEGER PRIMARY KEY AUTOINCREMENT,
  `carnets_descripcion_carnet` TEXT(3) NOT NULL UNIQUE,
  `carnets_texto_libre` TEXT(30)
);
--   PRIMARY KEY (carnets_id_carnet),
--   UNIQUE KEY carnets_id_carnet_UNIQUE (carnets_id_carnet)

DROP TABLE IF EXISTS `contratos`;
CREATE TABLE `contratos` (
  `contratos_id_contrato` INTEGER NOT NULL, -- AUTOINCREMENT,
  `contratos_descripcion_contrato` TEXT(20) NOT NULL,
  `contratos_descripcion_contrato_texto_libre` TEXT(20),
  PRIMARY KEY (`contratos_id_contrato`),
  UNIQUE  (`contratos_id_contrato`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `empresas`;
CREATE TABLE `empresas` (
  `empresas_id_empresa` INTEGER NOT NULL PRIMARY KEY, -- AUTOINCREMENT,
  `empresas_cif` TEXT(9) NOT NULL,
  `empresas_nombre` TEXT(45) NOT NULL,
  `empresas_correo_electronico` TEXT(45) NOT NULL,
  `empresas_persona_contacto` TEXT(45) NOT NULL,
  `empresas_telefono` TEXT(20) NOT NULL,
  UNIQUE (`empresas_id_empresa`),
  UNIQUE (`empresas_cif`),
  UNIQUE (`empresas_correo_electronico`),
  UNIQUE (`empresas_telefono`)
); --   ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `estados_ofertas`;
CREATE TABLE `estados_ofertas` (
  `estados_ofertas_id_estado_oferta` INTEGER NOT NULL,
  `estados_ofertas_descripcion_estado_oferta` TEXT(20) NOT NULL,
  `estados_ofertas_descripcion_estado_oferta_texto_libre` TEXT(20),
  PRIMARY KEY (`estados_ofertas_id_estado_oferta`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- DROP TABLE IF EXISTS `estados_trabajadores`;
-- CREATE TABLE `estados_trabajadores` (
--   `estados_trabajadores_id_estado_trabajador` INTEGER NOT NULL,
--   `estados_trabajadores_descripcion_estado_trabajador` TEXT(20) NOT NULL,
--   `estados_trabajadores_descripcion_estado_trabajador_texto_libre` TEXT(20),
--   PRIMARY KEY (`estados_trabajadores_id_estado_trabajador`),
--   UNIQUE (`estados_trabajadores_id_estado_trabajador`)
-- ); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `formaciones`;
CREATE TABLE `formaciones` (
  `formaciones_id_formacion` INTEGER NOT NULL, -- AUTOINCREMENT,
  `formaciones_descripcion_formacion` TEXT(190) NOT NULL,
  `formaciones_descripcion_formacion_texto_libre` TEXT(190),
  PRIMARY KEY (`formaciones_id_formacion`),
  UNIQUE (`formaciones_id_formacion`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `idiomas`;
CREATE TABLE `idiomas` (
  `idiomas_id_idioma` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `idiomas_descripcion_idioma` TEXT(20) NOT NULL,
  `idiomas_descripcion_idioma_texto_libre` TEXT(20),
  PRIMARY KEY (`idiomas_id_idioma`),
  UNIQUE (`idiomas_id_idioma`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `jornadas`;
CREATE TABLE `jornadas` (
  `jornadas_id_jornada` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `jornadas_descripcion_jornada` TEXT(20) NOT NULL,
  `jornadas_descipcion_jornada_texto_libre` TEXT(20),
  PRIMARY KEY (`jornadas_id_jornada`),
  UNIQUE (`jornadas_id_jornada`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `municipios`;
CREATE TABLE `municipios` (
  `municipios_id_municipio` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `municipios_descripcion_municipio` TEXT(45) NOT NULL,
  `municipios_descripcion_municipio_texto_libre` TEXT(45),
  PRIMARY KEY (`municipios_id_municipio`),
  UNIQUE (`municipios_id_municipio`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `provincias`;
CREATE TABLE `provincias` (
  `provincias_id_provincia` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `provincias_descripcion_provincia` TEXT(45) NOT NULL,
  `provincias_descripcion_provincia_texto_libre` TEXT(45),
  PRIMARY KEY (`provincias_id_provincia`),
  UNIQUE (`provincias_id_provincia`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `nivel_idiomas`;
CREATE TABLE `nivel_idiomas` (
  `nivel_idiomas_id_nivel_idioma` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `nivel_idiomas_descripcion_nivel_idioma` TEXT(20) NOT NULL,
  `nivel_idiomas_descripcion_nivel_idioma_texto_libre` TEXT(20),
  PRIMARY KEY (`nivel_idiomas_id_nivel_idioma`),
  UNIQUE (`nivel_idiomas_id_nivel_idioma`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `ocupaciones`;
CREATE TABLE `ocupaciones` (
  `ocupaciones_id_ocupacion` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `ocupaciones_descripcion_ocupacion` TEXT(120) NOT NULL,
  `ocupaciones_descripcion_ocupacion_texto_libre` TEXT(120),
  PRIMARY KEY (`ocupaciones_id_ocupacion`),
  UNIQUE (`ocupaciones_id_ocupacion`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
-- Lo siguiente en DB Browser Sqlite importar tabla con contratos y luego ejecutar sql siguiente
-- INSERT INTO "contratos" ( contratos_id_contrato, contratos_descripcion_contrato )
-- SELECT field1, field2
-- FROM "ocupaciones datos2";

DROP TABLE IF EXISTS `ofertas`;
CREATE TABLE `ofertas` (
  `ofertas_id_oferta` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `ofertas_id_empresa` INTEGER NOT NULL,
  `ofertas_id_ocupacion` INTEGER NOT NULL,
  `ofertas_meses_experiencia` INTEGER NOT NULL,
  `ofertas_id_formacion` INTEGER NOT NULL,
  `ofertas_id_carnet_conducir` INTEGER NOT NULL,
  `ofertas_id_vehiculo` INTEGER NOT NULL,
  `ofertas_id_municipio` INTEGER NOT NULL,
  `ofertas_id_provincia` INTEGER NOT NULL,
  `ofertas_puesto_descripcion` BLOB NOT NULL,
  `ofertas_id_contrato` INTEGER NOT NULL,
  `ofertas_id_jornada` INTEGER NOT NULL,
--   `ofertas_convenio` blob NOT NULL,
  `ofertas_salario` INTEGER NOT NULL DEFAULT '0',
  `ofertas_id_estado_oferta` INTEGER NOT NULL,
  `ofertas_fecha_creacion` date DEFAULT NULL,
  `ofertas_fecha_finalizacion` date DEFAULT NULL,
  `ofertas_priorityField1` BOOLEAN DEFAULT NULL,
  `ofertas_priorityField2` BOOLEAN DEFAULT NULL,
  `ofertas_priorityField3` BOOLEAN DEFAULT NULL,
  `ofertas_priorityField4` BOOLEAN DEFAULT NULL,
  PRIMARY KEY (`ofertas_id_oferta`),
  UNIQUE (`ofertas_id_oferta`),
  FOREIGN KEY (`ofertas_id_carnet_conducir`) REFERENCES `carnets` (`carnets_id_carnet`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_contrato`) REFERENCES `contratos` (`contratos_id_contrato`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_empresa`) REFERENCES `empresas` (`empresas_id_empresa`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_estado_oferta`) REFERENCES `estados_ofertas` (`estados_ofertas_id_estado_oferta`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_formacion`) REFERENCES `formaciones` (`formaciones_id_formacion`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_jornada`) REFERENCES `jornadas` (`jornadas_id_jornada`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_municipio`) REFERENCES `municipios` (`municipios_id_municipio`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_ocupacion`) REFERENCES `ocupaciones` (`ocupaciones_id_ocupacion`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_provincia`) REFERENCES `provincias` (`provincias_id_provincia`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_id_vehiculo`) REFERENCES `vehiculos` (`vehiculos_id_vehiculo`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `ofertas_idiomas`;
CREATE TABLE `ofertas_idiomas` (
  `ofertas_idiomas_id_oferta` INTEGER NOT NULL,
  `ofertas_idiomas_id_idioma` INTEGER NOT NULL,
  `ofertas_idiomas_id_nivel` INTEGER NOT NULL,
  FOREIGN KEY (`ofertas_idiomas_id_idioma`) REFERENCES `idiomas` (`idiomas_id_idioma`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_idiomas_id_nivel`) REFERENCES `nivel_idiomas` (`nivel_idiomas_id_nivel_idioma`) ON DELETE CASCADE,
  FOREIGN KEY (`ofertas_idiomas_id_oferta`) REFERENCES `ofertas` (`ofertas_id_oferta`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- DROP TABLE IF EXISTS `ofertas_trabajadores`;
-- CREATE TABLE `ofertas_trabajadores` (
--   `ofertas_trabajadores_id_oferta` INTEGER NOT NULL,
--   `ofertas_trabajadores_id_trabajador` INTEGER NOT NULL,
--   `ofertas_trabajadores_fecha_seleccion` date DEFAULT NULL,
--   `ofertas_trabajadores_id_estado_trabajador` INTEGER NOT NULL,
-- --   FOREIGN KEY (`ofertas_trabajadores_id_estado_trabajador`) REFERENCES `estados_trabajadores` (`estados_trabajadores_id_estado_trabajador`) ON DELETE CASCADE,
--   FOREIGN KEY (`ofertas_trabajadores_id_oferta`) REFERENCES `ofertas` (`ofertas_id_oferta`) ON DELETE CASCADE,
--   FOREIGN KEY (`ofertas_trabajadores_id_trabajador`) REFERENCES `trabajadores` (`trabajadores_id_trabajador`) ON DELETE CASCADE
-- ); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `vehiculos`;
CREATE TABLE `vehiculos` (
  `vehiculos_id_vehiculo` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `vehiculos_descripcion_vehiculo` TEXT(20) NOT NULL,
  `vehiculos_descripcion_vehiculo_texto_libre` TEXT(20),
  PRIMARY KEY (`vehiculos_id_vehiculo`),
  UNIQUE (`vehiculos_id_vehiculo`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `trabajadores`;
CREATE TABLE `trabajadores` (
  `trabajadores_id_trabajador` INTEGER NOT NULL, -- AUTO_INCREMENT,
  `trabajadores_nombre` TEXT(20) NOT NULL,
  `trabajadores_apellidos` TEXT(45) NOT NULL,
  `trabajadores_fecha_nacimiento` date NOT NULL,
  `trabajadores_doi` TEXT(8) NOT NULL,
  `trabajadores_id_municipio` INTEGER NOT NULL,
  `trabajadores_codigo_postal` INTEGER NOT NULL,
  `trabajadores_id_provincia` INTEGER NOT NULL,
  `trabajadores_id_vehiculo` INTEGER NOT NULL,
  `trabajadores_curriculum` BLOB, -- NOT NULL,
  `trabajadores_telefono_contacto` TEXT(20) NOT NULL,
  `trabajadores_correo_electronico` TEXT(45) NOT NULL,
  `trabajadores_id_situacion` INTEGER DEFAULT NULL,
  `trabajadores_lopd` BOOLEAN DEFAULT NULL,
  PRIMARY KEY (`trabajadores_id_trabajador`),
  UNIQUE (`trabajadores_id_trabajador`),
  FOREIGN KEY (`trabajadores_id_municipio`) REFERENCES `municipios` (`municipios_id_municipio`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_id_provincia`) REFERENCES `provincias` (`provincias_id_provincia`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_id_situacion`) REFERENCES `trabajadores_situaciones` (`trabajadores_situaciones_id_situacion`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_id_vehiculo`) REFERENCES `vehiculos` (`vehiculos_id_vehiculo`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
CREATE UNIQUE INDEX index_doi ON `trabajadores` (`trabajadores_doi` ASC); ---   PROBAR!!!

DROP TABLE IF EXISTS `trabajadores_carnets`;
CREATE TABLE `trabajadores_carnets` (
  `trabajadores_carnets_id_trabajador` INTEGER NOT NULL,
  `trabajadores_carnets_id_carnet` INTEGER NOT NULL,
  FOREIGN KEY (`trabajadores_carnets_id_carnet`) REFERENCES `carnets` (`carnets_id_carnet`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_carnets_id_trabajador`) REFERENCES `trabajadores` (`trabajadores_id_trabajador`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `trabajadores_formaciones`;
CREATE TABLE `trabajadores_formaciones` (
  `trabajadores_formaciones_id_trabajador` INTEGER NOT NULL,
  `trabajadores_formaciones_id_formacion` INTEGER NOT NULL,
  FOREIGN KEY (`trabajadores_formaciones_id_formacion`) REFERENCES `formaciones` (`formaciones_id_formacion`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_formaciones_id_trabajador`) REFERENCES `trabajadores` (`trabajadores_id_trabajador`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `trabajadores_idiomas`;
CREATE TABLE `trabajadores_idiomas` (
  `trabajadores_idiomas_id_trabajador` INTEGER NOT NULL,
  `trabajadores_idiomas_id_idioma` INTEGER NOT NULL,
  `trabajadores_idiomas_id_nivel_idioma` INTEGER NOT NULL,
  FOREIGN KEY (`trabajadores_idiomas_id_idioma`) REFERENCES `idiomas` (`idiomas_id_idioma`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_idiomas_id_nivel_idioma`) REFERENCES `nivel_idiomas` (`nivel_idiomas_id_nivel_idioma`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_idiomas_id_trabajador`) REFERENCES `trabajadores` (`trabajadores_id_trabajador`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `trabajadores_ocupaciones`;
CREATE TABLE `trabajadores_ocupaciones` (
  `trabajadores_ocupaciones_id_trabajador` INTEGER NOT NULL,
  `trabajadores_ocupaciones_id_ocupacion` INTEGER NOT NULL,
--   `trabajadores_ocupaciones_años` INTEGER NOT NULL DEFAULT '0',
  `trabajadores_ocupaciones_meses` INTEGER NOT NULL DEFAULT '0',
  FOREIGN KEY (`trabajadores_ocupaciones_id_ocupacion`) REFERENCES `ocupaciones` (`ocupaciones_id_ocupacion`) ON DELETE CASCADE,
  FOREIGN KEY (`trabajadores_ocupaciones_id_trabajador`) REFERENCES `trabajadores` (`trabajadores_id_trabajador`) ON DELETE CASCADE
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

DROP TABLE IF EXISTS `trabajadores_situaciones`;
CREATE TABLE `trabajadores_situaciones` (
  `trabajadores_situaciones_id_situacion` INTEGER NOT NULL,
  `trabajadores_situaciones_descripcion_situacion` TEXT(10) NOT NULL,
  `trabajadores_situaciones_descripcion_situacion_texto_libre` TEXT(10),
  PRIMARY KEY (`trabajadores_situaciones_id_situacion`),
  UNIQUE (`trabajadores_situaciones_id_situacion`)
); -- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

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

-- EXAMPLE
-- CREATE TABLE contact_groups(
--    contact_id INTEGER,
--    group_id INTEGER,
--    PRIMARY KEY (contact_id, group_id),
--    FOREIGN KEY (contact_id) 
--       REFERENCES contacts (contact_id) 
--          ON DELETE CASCADE 
--          ON UPDATE NO ACTION,
--    FOREIGN KEY (group_id) 
--       REFERENCES groups (group_id) 
--          ON DELETE CASCADE 
--          ON UPDATE NO ACTION
-- );