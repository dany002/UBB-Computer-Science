CREATE DATABASE PublicTransport;

CREATE TABLE Controller(
	controller_id SMALLINT PRIMARY KEY,
	name VARCHAR(200),
	rating TINYINT NOT NULL,
	CHECK (rating BETWEEN 1 AND 10)
)

CREATE TABLE Passenger(
	passenger_id SMALLINT PRIMARY KEY,
	name VARCHAR(200)
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
  	destination VARCHAR(200)
)

CREATE TABLE Train( 
	train_id SMALLINT PRIMARY KEY,
	company VARCHAR(80),
	number_of_seats SMALLINT,
	price FLOAT,
	first_class_number_of_seats SMALLINT,
	second_class_number_of_seats SMALLINT,
	departure VARCHAR(200),
	destination VARCHAR(200)
)

CREATE TABLE Tram(
	tram_id SMALLINT PRIMARY KEY,
	company VARCHAR(200),
	number_of_seats SMALLINT,
	price FLOAT,
	departure VARCHAR(200),
	destionation VARCHAR(200)
)

CREATE TABLE Coach(
	coach_id SMALLINT PRIMARY KEY,
	company VARCHAR(200),
	number_of_seats SMALLINT,
	price FLOAT,
	departure VARCHAR(200),
	destination VARCHAR(200)
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
	transatlantic BIT
)



CREATE TABLE Airport(
	airport_id SMALLINT PRIMARY KEY,
	location VARCHAR(200),
	number_of_planes SMALLINT,
	plane_id SMALLINT NOT NULL,
	CONSTRAINT FK_plane_id
		FOREIGN KEY (plane_id)
		REFERENCES Plane(plane_id)
		ON DELETE CASCADE
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
	destination VARCHAR(200)
)

CREATE TABLE Harbor(
	harbor_id SMALLINT PRIMARY KEY,
	number_of_ships SMALLINT,
	capacity SMALLINT,
	location VARCHAR(200),
	ship_id SMALLINT REFERENCES Ship(ship_id)
)

CREATE TABLE Trip(
	trip_id INT PRIMARY KEY,
	passenger_id SMALLINT REFERENCES Passenger(passenger_id) NOT NULL,
	bus_id SMALLINT REFERENCES Bus(bus_id),
	train_id SMALLINT REFERENCES Train(train_id),
	tram_id SMALLINT REFERENCES Tram(tram_id),
	coach_id SMALLINT REFERENCES Coach(coach_id),
	plane_id SMALLINT REFERENCES Plane(plane_id),
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

INSERT INTO Passenger(passenger_id, name)
VALUES(7, 'Sara');

INSERT INTO Passenger(passenger_id, name)
VALUES(8, 'Tania');

INSERT INTO Passenger(passenger_id, name)
VALUES(9, 'Diana');

INSERT INTO Passenger(passenger_id, name)
VALUES(10, 'Denisa');

INSERT INTO Passenger(passenger_id, name)
VALUES(11, 'Georgiana');

INSERT INTO Passenger(passenger_id, name)
VALUES(12, 'Iulia');

INSERT INTO Passenger(passenger_id, name)
VALUES(13, 'Daria');

INSERT INTO Passenger(passenger_id, name)
VALUES(14, 'Sabina');

INSERT INTO Passenger(passenger_id, name)
VALUES(15, 'Anca');

INSERT INTO Passenger(passenger_id, name)
VALUES(16, 'Dragos');

INSERT INTO Passenger(passenger_id, name)
VALUES(17, 'Ioan');

INSERT INTO Passenger(passenger_id, name)
VALUES(18, 'Vlad');



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

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination)
VALUES(25,'Renault',34,24.3,'Manastur','Ghiorgheni');

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination)
VALUES(26,'Renault',34,24.3,'Manastur','Ghiorgheni');

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination)
VALUES(27,'Renault',34,24.3,'Manastur','Ghiorgheni');

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination)
VALUES(3,'Renault',34,24.3,'Gara','Ghiorgheni');

