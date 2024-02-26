-- Crear la tabla de viajes
CREATE TABLE viajes (
    id SERIAL PRIMARY KEY,
    destino VARCHAR(50) NOT NULL,
    alojamiento NUMERIC(10, 2) NOT NULL,
    comida NUMERIC(10, 2) NOT NULL,
    transporte NUMERIC(10, 2) NOT NULL,
    descripcion TEXT,
    fecha DATE NOT NULL
);

-- Insertar algunos ejemplos de viajes
INSERT INTO viajes (destino, alojamiento, comida, transporte, descripcion, fecha)
VALUES 
    ('Antigua', 1500.00, 500.00, 300.00, 'Vacaciones en Antigua', '2024-01-10'),
    ('Guatemala', 2000.00, 800.00, 400.00, 'Viaje de negocios a Guatemala', '2024-02-20'),
    ('Quetzaltenango', 2500.00, 1000.00, 600.00, 'Viaje de turismo a Quetzaltenango', '2024-03-15');

select*from viajes;




-- Crear tabla de horas de sueño
CREATE TABLE horas (
    id SERIAL PRIMARY KEY,
    semana INTEGER NOT NULL,
    dia VARCHAR(20) NOT NULL,
    horas INTEGER NOT NULL
);

-- Insertar datos para la semana 1
INSERT INTO horas (semana, dia, horas) VALUES
    (1, 'lunes', 7),
    (1, 'martes', 7),
    (1, 'miércoles', 6),
    (1, 'jueves', 7),
    (1, 'viernes', 8),
    (1, 'sábado', 9),
    (1, 'domingo', 8);

-- Insertar datos para la semana 2
INSERT INTO horas (semana, dia, horas) VALUES
    (2, 'lunes', 8),
    (2, 'martes', 7);
	
select*from horas;

drop table horas;

-- Crear tabla de recomendaciones de sueño
CREATE TABLE recomendaciones (
    id SERIAL PRIMARY KEY,
    metodo VARCHAR(50) NOT NULL,
    recomendacion TEXT
);

-- Insertar recomendaciones para dormir más
INSERT INTO recomendaciones (metodo, recomendacion) VALUES
    ('Horario regular', 'Ir a la cama y levantarse a la misma hora todos los días.'),
    ('Ambiente adecuado', 'Dormitorio oscuro, tranquilo y a temperatura agradable.'),
    ('Evitar cafeína y tecnología', 'Reducir la ingesta de cafeína por la tarde y evitar pantallas antes de dormir.');

-- Insertar recomendaciones para dormir menos o despertar fácilmente
INSERT INTO recomendaciones (metodo, recomendacion) VALUES
    ('Ejercicio', 'Hacer ejercicio moderado para aumentar la energía.'),
    ('Recreacion', 'Pasar tiempo al aire libre para regular el reloj biológico.'),
    ('Siestas', 'Limitar las siestas a 20-30 minutos durante el día.');
select*from recomendaciones;