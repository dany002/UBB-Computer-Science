CREATE DATABASE PublicTransportTransact;

CREATE TABLE Controller(
	controller_id INT IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR(200),
	rating INT NOT NULL,
	CHECK (rating BETWEEN 1 AND 10)
)

CREATE TABLE Passenger(
	passenger_id INT IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR(200)
)

CREATE TABLE ControllerPassengerRelation(
	passenger_id INT NOT NULL,
	controller_id INT NOT NULL,
	CONSTRAINT FK_passenger_id
		FOREIGN KEY (passenger_id)
		REFERENCES Passenger(passenger_id)
		ON DELETE CASCADE,
	CONSTRAINT FK_controller_id
		FOREIGN KEY (controller_id)
		REFERENCES Controller(controller_id)
		ON DELETE CASCADE,
	UNIQUE (passenger_id, controller_id)
)

INSERT INTO Passenger
VALUES('Dani');

INSERT INTO Passenger
VALUES('Alin');

INSERT INTO Passenger
VALUES('George');

INSERT INTO Passenger
VALUES('Maria');

INSERT INTO Passenger
VALUES('Florin');

INSERT INTO Passenger
VALUES('Alina');

INSERT INTO Passenger
VALUES('Sara');

INSERT INTO Passenger
VALUES('Tania');

INSERT INTO Passenger
VALUES('Diana');

INSERT INTO Passenger
VALUES('Denisa');

INSERT INTO Passenger
VALUES('Georgiana');

INSERT INTO Passenger
VALUES('Iulia');

INSERT INTO Passenger
VALUES('Daria');

INSERT INTO Passenger
VALUES('Sabina');

INSERT INTO Passenger
VALUES('Anca');

INSERT INTO Passenger
VALUES('Dragos');

INSERT INTO Passenger
VALUES('Ioan');

INSERT INTO Passenger
VALUES('Vlad');


INSERT INTO Controller(name, rating)
VALUES('Ioan',3);

INSERT INTO Controller(name, rating)
VALUES('Matei',7);

INSERT INTO Controller(name, rating)
VALUES('Georgiana',10);

INSERT INTO Controller(name, rating)
VALUES('Marius',1);

INSERT INTO Controller(name, rating)
VALUES('Ionel',5);

INSERT INTO Controller(name, rating)
VALUES('Andreea',9);

INSERT INTO Controller(name, rating)
VALUES('George',10);


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


CREATE OR ALTER FUNCTION validatePassengerName(@name VARCHAR(200)) RETURNS INT AS
BEGIN 
	DECLARE @return INT = 0
	IF (len(@name)>=5)
		SET @return=1
	RETURN @return
END;


CREATE OR ALTER FUNCTION validateControllerName(@name VARCHAR(200)) RETURNS INT AS 
BEGIN 
	DECLARE @return INT = 0
	IF (len(@name)>=5)
		SET @return=1
	RETURN @return
END;


CREATE OR ALTER FUNCTION validateControllerRating(@rating INT) RETURNS INT AS 
BEGIN 
	DECLARE @return INT = 0
	IF (@rating>0)
		SET @return=1
	RETURN @return
END;


CREATE OR ALTER PROCEDURE AddPassengerController @passengerName VARCHAR(200), @controllerName VARCHAR(200), @rating INT AS 
BEGIN 
	BEGIN TRAN 
		BEGIN try
			IF(dbo.validatePassengerName(@passengerName)<>1)
			BEGIN 
				RAISERROR('Passenger name must have more than 5 characters',14,1)
			END
			IF(dbo.validateControllerName(@controllerName)<>1)
			BEGIN 
				RAISERROR('Controller name must have more than 5 characters',14,1)
			END
			IF(dbo.validateControllerRating(@rating)<>1)
			BEGIN 
				RAISERROR('Controller rating must be greater than 0',14,1)
			END
			
			INSERT INTO Passenger VALUES(@passengerName)
			DECLARE @pid INT = scope_identity()
			INSERT INTO Controller(name, rating) VALUES (@controllerName, @rating)
			DECLARE @cid INT = scope_identity()
			INSERT INTO ControllerPassengerRelation(passenger_id, controller_id) VALUES (@pid, @cid)
			COMMIT TRAN
			SELECT 'Transaction committed'
		END try
		BEGIN catch
			DECLARE @ErrorMessage NVARCHAR(4000);
    		DECLARE @ErrorSeverity INT;
    		DECLARE @ErrorState INT;

    		SELECT
        		@ErrorMessage = ERROR_MESSAGE(),
        		@ErrorSeverity = ERROR_SEVERITY(),
        		@ErrorState = ERROR_STATE();

   			ROLLBACK TRAN;

   			SELECT 'Transaction rollbacked' AS Result, @ErrorMessage AS ErrorMessage, @ErrorSeverity AS ErrorSeverity, @ErrorState AS ErrorState;
		END catch
