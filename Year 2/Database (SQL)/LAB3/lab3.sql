CREATE DATABASE PublicTransport

CREATE TABLE Controller(
	controller_id SMALLINT PRIMARY KEY,
	name VARCHAR(200),
	rating TINYINT NOT NULL,
	CHECK (rating BETWEEN 1 AND 10)
)

CREATE TABLE Passenger(
	passenger_id SMALLINT PRIMARY KEY,
	name VARCHAR(200),
)

CREATE TABLE ControllerPassengerRelation(
	passenger_id SMALLINT NOT NULL,
	controller_id SMALLINT NOT NULL,
	FOREIGN KEY (passenger_id) REFERENCES Passenger(passenger_id),
	FOREIGN KEY (controller_id) REFERENCES Controller(controller_id),
	UNIQUE (passenger_id, controller_id)
)


CREATE TABLE Bus(
	bus_id SMALLINT PRIMARY KEY,
  	company VARCHAR(80),
  	number_of_seats TINYINT,
  	price FLOAT,
  	departure VARCHAR(200),
  	destination VARCHAR(200),
  	passenger_id SMALLINT REFERENCES Passenger(passenger_id)
)

CREATE TABLE Train( 
	train_id SMALLINT PRIMARY KEY,
	company VARCHAR(80),
	number_of_seats SMALLINT,
	price FLOAT,
	first_class_number_of_seats SMALLINT,
	second_class_number_of_seats SMALLINT,
	departure VARCHAR(200),
	destination VARCHAR(200),
	passenger_id SMALLINT REFERENCES Passenger(passenger_id)
)

CREATE TABLE Tram(
	tram_id SMALLINT PRIMARY KEY,
	company VARCHAR(200),
	number_of_seats SMALLINT,
	price FLOAT,
	departure VARCHAR(200),
	destionation VARCHAR(200),
	passenger_id SMALLINT REFERENCES Passenger(passenger_id)
)

CREATE TABLE Coach(
	coach_id SMALLINT PRIMARY KEY,
	company VARCHAR(200),
	number_of_seats SMALLINT,
	price FLOAT,
	departure VARCHAR(200),
	destination VARCHAR(200),
	passenger_id SMALLINT REFERENCES Passenger(passenger_id)
)

CREATE TABLE Plane(
	plane_id SMALLINT PRIMARY KEY,
	company VARCHAR(200),
	number_of_seats SMALLINT,
	price_first_class FLOAT,
	price_second_class FLOAT,
	first_class_number_of_seats SMALLINT,
	second_class_number_of_seats SMALLINT,
	departure VARCHAR(200),
	destination VARCHAR(200),
	transatlantic BIT,
	passenger_id SMALLINT REFERENCES Passenger(passenger_id)
)



CREATE TABLE Airport(
	airport_id SMALLINT PRIMARY KEY,
	location VARCHAR(200),
	number_of_planes SMALLINT,
	plane_id SMALLINT REFERENCES Plane(plane_id) /* 1:n */

)

CREATE TABLE Garage(
	garage_id SMALLINT PRIMARY KEY,
	location VARCHAR(200),
	number_of_trams SMALLINT,
	number_of_buses SMALLINT,
	capacity SMALLINT,
	bus_id SMALLINT REFERENCES Bus(bus_id),
	trams_id SMALLINT REFERENCES Tram(tram_id)
)

CREATE TABLE Ship(
	ship_id SMALLINT PRIMARY KEY,
	first_class_number_of_seats SMALLINT,
	second_class_number_of_seats SMALLINT,
	price_first_class FLOAT,
	price_second_class FLOAT,
	departure VARCHAR(200),
	destination VARCHAR(200),
	passenger_id SMALLINT REFERENCES Passenger(passenger_id)
)

CREATE TABLE Harbor(
	harbor_id SMALLINT PRIMARY KEY,
	number_of_ships SMALLINT,
	capacity SMALLINT,
	location VARCHAR(200),
	ship_id SMALLINT REFERENCES Ship(ship_id)
)


INSERT INTO Passenger(passenger_id, name)
VALUES(1, 'Dani');

INSERT INTO Passenger(passenger_id, name)
VALUES(2, 'Alin');

