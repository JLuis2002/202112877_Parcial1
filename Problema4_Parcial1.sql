-- Crear la tabla de libros
CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    genero VARCHAR(100),
    paginas INTEGER,
    fecha_publicacion DATE,
    fecha_lectura DATE
);

-- Crear la tabla de lecturas
CREATE TABLE lecturas (
    id SERIAL PRIMARY KEY,
    libro_id INTEGER REFERENCES libros(id),
    usuario_id INTEGER,
    fecha_lectura DATE,
    paginas_leidas INTEGER,
    nota TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Crear la tabla de metas de lectura
CREATE TABLE metas_lectura (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER,
    fecha_inicio DATE,
    fecha_fin DATE,
    paginas_objetivo INTEGER,
    cumplida BOOLEAN,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Agregar libros a la base de datos
INSERT INTO libros(titulo, autor, genero, paginas, fecha_publicacion) VALUES 
    ('Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico', 448, '1967-05-30'),
    ('1984', 'George Orwell', 'Ciencia ficción', 328, '1949-06-08'),
    ('Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', 332, '1997-06-26'),
    ('El hobbit', 'J.R.R. Tolkien', 'Fantasía', 310, '1937-09-21'),
    ('Matar a un ruiseñor', 'Harper Lee', 'Novela', 281, '1960-07-11');


-- Crear la tabla de recomendaciones
CREATE TABLE recomendaciones (
    id SERIAL PRIMARY KEY,
    libro_id INTEGER REFERENCES libros(id),
    descripcion TEXT
);

-- Crear la tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    fecha_nacimiento DATE
);