END;


---------------------------------------- let's call the procedure --------------------------

SELECT * FROM Passenger;
SELECT * FROM Controller;
SELECT * FROM ControllerPassengerRelation;

EXEC AddPassengerController @passengerName='Georgian', @controllerName='Georgiana', @rating=5;

SELECT * FROM Passenger;
SELECT * FROM Controller;
SELECT * FROM ControllerPassengerRelation;

 --------------------------------------- 2nd procedure ------------------------------------------




CREATE OR ALTER PROCEDURE AddPassengerControllerSecondProcedure
    @passengerName VARCHAR(200),
    @controllerName VARCHAR(200),
    @rating INT
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @ErrorOccurred BIT = 0;
    DECLARE @PassengerId INT = NULL;
    DECLARE @ControllerId INT = NULL;
    
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Validate passenger name
		IF(dbo.validatePassengerName(@passengerName)<>1)
        BEGIN
            RAISERROR('Passenger name must have more than 5 characters', 16, 1);
        END
        ELSE
        BEGIN
            -- Insert passenger
            INSERT INTO Passenger (name)
            VALUES (@passengerName);
            
            SET @PassengerId = SCOPE_IDENTITY();
        END
        
        
        -- Validate controller rating
		IF(dbo.validateControllerRating(@rating)<>1)
        BEGIN
            RAISERROR('Controller rating must be greater than 0', 16, 1);
        END
        
        -- Validate controller name
		IF(dbo.validateControllerName(@controllerName)<>1)
        BEGIN
            RAISERROR('Controller name must have more than 5 characters', 16, 1);
        END
        ELSE
        BEGIN
            -- Insert controller
            INSERT INTO Controller (name, rating)
            VALUES (@controllerName, @rating);
            
            SET @ControllerId = SCOPE_IDENTITY();
        END
        
        IF @PassengerId IS NOT NULL AND @ControllerId IS NOT NULL
        BEGIN
            -- Insert relation
            INSERT INTO ControllerPassengerRelation (passenger_id, controller_id)
            VALUES (@PassengerId, @ControllerId);
        END
        
        COMMIT TRANSACTION;
        
        SELECT 'Data inserted successfully' AS Result;
    END TRY
    BEGIN CATCH
        SET @ErrorOccurred = 1;
        
        IF @@TRANCOUNT > 0
        BEGIN
            COMMIT TRANSACTION;
        END
        
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        
        
        IF @ControllerId IS NOT NULL
        BEGIN
            DELETE FROM Controller WHERE controller_id = @ControllerId;
        END
        
        SELECT 'Data insertion failed' AS Result, @ErrorMessage AS ErrorMessage, @ErrorOccurred AS ErrorOccurred;
    END CATCH
END;



SELECT * FROM Passenger;
SELECT * FROM Controller;
SELECT * FROM ControllerPassengerRelation;

EXEC AddPassengerControllerSecondProcedure @passengerName='Daniellll', @controllerName='Georgianaaaa', @rating=0;

SELECT * FROM Passenger;
SELECT * FROM Controller;
SELECT * FROM ControllerPassengerRelation;



---------------------------------------------------------------- DIRTY READS, PHANTOM READS, DEADLOCKS ----------------------

