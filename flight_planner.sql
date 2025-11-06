DROP DATABASE IF EXISTS flight_planner;
CREATE DATABASE flight_planner;
USE flight_planner;

-- Create Airports Table
CREATE TABLE airports (
    airport_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50)
);

-- Create Routes Table
CREATE TABLE routes (
    route_id INT PRIMARY KEY AUTO_INCREMENT,
    source_id INT,
    destination_id INT,
    distance INT,
    fuel_cost INT,
    flight_time INT,
    FOREIGN KEY (source_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_id) REFERENCES airports(airport_id)
);

-- Create Weather Table
CREATE TABLE weather (
    weather_id INT PRIMARY KEY AUTO_INCREMENT,
    airport_id INT,
    weather_condition VARCHAR(30),
    delay_factor INT,
    FOREIGN KEY (airport_id) REFERENCES airports(airport_id)
);

-- Insert Data into Airports
INSERT INTO airports (name, city, country) VALUES
('Indira Gandhi International Airport','Delhi','India'),
('Chhatrapati Shivaji International Airport','Mumbai','India'),
('Kempegowda International Airport','Bangalore','India'),
('Netaji Subhas Chandra Bose International Airport','Kolkata','India'),
('Rajiv Gandhi International Airport','Hyderabad','India'),
('Chennai International Airport','Chennai','India'),
('Cochin International Airport','Kochi','India'),
('Sardar Vallabhbhai Patel International Airport','Ahmedabad','India'),
('Goa International Airport','Goa','India'),
('Pune International Airport','Pune','India'),
('Jaipur International Airport','Jaipur','India'),
('Lucknow Airport','Lucknow','India'),
('Biju Patnaik International Airport','Bhubaneswar','India'),
('Trivandrum International Airport','Thiruvananthapuram','India'),
('Lal Bahadur Shastri Airport','Varanasi','India');

-- Insert Data into Routes
INSERT INTO routes (source_id, destination_id, distance, fuel_cost, flight_time) VALUES
(1,2,1150,45000,130),(1,3,1700,60000,155),(1,4,1300,50000,140),(1,5,1250,47000,135),
(1,6,1750,65000,160),(1,8,950,38000,100),(1,11,270,12000,45),(1,12,480,16000,60),
(2,3,980,40000,110),(2,5,1200,48000,125),(2,9,560,20000,60),(2,10,150,8000,40),
(2,8,520,18000,55),(2,11,1140,45000,130),(3,5,500,20000,75),(3,6,290,12000,45),
(3,7,370,14000,55),(3,9,550,21000,60),(3,14,720,25000,80),(4,5,1500,55000,160),
(4,13,440,18000,55),(4,15,650,22000,70),(4,11,1510,52000,150),(5,6,630,24000,70),
(5,7,760,26000,85),(5,8,980,34000,100),(5,9,670,23000,75),(5,10,550,21000,70),
(6,7,530,20000,65),(6,14,630,23000,75),(6,9,780,26000,85),(7,9,610,22000,70),
(7,14,200,8000,30),(8,9,700,25000,80),(8,11,650,24000,75),(8,10,680,25000,80),
(9,10,450,15000,60),(9,14,740,25000,90),(11,12,470,18000,50),(12,15,520,19000,55),
(13,15,430,16000,45);

-- Insert Data into Weather
INSERT INTO weather (airport_id, weather_condition, delay_factor) VALUES
(1, 'Clear', 0),
(2, 'Rainy', 10),
(3, 'Cloudy', 5),
(4, 'Stormy', 20),
(5, 'Clear', 0),
(6, 'Clear', 0),
(7, 'Rainy', 8),
(8, 'Cloudy', 6),
(9, 'Clear', 0),
(10, 'Rainy', 12),
(11, 'Clear', 0),
(12, 'Foggy', 15),
(13, 'Cloudy', 5),
(14, 'Rainy', 10),
(15, 'Clear', 0);

-- Select Data
SELECT * FROM airports;
SELECT * FROM routes;
SELECT * FROM weather;