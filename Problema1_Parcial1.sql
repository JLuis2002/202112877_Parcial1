

CREATE TABLE dias(
	ndia serial PRIMARY KEY, 
	dia varchar(20) not null,
	horas int not null --horas por dia de hacer ejercicio
);
INSERT INTO dias(dia,horas) VALUES 
				('LUNES',2),
				('MARTES',2),
				('MIERCOLES',2),
				('JUEVES',2),
				('VIERNES',2),
				('SABADO',2);

SELECT d.ndia AS N , d.dia AS DIA, d.horas AS Horas_diarias FROM dias d;

CREATE TABLE ejercicios(
	nejercicio INT PRIMARY KEY,
	tipo VARCHAR(20) NOT NULL,
	series INT NOT NULL,
	repeticiones INT NOT NULL
);


INSERT INTO ejercicios(nejercicio,tipo,series,repeticiones) VALUES
				  (1,'PECHO',4,10),
				  (2,'BICEPS',4,10),
				  (3,'ESPALDA',4,10),
				  (4,'TRICEPS',3,8),
				  (5,'PIERNA',3,12);
SELECT e.tipo AS Ejercicio, 
	   e.series AS Series_alDía, 
	   e.repeticiones AS REPS 
FROM ejercicios e;

CREATE TABLE rutina(
    id SERIAL PRIMARY KEY,
    Rutinas VARCHAR(20) NOT NULL,
    ndia INTEGER REFERENCES dias(ndia),
    ejercicio_id INTEGER REFERENCES ejercicios(nejercicio)
);

insert into rutina(Rutinas,ndia,ejercicio_id) VALUES
				  ('Intensa',1,5),
				  ('Media',2,3),
				  ('Media',2,2);
select*from rutina;
SELECT d.dia AS DIA,
       r.rutinas AS RUTINA,
       d.horas AS Horas_diarias,
       e.tipo AS Ejercicio,
       e.series AS "N series",
       e.repeticiones AS REPS
FROM rutina r
JOIN dias d ON r.ndia = d.ndia
JOIN ejercicios e ON r.ejercicio_id = e.nejercicio;

	   

select*from rutina;

drop table dias;
DROP TABLE ejercicios;
drop table rutina;