--Dirty Reeds
BEGIN TRANSACTION
UPDATE Controller SET rating=8
WHERE controller_id = 1
WAITFOR DELAY '00:00:10'
ROLLBACK TRANSACTION;

--NON-REPEATABLE READS
INSERT INTO Controller(name, rating) VALUES ('Florinels',5)
BEGIN TRAN
WAITFOR DELAY '00:00:05'
UPDATE Controller SET name='Florinels' where rating = 5
COMMIT TRAN;


--PHANTOM READS
BEGIN TRAN
WAITFOR DELAY '00:00:04'
INSERT INTO Controller(name,rating) VALUES
('Alinut',7)
COMMIT TRAN


--DEADLOCK
BEGIN TRAN
UPDATE Controller SET name='Flo' WHERE controller_id=14;
WAITFOR DELAY '00:00:10'
UPDATE Passenger SET name='Georgelut' WHERE passenger_id=18
COMMIT TRAN;



--Dirty Reeds
SET TRANSACTION ISOLATION LEVEL READ
UNCOMMITTED
BEGIN TRAN
SELECT * FROM Controller
WAITFOR DELAY '00:00:15'
SELECT * FROM Controller
COMMIT TRAN;


--Dirty Reeds Solution
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
SELECT * FROM Controller
WAITFOR DELAY '00:00:15'
SELECT * FROM Controller;
COMMIT TRAN;



--NON-REPEATABLE READS
SET TRANSACTION ISOLATION LEVEL READ
COMMITTED
BEGIN TRAN
SELECT * FROM Controller
WAITFOR DELAY '00:00:05'
SELECT * FROM Controller
COMMIT TRAN;


--NON-REPEATABLE READS Solution
SET TRANSACTION ISOLATION LEVEL REPEATABLE
READ
BEGIN TRAN
SELECT * FROM Controller
WAITFOR DELAY '00:00:05'
SELECT * FROM Controller
COMMIT TRAN;


--PHANTOM READS
SET TRANSACTION ISOLATION LEVEL REPEATABLE
READ
BEGIN TRAN
SELECT * FROM Controller
WAITFOR DELAY '00:00:05'
SELECT * FROM Controller;
COMMIT TRAN;


--PHANTOM READS Solution
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
BEGIN TRAN
SELECT * FROM Controller
WAITFOR DELAY '00:00:05'
SELECT * FROM Controller
COMMIT TRAN;


--DEADLOCK
BEGIN TRAN
UPDATE Controller SET name='Flo' WHERE controller_id=14;
WAITFOR DELAY '00:00:10'
UPDATE Passenger SET name='Georgelut' WHERE passenger_id=18
COMMIT TRAN;



--DEADLOCK Solution
SET DEADLOCK_PRIORITY HIGH
BEGIN TRAN
UPDATE Controller SET name='Flo' WHERE controller_id=14;
-- this transaction has exclusively lock on table Controller
WAITFOR DELAY '00:00:10'
UPDATE Passenger SET name='Georgelut' WHERE passenger_id=18
COMMIT TRAN;


--------------------------------------------------- UPDATE CONFLICT UNDER OPTIMISTIC ISOLATION LEVEL --------------------------------


ALTER DATABASE PublicTransportTransact SET ALLOW_SNAPSHOT_ISOLATION ON

WAITFOR DELAY '00:00:10'
BEGIN TRAN
UPDATE Controller SET name ='Florinelut' WHERE controller_id=14;
-- name is now Florinelut
WAITFOR DELAY '00:00:10'
COMMIT TRAN;

SELECT * FROM Controller;

--ALTER DATABASE PublicTransportTransact SET ALLOW_SNAPSHOT_ISOLATION OFF


SET TRANSACTION ISOLATION LEVEL SNAPSHOT
BEGIN TRAN
SELECT * FROM Passenger WHERE passenger_id=17
WAITFOR DELAY '00:00:10'
SELECT * FROM Passenger WHERE passenger_id=18
UPDATE Passenger SET name='Ionelut' WHERE passenger_id=17
-- process will block
-- Process will receive Error 3960.
COMMIT TRAN

SELECT * FROM Passenger p ;



