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

CREATE TABLE IF NOT EXISTS Especialidad(
    id INT AUTO_INCREMENT,
    especialidad VARCHAR(250) NOT NULL,
    descripcion VARCHAR(250) NOT NULL,
     
    CONSTRAINT PK_especialidad PRIMARY KEY (id) 
 );

CREATE TABLE IF NOT EXISTS Doctor(
    id INT AUTO_INCREMENT,  
    nombre varchar (250) NOT NULL, 
    licencia varchar (250) NOT NULL,
    id_especialidad INT NOT NULL,

    CONSTRAINT PK_Doctor PRIMARY KEY (id), 
    CONSTRAINT fk_Doctor_id_especialidad FOREIGN key (id_especialidad) REFERENCES especialidad (id)
 );

CREATE TABLE IF NOT EXISTS Paciente(
    id INT AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL, -- "VARCHAR" es el limite de carcacteres que puede tener (en nombre, letras, etc.. el limite es 255
    edad INT NOT NULL, -- ahora "VARCHAR" en numeros el limite es 10
    id_direccion INT NOT NULL,  
    rut VARCHAR(10) NOT NULL,

    CONSTRAINT PK_paciente PRIMARY KEY (id) -- aqui es para crear la pk (primary key)
    CONSTRAINT fk_paciente_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id) -- aqui es para insertar y/o crear la fk (foreing key)
 ); 

CREATE TABLE IF NOT EXISTS ficha_clinica(
    id INT AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    historial_medico VARCHAR(255) NOT NULL,

    CONSTRAINT pk_ficha_clinica PRIMARY KEY (id),
    CONSTRAINT fk_ficha_clinica_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id)
);

 CREATE TABLE IF NOT EXISTS Cita_medica( -- creacion de tablas 
    id INT AUTO_INCREMENT -- aqui es para empezar una id de una tabla 
    fechayhora DATE NOT NULL,  -- "not null" es que es 100% necesaria esa info
    motivo VARCHAR(255) NOT NULL, 
    diagnostico VARCHAR(255) NOT NULL,
    licencia_medica VARCHAR(255) NULL, -- "NULL" es que no es necesaria, da igual si esta o no 
    id_doctor INT NOT NULL, -- "INT" Se utiliza normalmente en entero como id, edad, etc... (se pone porque no son tantos numeros)
    id_paciente INT NOT NULL, 

    CONSTRAINT pk_Cita_medica PRIMARY KEY (id),
    CONSTRAINT fk_cita_medica_id_doctor FOREIGN KEY (id_doctor) REFERENCES doctor(id)
    CONSTRAINT fk_cita_medica-id_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id)
 );
 
 CREATE TABLE IF NOT EXISTS Recetamedica(
    id INT AUTO_INCREMENT, 
    detalle VARCHAR(250) NOT NULL, 
    fecha DATE NOT NULL, 
    id_paciente INT NOT NULL,
    id_doctor INT NOT NULL,

    CONSTRAINT pk_Recetamedica PRIMARY KEY (id), 
    CONSTRAINT fk_Recetamedica_id_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id)
    CONSTRAINT fk_Recetamedica_id_doctor FOREIGN KEY (id_doctor) REFERENCES Doctor(id)
 );

 CREATE TABLE IF NOT EXISTS Turno(
   id INT AUTO_INCREMENT,
   fecha DATE NOT NULL,
   hora_inicio DATETIME NOT NULL,
   hora_fin DATETIME NOT NULL,
   id_doctor INT NOT NULL,

   CONSTRAINT pk_id_Turno PRIMARY KEY (id),
   CONSTRAINT fk_Turno_id_doctor FOREIGN KEY (id_doctor) REFERENCES Doctor(id)
 );

 CREATE TABLE IF NOT EXISTS Orden_examenes(
   id INT AUTO_INCREMENT,
   fecha DATE NOT NULL,
   id_paciente INT NOT NULL,
   id_doctor INT NOT NULL,
   id_cita_medica INT NOT NULL,

   CONSTRAINT pk_id_orden_examenes PRIMARY KEY(id),
   CONSTRAINT fk_orden_examenes_id_paciente FOREIGN KEY (id_paciente) REFERENCES Paciente(id),
   CONSTRAINT fk_orden_examenes_id_doctor FOREIGN KEY (id_doctor) REFERENCES Doctor(id),
   CONSTRAINT fk_orden_examenes_id_cita_medica FOREIGN KEY (id_cita_medica) REFERENCES Cita_medica(id)
 );