INSERT INTO Passenger(passenger_id, name)
VALUES(3, 'George');

INSERT INTO Passenger(passenger_id, name)
VALUES(4, 'Maria');

INSERT INTO Passenger(passenger_id, name)
VALUES(5, 'Florin');

INSERT INTO Passenger(passenger_id, name)
VALUES(6, 'Alina');


SELECT * from Passenger;

INSERT INTO Controller(controller_id, name, rating)
VALUES(1,'Ioan',3);

INSERT INTO Controller(controller_id, name, rating)
VALUES(2,'Matei',7);

INSERT INTO Controller(controller_id, name, rating)
VALUES(3,'Georgiana',10);

INSERT INTO Controller(controller_id, name, rating)
VALUES(4,'Marius',1);

INSERT INTO Controller(controller_id, name, rating)
VALUES(5,'Ionel',5);

INSERT INTO Controller(controller_id, name, rating)
VALUES(6,'Andreea',9);

INSERT INTO Controller(controller_id, name, rating)
VALUES(7,'George',10);

SELECT * FROM Controller;

INSERT INTO ControllerPassengerRelation(passenger_id, controller_id)
VALUES(1,4);

INSERT INTO ControllerPassengerRelation(passenger_id, controller_id)
VALUES(1,5);

INSERT INTO ControllerPassengerRelation(passenger_id, controller_id)
VALUES(1,1);

INSERT INTO ControllerPassengerRelation(passenger_id, controller_id)
VALUES(2,3);

INSERT INTO ControllerPassengerRelation(passenger_id, controller_id)
VALUES(2,5);

INSERT INTO ControllerPassengerRelation(passenger_id, controller_id)
VALUES(4,6);


SELECT * FROM ControllerPassengerRelation;

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(25,'Renault',34,24.3,'Manastur','Ghiorgheni',1);

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(26,'Renault',34,24.3,'Manastur','Ghiorgheni',2);

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(27,'Renault',34,24.3,'Manastur','Ghiorgheni',3);

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(3,'Renault',34,24.3,'Gara','Ghiorgheni',4);

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(4,'Renault',34,24.3,'Gara','Ghiorgheni',5);

SELECT * FROM Bus;

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination, passenger_id)
VALUES(1, 'CFR', 40, 100, 10, 17, 'Cluj', 'Brasov', 2);

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination, passenger_id)
VALUES(2, 'CFR', 130, 150, 100, 30, 'Constanta', 'Frant', 4);

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination, passenger_id)
VALUES(3, 'CFR', 180, 300, 100, 80, 'Detroit', 'Chicago', 3);

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination, passenger_id)
VALUES(4, 'CFR', 100, 70, 30, 50, 'Bucharest', 'Mangalia', 1);

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination, passenger_id)
VALUES(5, 'CFR', 300, 140, 24, 37, 'Dorohoi', 'Lyon', 6);

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination, passenger_id)
VALUES(6, 'CFR', 400, 13, 240, 100, 'Bacau', 'Cernavoda', 5);

SELECT * FROM Train;


INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation, passenger_id)
VALUES(1, 'CTP Botosani', 100, 30, 'Piata mica', 'Gara mare', 4);

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation, passenger_id)
VALUES(2, 'CTP', 180, 5, 'Mihai Viteazu', 'Avram Iancu', 2);

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation, passenger_id)
VALUES(3, 'RATB', 150, 10, 'Arcul de Triumf', 'Tei', 5);

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation, passenger_id)
VALUES(4, 'Mara Nord', 180, 3, 'Big', 'Independentei', 1);

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation, passenger_id)
VALUES(5, 'RATBV', 130, 5, 'Livada Postei', 'Teatrul Dramatic', 6);

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation, passenger_id)
VALUES(6, 'CTP', 170, 100, 'Floresti', 'Apahida', 3);

SELECT * FROM Tram;

	
INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(1,'Christian Tour', 100, 30, 'Cluj-Napoca', 'Mihai Viteazu', 4);

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(2,'Christian Tour', 300, 50, 'Bucuresti', 'Brasov', 6);

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(3,'Christian Tour', 250, 15, 'Dorohoi', 'Iasi', 2);

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(4,'FlixBux', 170, 23, 'Chisinau', 'Cernavoda', 1);

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(5, 'FlixBus', 200, 10, 'Sibiu', 'Timisoara', 3);

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination, passenger_id)
VALUES(6, 'FlixBus', 300, 7, 'Constanta', 'Vama Veche',5);

