USE iei_172_n2;

CREATE TABLE IF NOT EXISTS comunas(
    id INT AUTO_INCREMENT, 
    codigo_comuna CHAR(5) NOT NULL,
    nombre_comuna VARCHAR(60) NOT NULL,

    CONSTRAINT pk_comunas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS direccion(
    id INT AUTO_INCREMENT,
    calle VARCHAR(255) NULL,
    numero VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,
    detalle VARCHAR(255) NULL,
    id_comuna INT NOT NULL,

    CONSTRAINT pk_direccion PRIMARY KEY (id),
    CONSTRAINT fk_direccion_comunas FOREIGN KEY (id_comuna) REFERENCES comunas(id)
);

CREATE TABLE IF NOT EXISTS ficha_clinica(
    id INT AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    historial_medico VARCHAR(255) NOT NULL,

);