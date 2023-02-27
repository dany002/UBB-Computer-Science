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