SELECT * FROM Coach;


INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic, passenger_id)
VALUES(1, 'Wizz Air', 100, 30, 15, 70, 20, 'Cluj', 'London', 0, 4);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic, passenger_id)
VALUES(2, 'Wizz Air', 300, 150, 100, 90, 100, 'Paris', 'New York',1, 5);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic, passenger_id)
VALUES(3, 'Wizz Air', 400, 120, 40, 100, 300, 'Tokyo', 'Las Vegas', 1, 2);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic, passenger_id)
VALUES(4, 'Blue Air', 300, 100, 20, 150, 100, 'Moscova', 'Kiev', 0, 3);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic, passenger_id)
VALUES(5, 'Blue Air', 370, 50, 30, 100, 30, 'Harare', 'Cairo', 0, 1);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic, passenger_id)
VALUES(6, 'Blue Air', 400, 100, 80, 100, 30, 'Madrid', 'Chicago', 1, 6);

SELECT * FROM Plane;


INSERT INTO Airport(airport_id, location, number_of_planes, plane_id)
VALUES(1, 'Cluj-Napoca', 100, 3);

INSERT INTO Airport(airport_id, location, number_of_planes, plane_id)
VALUES(2, 'Paris', 30, 6);

INSERT INTO Airport(airport_id, location, number_of_planes, plane_id)
VALUES(3, 'Moscova', 50, 2);

INSERT INTO Airport(airport_id, location, number_of_planes, plane_id)
VALUES(4, 'Amsterdam', 100, 1);

INSERT INTO Airport(airport_id, location, number_of_planes, plane_id)
VALUES(5, 'Varsovia', 70, 4);

INSERT INTO Airport(airport_id, location, number_of_planes, plane_id)
VALUES(6, 'Viena', 300, 5);

SELECT * FROM Airport;

INSERT INTO Garage(garage_id, location, number_of_trams, number_of_buses, capacity, bus_id, trams_id)
VALUES(1, 'Moscova', 300, 100, 500, 3, 3);

INSERT INTO Garage(garage_id, location, number_of_trams, number_of_buses, capacity, bus_id, trams_id)
VALUES(2, 'Paris', 100, 200, 500, 4, 4);

INSERT INTO Garage(garage_id, location, number_of_trams, number_of_buses, capacity, bus_id, trams_id)
VALUES(3, 'Viena', 70, 30, 150, 25, 6);

INSERT INTO Garage(garage_id, location, number_of_trams, number_of_buses, capacity, bus_id, trams_id)
VALUES(4, 'Bucharest', 100, 150, 400, 26, 1);

INSERT INTO Garage(garage_id, location, number_of_trams, number_of_buses, capacity, bus_id, trams_id)
VALUES(5, 'Cluj-Napoca', 70, 130, 500, 27, 2);

INSERT INTO Garage(garage_id, location, number_of_trams, number_of_buses, capacity, bus_id, trams_id)
VALUES(6, 'Brasov', 100, 200, 700, 4, 5);

SELECT * FROM Garage;


INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination, passenger_id)
VALUES(1, 100, 20, 400, 200, 'New York', 'Porto', 3);

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination, passenger_id)
VALUES(2, 300, 150, 200, 130, 'Lisabona', 'Miami', 5);

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination, passenger_id)
VALUES(3, 200, 100, 100, 50, 'Bahamas', 'Havana', 1);

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination, passenger_id)
VALUES(4, 300, 200, 150, 39, 'Ciudad de Panama', 'Barranquilla',2);

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination, passenger_id)
VALUES(5, 100, 200, 300, 170, 'Caracas', 'Georgetown', 6);

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination, passenger_id)
VALUES(6, 300, 150, 90, 70, 'Lima', 'Rio Janeiro', 4);

SELECT * FROM Ship;