INSERT INTO Bus(bus_id, company, number_of_seats, price, departure, destination)
VALUES(4,'Renault',34,24.3,'Gara','Ghiorgheni');

SELECT * FROM Bus;

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination)
VALUES(1, 'CFR', 40, 100, 10, 17, 'Cluj', 'Brasov');

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination)
VALUES(2, 'CFR', 130, 150, 100, 30, 'Constanta', 'Frant');

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination)
VALUES(3, 'CFR', 180, 300, 100, 80, 'Detroit', 'Chicago');

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination)
VALUES(4, 'CFR', 100, 70, 30, 50, 'Bucharest', 'Mangalia');

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination)
VALUES(5, 'CFR', 300, 140, 24, 37, 'Dorohoi', 'Lyon');

INSERT INTO Train(train_id, company, number_of_seats, price, first_class_number_of_seats, second_class_number_of_seats, departure, destination)
VALUES(6, 'CFR', 400, 13, 240, 100, 'Bacau', 'Cernavoda');

SELECT * FROM Train;


INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation)
VALUES(1, 'CTP Botosani', 100, 30, 'Piata mica', 'Gara mare');

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation)
VALUES(2, 'CTP', 180, 5, 'Mihai Viteazu', 'Avram Iancu');

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation)
VALUES(3, 'RATB', 150, 10, 'Arcul de Triumf', 'Tei');

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation)
VALUES(4, 'Mara Nord', 180, 3, 'Big', 'Independentei');

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation)
VALUES(5, 'RATBV', 130, 5, 'Livada Postei', 'Teatrul Dramatic');

INSERT INTO Tram(tram_id, company, number_of_seats, price, departure, destionation)
VALUES(6, 'CTP', 170, 100, 'Floresti', 'Apahida');

SELECT * FROM Tram;

	
INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination)
VALUES(1,'Christian Tour', 100, 30, 'Cluj-Napoca', 'Mihai Viteazu');

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination)
VALUES(2,'Christian Tour', 300, 50, 'Bucuresti', 'Brasov');

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination)
VALUES(3,'Christian Tour', 250, 15, 'Dorohoi', 'Iasi');

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination)
VALUES(4,'FlixBux', 170, 23, 'Chisinau', 'Cernavoda');

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination)
VALUES(5, 'FlixBus', 200, 10, 'Sibiu', 'Timisoara');

INSERT INTO Coach(coach_id, company, number_of_seats, price, departure, destination)
VALUES(6, 'FlixBus', 300, 7, 'Constanta', 'Vama Veche');

SELECT * FROM Coach;


INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic)
VALUES(1, 'Wizz Air', 100, 30, 15, 70, 20, 'Cluj', 'London', 0);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic)
VALUES(2, 'Wizz Air', 300, 150, 100, 90, 100, 'Paris', 'New York',1);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic)
VALUES(3, 'Wizz Air', 400, 120, 40, 100, 300, 'Tokyo', 'Las Vegas', 1);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic)
VALUES(4, 'Blue Air', 300, 100, 20, 150, 100, 'Moscova', 'Kiev', 0);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic)
VALUES(5, 'Blue Air', 370, 50, 30, 100, 30, 'Harare', 'Cairo', 0);

INSERT INTO Plane(plane_id, company, number_of_seats, price_first_class, price_second_class, first_class_number_of_seats, second_class_number_of_seats, departure, destination, transatlantic)
VALUES(6, 'Blue Air', 400, 100, 80, 100, 30, 'Madrid', 'Chicago', 1);

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


INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination)
VALUES(1, 100, 20, 400, 200, 'New York', 'Porto');

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination)
VALUES(2, 300, 150, 200, 130, 'Lisabona', 'Miami');

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination)
VALUES(3, 200, 100, 100, 50, 'Bahamas', 'Havana');

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination)
VALUES(4, 300, 200, 150, 39, 'Ciudad de Panama', 'Barranquilla');

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination)
VALUES(5, 100, 200, 300, 170, 'Caracas', 'Georgetown');

