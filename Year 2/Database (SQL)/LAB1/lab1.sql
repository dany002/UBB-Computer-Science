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



