INSERT INTO Harbor(harbor_id, number_of_ships, capacity, location, ship_id)
VALUES(1, 300, 500, 'Caracas', 3);

INSERT INTO Harbor(harbor_id, number_of_ships, capacity, location, ship_id)
VALUES(2, 150, 200, 'Constanta', 5);

INSERT INTO Harbor(harbor_id, number_of_ships, capacity, location, ship_id)
VALUES(3, 200, 1400, 'Rio de Janeiro', 1);

INSERT INTO Harbor(harbor_id, number_of_ships, capacity, location, ship_id)
VALUES(4, 100, 350, 'Cape Town', 2);

INSERT INTO Harbor(harbor_id, number_of_ships, capacity, location, ship_id)
VALUES(5, 200, 751, 'Mogadishu', 6);

INSERT INTO Harbor(harbor_id, number_of_ships, capacity, location, ship_id)
VALUES(6, 100, 150, 'Colombo', 4);

SELECT * FROM Harbor;

SELECT * FROM Tram;

-- updates

UPDATE Tram 
SET departure = 'Franta'
WHERE departure = 'Piata Mica' OR departure = 'China';

UPDATE Tram 
SET company = 'CTP Iasi'
WHERE number_of_seats = 170 AND departure = 'Floresti';

UPDATE Tram
SET destionation = 'Barcelona'
WHERE destionation LIKE '%Apahid'


-- DELETE 

DELETE FROM Harbor
WHERE capacity = 500 AND location = 'Caracas';

DELETE FROM Harbor
WHERE location = 'Constanta' OR capacity = 1400;


-- sub a

SELECT TOP 4 harbor_id FROM Harbor
UNION 
SELECT bus_id FROM Bus;

SELECT TOP 5 harbor_id FROM Harbor
UNION ALL
SELECT bus_id FROM Bus;

SELECT * FROM Passenger
WHERE name = 'Dani' OR name = 'Florin';

-- sub b

SELECT passenger_id FROM Passenger
INTERSECT
SELECT bus_id FROM Bus;

SELECT passenger_id, name FROM Passenger
WHERE passenger_id IN (1,2,3);

-- sub c

SELECT passenger_id FROM Passenger
EXCEPT
SELECT bus_id FROM Bus;

SELECT passenger_id, name FROM Passenger
WHERE passenger_id NOT IN (1,2,3);

-- sub d

SELECT * FROM Passenger
INNER JOIN Controller
ON Passenger.name = Controller.name; 

SELECT * FROM Passenger
LEFT JOIN Controller
ON Passenger.name = Controller.name; 

SELECT * FROM Passenger
RIGHT JOIN Controller
ON Passenger.name = Controller.name; 

SELECT * FROM Passenger
FULL JOIN Controller
ON Passenger.name = Controller.name; 

-- sub e

SELECT name FROM Passenger
WHERE Passenger.name IN ( SELECT Controller.name FROM Controller WHERE Controller.name = 'George');

SELECT * FROM Ship
WHERE Ship.first_class_number_of_seats IN(
SELECT Coach.number_of_seats  FROM Coach
WHERE Coach.number_of_seats IN (100,300,200));

-- sub f


SELECT number_of_seats FROM Coach
WHERE EXISTS ( SELECT number_of_buses FROM Garage WHERE Garage.number_of_buses = Coach.number_of_seats AND Garage.capacity > 10);

SELECT number_of_seats FROM Coach
WHERE EXISTS ( SELECT price_first_class FROM Plane WHERE Plane.price_first_class = Coach.number_of_seats OR Plane.second_class_number_of_seats > 1000);

-- sub g

SELECT * FROM Plane;

SELECT AVG(capacitate) FROM ( SELECT SUM(capacity) AS capacitate FROM Harbor) AS average;

SELECT AVG(plane_tickets) FROM (SELECT SUM(price_first_class) AS plane_tickets FROM Plane) as average;


-- sub h



SELECT COUNT(number_of_seats)
FROM PLANE
GROUP BY first_class_number_of_seats 
HAVING COUNT(number_of_seats) > 0
ORDER BY COUNT(second_class_number_of_seats) ASC;


SELECT AVG(price_first_class)
FROM Ship
GROUP BY first_class_number_of_seats 
HAVING MAX(price_second_class) > 10;