INSERT INTO Ship(ship_id, first_class_number_of_seats, second_class_number_of_seats, price_first_class, price_second_class, departure, destination)
VALUES(6, 300, 150, 90, 70, 'Lima', 'Rio Janeiro');

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

SELECT * FROM Bus;

SELECT * FROM Harbor;

SELECT * FROM Tram;

SELECT * FROM Trip;

SELECT * FROM Train;

SELECT * FROM Coach;

INSERT INTO Trip(trip_id,passenger_id,bus_id)
VALUES(1,18,25);

INSERT INTO Trip(trip_id,passenger_id,bus_id)
VALUES(2,17,25);

INSERT INTO Trip(trip_id,passenger_id,bus_id)
VALUES(3,16,25);

INSERT INTO Trip(trip_id,passenger_id,bus_id)
VALUES(4,15,3);

INSERT INTO Trip(trip_id,passenger_id,train_id)
VALUES(5,14,5);

INSERT INTO Trip(trip_id,passenger_id, train_id)
VALUES(6,13,5);

INSERT INTO Trip(trip_id,passenger_id, train_id)
VALUES(7,12,6);

INSERT INTO Trip(trip_id,passenger_id, train_id)
VALUES(8,11,6);

INSERT INTO Trip(trip_id,passenger_id,tram_id)
VALUES(9,10,6);

INSERT INTO Trip(trip_id,passenger_id, tram_id)
VALUES(10,9,6);

INSERT INTO Trip(trip_id,passenger_id, coach_id)
VALUES(11,8,3);

INSERT INTO Trip(trip_id,passenger_id, coach_id)
VALUES(12,7,3);

INSERT INTO Trip(trip_id,passenger_id, plane_id)
VALUES(13,6,2);

INSERT INTO Trip(trip_id, passenger_id, plane_id)
VALUES(14,5,2);

INSERT INTO Trip(trip_id, passenger_id, ship_id)
VALUES(15,4,5);

INSERT INTO Trip(trip_id, passenger_id, ship_id)
VALUES(16,3,4);

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

SELECT * FROM Bus;

EXEC goToVersion 2;

-------------------------------------------------------------------------- LAB 4 ---------------------------------------------------------------------

-- tests

IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestRunTables_Tables]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
	ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_Tables;



IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestTables_Tables]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tables;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestRunTables_TestRuns]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_TestRuns;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestRunViews_TestRuns]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_TestRuns;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestTables_Tests]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tests;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestViews_Tests]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Tests;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestRunViews_Views]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_Views;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[FK_TestViews_Views]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Views;


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[Tables]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [Tables];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[TestRunTables]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [TestRunTables];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[TestRunViews]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [TestRunViews];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[TestRuns]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [TestRuns];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[TestTables]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [TestTables];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[TestViews]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [TestViews];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[Tests]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [Tests];


IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = object_id(N'[Views]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [Views];



CREATE TABLE [Tables] (
	[TableID] [int] IDENTITY (1, 1) NOT NULL ,
	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 
) ON [PRIMARY];


CREATE TABLE [TestRunTables] (
	[TestRunID] [int] NOT NULL ,
	[TableID] [int] NOT NULL ,
	[StartAt] [datetime] NOT NULL ,
	[EndAt] [datetime] NOT NULL 
) ON [PRIMARY];


CREATE TABLE [TestRunViews] (
	[TestRunID] [int] NOT NULL ,
	[ViewID] [int] NOT NULL ,
	[StartAt] [datetime] NOT NULL ,
	[EndAt] [datetime] NOT NULL 
) ON [PRIMARY];


CREATE TABLE [TestRuns] (
	[TestRunID] [int] IDENTITY (1, 1) NOT NULL ,
	[Description] [nvarchar] (2000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
	[StartAt] [datetime] NULL ,
	[EndAt] [datetime] NULL 
) ON [PRIMARY];


CREATE TABLE [TestTables] (
	[TestID] [int] NOT NULL ,
	[TableID] [int] NOT NULL ,
	[NoOfRows] [int] NOT NULL ,
	[Position] [int] NOT NULL 
) ON [PRIMARY];


CREATE TABLE [TestViews] (
	[TestID] [int] NOT NULL ,
	[ViewID] [int] NOT NULL 
) ON [PRIMARY];


CREATE TABLE [Tests] (
	[TestID] [int] IDENTITY (1, 1) NOT NULL ,
	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 
) ON [PRIMARY];


CREATE TABLE [Views] (
	[ViewID] [int] IDENTITY (1, 1) NOT NULL ,
	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 
) ON [PRIMARY];


ALTER TABLE [Tables] WITH NOCHECK ADD 
	CONSTRAINT [PK_Tables] PRIMARY KEY  CLUSTERED 
	(
		[TableID]
	)  ON [PRIMARY] ;


ALTER TABLE [TestRunTables] WITH NOCHECK ADD 
	CONSTRAINT [PK_TestRunTables] PRIMARY KEY  CLUSTERED 
	(
		[TestRunID],
		[TableID]
	)  ON [PRIMARY] ;


ALTER TABLE [TestRunViews] WITH NOCHECK ADD 
	CONSTRAINT [PK_TestRunViews] PRIMARY KEY  CLUSTERED 
	(
		[TestRunID],
		[ViewID]
	)  ON [PRIMARY] ;


ALTER TABLE [TestRuns] WITH NOCHECK ADD 
	CONSTRAINT [PK_TestRuns] PRIMARY KEY  CLUSTERED 
	(
		[TestRunID]
	)  ON [PRIMARY] ;


ALTER TABLE [TestTables] WITH NOCHECK ADD 
	CONSTRAINT [PK_TestTables] PRIMARY KEY  CLUSTERED 
	(
		[TestID],
		[TableID]
	)  ON [PRIMARY] ;


ALTER TABLE [TestViews] WITH NOCHECK ADD 
	CONSTRAINT [PK_TestViews] PRIMARY KEY  CLUSTERED 
	(
		[TestID],
		[ViewID]
	)  ON [PRIMARY] ;


ALTER TABLE [Tests] WITH NOCHECK ADD 
	CONSTRAINT [PK_Tests] PRIMARY KEY  CLUSTERED 
	(
		[TestID]
	)  ON [PRIMARY] ;


ALTER TABLE [Views] WITH NOCHECK ADD 
	CONSTRAINT [PK_Views] PRIMARY KEY  CLUSTERED 
	(
		[ViewID]
	)  ON [PRIMARY] ;


ALTER TABLE [TestRunTables] ADD 
	CONSTRAINT [FK_TestRunTables_Tables] FOREIGN KEY 
	(
		[TableID]
	) REFERENCES [Tables] (
		[TableID]
	) ON DELETE CASCADE  ON UPDATE CASCADE ,
	CONSTRAINT [FK_TestRunTables_TestRuns] FOREIGN KEY 
	(
		[TestRunID]
	) REFERENCES [TestRuns] (
		[TestRunID]
	) ON DELETE CASCADE  ON UPDATE CASCADE ;


ALTER TABLE [TestRunViews] ADD 
	CONSTRAINT [FK_TestRunViews_TestRuns] FOREIGN KEY 
	(
		[TestRunID]
	) REFERENCES [TestRuns] (
		[TestRunID]
	) ON DELETE CASCADE  ON UPDATE CASCADE ,
	CONSTRAINT [FK_TestRunViews_Views] FOREIGN KEY 
	(
		[ViewID]
	) REFERENCES [Views] (
		[ViewID]
	) ON DELETE CASCADE  ON UPDATE CASCADE ;


ALTER TABLE [TestTables] ADD 
	CONSTRAINT [FK_TestTables_Tables] FOREIGN KEY 
	(
		[TableID]
	) REFERENCES [Tables] (
		[TableID]
	) ON DELETE CASCADE  ON UPDATE CASCADE ,
	CONSTRAINT [FK_TestTables_Tests] FOREIGN KEY 
	(
		[TestID]
	) REFERENCES [Tests] (
		[TestID]
	) ON DELETE CASCADE  ON UPDATE CASCADE ;


ALTER TABLE [TestViews] ADD 
	CONSTRAINT [FK_TestViews_Tests] FOREIGN KEY 
	(
		[TestID]
	) REFERENCES [Tests] (
		[TestID]
	),
	CONSTRAINT [FK_TestViews_Views] FOREIGN KEY 
	(
		[ViewID]
	) REFERENCES [Views] (
		[ViewID]
	);





CREATE PROCEDURE addToTables (@tableName VARCHAR(255)) AS
	IF @tableName NOT IN (SELECT TABLE_NAME  FROM INFORMATION_SCHEMA.TABLES) BEGIN
		PRINT 'Table doesn''t exist'
		RETURN 
	END
	IF @tableName IN (SELECT Name FROM Tables) BEGIN
		PRINT 'Table already in Tables'
		RETURN 
	END
	INSERT INTO Tables(Name) Values (@tableName);



CREATE PROCEDURE addToViews(@viewName VARCHAR(255)) AS 
	IF @viewName NOT IN (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS) BEGIN
		PRINT 'View doesn''t exist'
		RETURN 
	END
	IF @viewName IN (SELECT Name FROM Views) BEGIN
		PRINT 'View already in views'
		RETURN 
	END
	INSERT INTO Views(Name) Values (@viewName);



CREATE PROCEDURE addToTests(@testName VARCHAR(255)) AS 
	IF @testName IN (SELECT Name FROM Tests) BEGIN
		PRINT 'Test already in tests'
		RETURN 
	END
	INSERT INTO Tests(Name) Values (@testName);



CREATE PROCEDURE connectTableToTest(@tableName VARCHAR(255), @testName VARCHAR(255), @rows INT, @pos INT) AS
	IF @tableName NOT IN (SELECT Name FROM Tables) BEGIN
		PRINT 'Table not in Tables'
		RETURN 
	END
	IF @testName NOT IN (SELECT Name FROM Tests) BEGIN
		PRINT 'Test not in tests'
		RETURN 
	END 
	DECLARE @tableId int
	DECLARE @testId int
	SET @tableId = (SELECT TableID FROM Tables WHERE Name=@tableName)
	SET @testId = (SELECT TestID FROM Tests WHERE Name=@testName)
	IF EXISTS(SELECT * FROM TestTables WHERE TestId=@testId AND TableId=@tableId) BEGIN 
		PRINT 'TestTable connection already exists'
	END
	
	INSERT INTO TestTables VALUES(@testId, @tableId, @rows, @pos);
	

CREATE PROCEDURE connectViewToTest(@viewName VARCHAR(255), @testName VARCHAR(255)) AS
	IF @viewName NOT IN (SELECT Name FROM Views) BEGIN
		PRINT 'Table not in Tables'
		RETURN 
	END
	IF @testName NOT IN (SELECT Name FROM Tests) BEGIN
		PRINT 'Test not in tests'
		RETURN 
	END 
	DECLARE @viewId int
	DECLARE @testId int
	SET @viewId = (SELECT ViewID FROM Views WHERE Name=@viewName)
	SET @testId = (SELECT TestID FROM Tests WHERE Name=@testName)
	IF EXISTS(SELECT * FROM TestViews WHERE TestId=@testId AND ViewID=@viewId) BEGIN 
		PRINT 'TestView connection already exists'
	END
	
	INSERT INTO TestViews  VALUES(@testId, @viewId);
	


CREATE PROCEDURE runTest(@testName VARCHAR(255), @description VARCHAR(255)) AS
	IF @testName NOT IN (SELECT Name FROM TESTS) BEGIN
		PRINT 'test not in Tests'
		RETURN
	END
	
	
	DECLARE @testStartTime DATETIME2
	DECLARE @testRunId INT
	DECLARE @tableId INT
	DECLARE @table VARCHAR(255)
	DECLARE @rows INT
	DECLARE @pos INT
	DECLARE @command VARCHAR(255)
	DECLARE @tableInsertStartTime DATETIME2
	DECLARE @tableInsertEndTime DATETIME2
	DECLARE @testId INT
	DECLARE @view VARCHAR(255)
	DECLARE @viewId INT
	DECLARE @viewStartTime DATETIME2
	DECLARE @viewEndTime DATETIME2
	
	SET @testId = (SELECT TestId FROM Tests T WHERE T.Name = @testName)
	
	DECLARE tableCursor CURSOR SCROLL FOR 
		SELECT T1.Name, T1.TableId, T2.NoOfRows, T2.Position
		FROM Tables T1 INNER JOIN TestTables T2 ON T1.TableID = T2.TableID
		WHERE T2.TestID = @testId
		ORDER BY T2.Position ASC
	
	DECLARE viewCursor CURSOR SCROLL FOR 
		SELECT V.Name, V.ViewId
		FROM Views V INNER JOIN TestViews TV ON V.ViewID = TV.ViewID 
		WHERE TV.TestID = @testId
	
	
	SET @testStartTime = sysdatetime()
	
	INSERT INTO TestRuns(Description, StartAt, EndAt) VALUES(@description, @testStartTime, @testStartTime)
	SET @testRunId = SCOPE_IDENTITY()
	
	OPEN tableCursor
	FETCH FIRST FROM tableCursor INTO @table, @tableId, @rows, @pos
	
	WHILE @@FETCH_STATUS = 0 BEGIN
		EXEC ('DELETE FROM ' + @table)
		FETCH tableCursor INTO @table, @tableId, @rows, @pos
	END
	
	FETCH LAST FROM tableCursor INTO @table, @tableId, @rows, @pos
	WHILE @@FETCH_STATUS = 0 BEGIN
		SET @command = 'populateTable' + @table
		IF @rows > 0 AND @command NOT IN (SELECT ROUTINE_NAME FROM INFORMATION_SCHEMA.ROUTINES) BEGIN
			PRINT @command + 'does not exist'
			RETURN
		END
		SET @tableInsertStartTime = sysdatetime()
		IF @rows > 0 BEGIN
			EXEC @command @rows
		END
		SET @tableInsertEndTime = sysdatetime()
		INSERT INTO TestRunTables VALUES(@testRunId, @tableId, @tableInsertStartTime, @tableInsertEndTime)
		FETCH PRIOR FROM tableCursor INTO @table, @tableId, @rows, @pos
	END
	CLOSE tableCursor
	DEALLOCATE tableCursor 
	
	OPEN viewCursor
	FETCH viewCursor INTO @view, @viewId
	
	WHILE @@FETCH_STATUS = 0 BEGIN
		SET @viewStartTime = sysdatetime()
		EXEC ('SELECT * FROM ' + @view)
		SET @viewEndTime = sysdatetime()
		INSERT INTO TestRunViews VALUES(@testRunID, @viewId, @viewStartTime, @viewEndTime)
		FETCH viewCursor INTO @view, @viewId	
	END
	CLOSE viewCursor 
	DEALLOCATE viewCursor
	UPDATE TestRuns 
	SET EndAt = sysdatetime()
	WHERE TestRunID = @testRunId;



CREATE VIEW Passenger_VIEW AS
	SELECT * FROM Passenger;

CREATE PROCEDURE populateTablePassenger (@rows INT) AS
	WHILE @rows > 0 BEGIN
		INSERT INTO Passenger VALUES(@rows,'test_' + CONVERT(VARCHAR(255),@rows))
		SET @rows = @rows - 1
	END;
	


SELECT * FROM Passenger p ;
DELETE FROM Passenger where passenger_id >= 0;

EXEC addToTables 'ControllerPassengerRelation';
EXEC addToTables 'Passenger';
EXEC addToViews 'Passenger_VIEW';
EXEC addToTests 'Passenger_TEST';
EXEC connectTableToTest 'Passenger', 'Passenger_TEST', 200, 1;
EXEC connectViewToTest 'Passenger_VIEW', 'Passenger_TEST'; 

EXEC runTest 'Passenger_TEST', 'Test1';

ALTER TABLE ControllerPassengerRelation 
drop CONSTRAINT FK__Controlle__passe__2A6B46EF;


ALTER TABLE ControllerPassengerRelation 
ADD CONSTRAINT fk_controller_id
    FOREIGN KEY (controller_id)
    REFERENCES Passenger
        (passenger_id)
    ON DELETE CASCADE;

ALTER TABLE Trip
drop CONSTRAINT FK__Trip__bus_id__442B18F2;
   
ALTER TABLE Trip 
ADD CONSTRAINT FK__Trip__bus_id__442B18F2
	FOREIGN KEY(bus_id)
	REFERENCES Bus(bus_id)
	ON DELETE CASCADE;

ALTER TABLE Trip
drop CONSTRAINT FK__Trip__passenger___4336F4B9;
   
ALTER TABLE Trip 
ADD CONSTRAINT FK__Trip__passenger___4336F4B9
	FOREIGN KEY(passenger_id)
	REFERENCES Passenger(passenger_id)
	ON DELETE CASCADE;


DELETE FROM ControllerPassengerRelation ;

SELECT * FROM ControllerPassengerRelation;

CREATE VIEW ControllerPassengerRelation_VIEW AS
	SELECT p.passenger_id

SELECT * FROM Plane;
SELECT * FROM Airport;

CREATE VIEW Plane_Airport_View AS
	SELECT p.number_of_seats AS Seats, a.number_of_planes AS Planes
	FROM Plane p INNER JOIN Airport a ON p.plane_id = a.airport_id ;


CREATE PROCEDURE populateTablePlane (@rows INT) AS
	WHILE @rows > 0 BEGIN 
		INSERT INTO Plane VALUES(@rows, 'test_' + CONVERT(VARCHAR(255), @rows), @rows, @rows, @rows, @rows, @rows, 'test_' + CONVERT(VARCHAR(255), @rows), 'test_' + CONVERT(VARCHAR(255),@rows), 0)
		SET @rows = @rows - 1
	END;

CREATE PROCEDURE populateTableAirport (@rows INT) AS
	WHILE @rows > 0 BEGIN
		INSERT INTO Airport VALUES(@rows, 'test_' + CONVERT(VARCHAR(255),@rows), @rows, @rows)
		SET @rows = @rows - 1
	END;




ALTER TABLE Trip
drop CONSTRAINT FK__Trip__plane_id__47FBA9D6;


ALTER TABLE Trip
ADD CONSTRAINT fk_planee_id
    FOREIGN KEY (plane_id)
    REFERENCES Plane
        (plane_id)
    ON DELETE CASCADE;


SELECT * FROM Airport;
SELECT * FROM Plane;

DELETE FROM Airport ;
DELETE FROM Plane ;

SELECT * FROM TestTables;
DELETE FROM TestTables WHERE TestTables.[TestID] = 2;



EXEC addToTests 'Test 2';
EXEC addToTables 'Plane';
EXEC addToTables 'Airport';
EXEC addToViews 'Plane_Airport_View';
EXEC connectTableToTest 'Plane', 'Test 2', 100, 2;
EXEC connectTableToTest 'Airport', 'Test 2', 10, 1;
EXEC connectViewToTest 'Plane_Airport_View', 'Test 2';

EXEC runTest 'Test 2', 'test 2';


SELECT * FROM Tram;

CREATE PROCEDURE populateTableBus (@rows INT) AS
	WHILE @rows > 0 BEGIN 
		INSERT INTO Bus VALUES(@rows, 'test_' + CONVERT(VARCHAR(255), @rows), @rows, @rows, 'test_' + CONVERT(VARCHAR(255), @rows), 'test_' + CONVERT(VARCHAR(255),@rows))
		SET @rows = @rows - 1
	END;

CREATE PROCEDURE populateTableCoach (@rows INT) AS
	WHILE @rows > 0 BEGIN
		INSERT INTO Coach VALUES(@rows, 'test_' + CONVERT(VARCHAR(255),@rows), @rows, @rows, 'test_' + CONVERT(VARCHAR(255),@rows), 'test_' + CONVERT(VARCHAR(255),@rows))
		SET @rows = @rows - 1
	END;

CREATE PROCEDURE populateTableShip (@rows INT) AS
	WHILE @rows > 0 BEGIN
		INSERT INTO Ship VALUES(@rows, @rows, @rows, @rows, @rows ,'test_' + CONVERT(VARCHAR(255),@rows), 'test_' + CONVERT(VARCHAR(255),@rows))
		SET @rows = @rows - 1
	END;

CREATE PROCEDURE populateTableTrain (@rows INT) AS
	WHILE @rows > 0 BEGIN
		INSERT INTO Train VALUES(@rows, 'test_' + CONVERT(VARCHAR(255),@rows), @rows, @rows, @rows, @rows, 'test_' + CONVERT(VARCHAR(255),@rows), 'test_' + CONVERT(VARCHAR(255),@rows))
		SET @rows = @rows - 1
	END;

CREATE PROCEDURE populateTableTram (@rows INT) AS
	WHILE @rows > 0 BEGIN
		INSERT INTO Tram VALUES(@rows, 'test_' + CONVERT(VARCHAR(255),@rows), @rows, @rows, 'test_' + CONVERT(VARCHAR(255),@rows), 'test_' + CONVERT(VARCHAR(255),@rows))
		SET @rows = @rows - 1
	END;


CREATE VIEW Trip_VIEW AS
	SELECT * FROM Trip;


EXEC addToTests 'Test 3';
EXEC addToTables 'Bus';
EXEC addToTables 'Ship';
EXEC addToTables 'Coach';
EXEC addToTables 'Passenger';
EXEC addToTables 'Train';
EXEC addToTables 'Tram';
EXEC addToTables 'Plane';
EXEC addToViews 'Trip_VIEW';
EXEC connectTableToTest 'Plane', 'Test 3', 100, 2;
EXEC connectTableToTest 'Bus', 'Test 3', 100, 1;
EXEC connectTableToTest 'Coach', 'Test 3', 100, 3;
EXEC connectTableToTest 'Passenger', 'Test 3', 100, 4;
EXEC connectTableToTest 'Train', 'Test 3', 100, 5;
EXEC connectTableToTest 'Tram', 'Test 3', 100, 6;
EXEC connectViewToTest 'Trip_VIEW', 'Test 3';
EXEC runTest 'Test 3', 'test 3';


ALTER TABLE Garage
drop CONSTRAINT FK__Garage__bus_id__3AA1AEB8;


ALTER TABLE Garage
ADD CONSTRAINT FK__Garage__bus_id__3AA1AEB8
    FOREIGN KEY (bus_id)
    REFERENCES Bus
        (bus_id)
    ON DELETE CASCADE;
   
ALTER TABLE Garage
drop CONSTRAINT FK__Garage__trams_id__3B95D2F1;


ALTER TABLE Garage
ADD CONSTRAINT FK__Garage__trams_id__3B95D2F1
    FOREIGN KEY (trams_id)
    REFERENCES Tram
        (tram_id)
    ON DELETE CASCADE;

