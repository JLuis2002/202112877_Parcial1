CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_vencimiento DATE,
    completada BOOLEAN DEFAULT FALSE
);

insert into tareas(nombre,descripcion,fecha_vencimiento)
			VALUES('Ordenar','Ordenar la ropa','2024-02-20');

select*from tareas;