SELECT * FROM Harbor;

SELECT MAX(capacity)
FROM Harbor
GROUP BY number_of_ships
HAVING COUNT(capacity) < 5000;

SELECT * FROM Controller;

SELECT COUNT(name)
FROM Controller
GROUP BY rating;

SELECT * FROM Garage;
SELECT * FROM AIRPORT;
-- sub i

SELECT capacity
FROM Harbor
WHERE number_of_ships = ANY
	(
	SELECT number_of_trams
	FROM Garage
	WHERE number_of_buses > 10
) ;

SELECT airport_id, plane_id
FROM Airport
WHERE number_of_planes = ANY 
(
	SELECT number_of_buses
	FROM Garage
	WHERE number_of_buses < 1000
);


SELECT capacity
FROM Harbor
WHERE number_of_ships = ALL
	(
	SELECT number_of_trams
	FROM Garage
	WHERE number_of_buses = 10
) ;

SELECT airport_id, plane_id
FROM Airport
WHERE number_of_planes = ALL
(
	SELECT number_of_buses
	FROM Garage
	WHERE number_of_buses = 1000
);

--------------------------------------------------------------------------------- LAB 3 -----------------------------------------------------------------------------------------------------------------
-- sub a

CREATE PROCEDURE setNumberOfSeatsFromBusToInt
AS
	ALTER TABLE Bus ALTER COLUMN number_of_seats INT;
	

	
SELECT DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Bus';

EXEC setNumberOfSeatsFromBusToInt; 



CREATE PROCEDURE setNumberOfSeatsFromBusToTinyInt AS
	ALTER TABLE Bus ALTER COLUMN number_of_seats TINYINT;
	
	
EXEC setNumberOfSeatsFromBusToTinyInt; 

-- sub b

CREATE PROCEDURE addYearOfProductionToBus AS
	ALTER TABLE Bus ADD year_of_production TINYINT;


EXEC addYearOfProductionToBus;

CREATE PROCEDURE removeYearOfProductionToBus AS
	ALTER TABLE Bus DROP COLUMN year_of_production;

EXEC removeYearOfProductionToBus; 


-- sub c

CREATE PROCEDURE addDefaultToTransatlanticFromPlane AS
	ALTER TABLE Plane ADD CONSTRAINT DEFAULT0 DEFAULT(0) FOR transatlantic;

CREATE PROCEDURE removeDefaultTransatlanticFromPlane AS
	ALTER TABLE Plane DROP CONSTRAINT DEFAULT0;

-- sub g

CREATE PROCEDURE createTrolleybus AS
	CREATE TABLE Trolleybus(
		company VARCHAR(100) NOT NULL,
		departure VARCHAR(100),
		destination VARCHAR(100),
		trolleybus_id INT NOT NULL
	);

CREATE PROCEDURE dropTrolleybus AS
	DROP TABLE Trolleybus;



EXEC dropTrolleybus; 
EXEC createTrolleybus;

-- sub d

CREATE PROCEDURE addTrolleybus_idPrimaryKey AS
	ALTER TABLE Trolleybus 
		ADD CONSTRAINT TROLLEYBUS_PRIMARY_KEY PRIMARY KEY(trolleybus_id);

EXEC addTrolleybus_idPrimaryKey;
	
CREATE PROCEDURE removeTrolleybus_idPrimaryKey AS
	ALTER TABLE Trolleybus
		DROP CONSTRAINT TROLLEYBUS_PRIMARY_KEY;
	
EXEC removeTrolleybus_idPrimaryKey; 

-- Sub e

CREATE PROCEDURE createCandidateKeyForTrolleybus AS
	ALTER TABLE Trolleybus
		DROP CONSTRAINT TROLLEYBUS_PRIMARY_KEY
	ALTER TABLE Trolleybus
		ADD CONSTRAINT TROLLEYBUS_PRIMARY_KEY PRIMARY KEY(company, trolleybus_id);

EXEC createCandidateKeyForTrolleyBus;
	

