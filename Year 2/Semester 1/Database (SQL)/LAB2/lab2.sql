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