CREATE PROCEDURE removeCandidateKeyForTrolleyBus AS
	ALTER TABLE Trolleybus
		DROP CONSTRAINT TROLLEYBUS_PRIMARY_KEY
	ALTER TABLE Trolleybus
		ADD CONSTRAINT TROLLEYBUS_PRIMARY_KEY PRIMARY KEY(trolleybus_id);


	
-- sub f
	
ALTER TABLE Trolleybus ADD passenger_id SMALLINT NOT NULL;

SELECT * FROM Trolleybus;
	
CREATE PROCEDURE addForeignKeyForTrolleyBus AS
	ALTER TABLE Trolleybus
		ADD CONSTRAINT passenger_id FOREIGN KEY(passenger_id) REFERENCES Passenger(passenger_id);
	
EXEC addForeignKeyForTrolleyBus; 
	
CREATE PROCEDURE deleteForeignKeyForTrolleyBus AS
	ALTER TABLE Trolleybus
		DROP CONSTRAINT passenger_id;

EXEC deleteForeignKeyForTrolleyBus; 



----- MAIN !!!!

CREATE PROCEDURE createProceduresTable AS
	CREATE TABLE ProceduresTable(
		fromVersion INT,
		toVersion INT,
		nameProcedure VARCHAR(200)
		PRIMARY KEY(fromVersion, toVersion)
	);


EXEC createProceduresTable;

SELECT * FROM ProceduresTable;

INSERT INTO ProceduresTable VALUES(1, 2, 'setNumberOfSeatsFromBusToInt');
INSERT INTO ProceduresTable VALUES(2, 1, 'setNumberOfSeatsFromBusToTinyInt');
INSERT INTO ProceduresTable VALUES(2, 3, 'addYearOfProductionToBus');
INSERT INTO ProceduresTable VALUES(3, 2, 'removeYearOfProductionToBus');
INSERT INTO ProceduresTable VALUES(3, 4, 'addDefaultToTransatlanticFromPlane');
INSERT INTO ProceduresTable VALUES(4, 3, 'removeDefaultTransatlanticFromPlane');
INSERT INTO ProceduresTable VALUES(4, 5, 'createTrolleybus');
INSERT INTO ProceduresTable VALUES(5, 4, 'dropTrolleybus');
INSERT INTO ProceduresTable VALUES(5, 6, 'addTrolleybus_idPrimaryKey');
INSERT INTO ProceduresTable VALUES(6, 5, 'removeTrolleybus_idPrimaryKey');
INSERT INTO ProceduresTable VALUES(6, 7, 'createCandidateKeyForTrolleybus');
INSERT INTO ProceduresTable VALUES(7, 6, 'removeCandidateKeyForTrolleyBus');
INSERT INTO ProceduresTable VALUES(7, 8, 'addForeignKeyForTrolleyBus');
INSERT INTO ProceduresTable VALUES(8, 7, 'deleteForeignKeyForTrolleyBus');



CREATE TABLE VERSION_TABLE(
	version int,
	PRIMARY KEY(version)
);

INSERT INTO VERSION_TABLE VALUES(1);



CREATE PROCEDURE goToVersion(@newVersion INT) AS
	DECLARE @curr int
	DECLARE @procedureName varchar(255)
	SELECT @curr=version FROM VERSION_TABLE
	IF @newVersion > (SELECT max(toVersion) FROM ProceduresTable)
		RAISERROR ('Version does not exist', 10, 1)
	
	IF @newVersion < (SELECT min(fromVersion) FROM ProceduresTable)
		RAISERROR ('Version does not exist', 10, 1)
	
	WHILE @curr < @newVersion BEGIN
		SELECT @procedureName=nameProcedure FROM ProceduresTable WHERE @curr=fromVersion AND @curr+1=toVersion
		EXEC (@procedureName)
		SET @curr=@curr+1
		UPDATE VERSION_TABLE SET version=@curr
	END
	
	WHILE @curr > @newVersion BEGIN
		SELECT @procedureName=nameProcedure FROM ProceduresTable WHERE @curr=fromVersion AND @curr-1=toVersion
		EXEC (@procedureName)
		SET @curr=@curr-1
		UPDATE VERSION_TABLE SET version=@curr
	END; 

DROP PROCEDURE goToVersion;

SELECT * FROM VERSION_TABLE;

EXEC goToVersion 4;


