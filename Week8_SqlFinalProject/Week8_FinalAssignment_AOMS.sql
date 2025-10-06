-- =====================================================================
-- AIRLINE OPERATIONS MANAGEMENT SYSTEM (AOMS)
-- Relational database for airline operations
-- Application part in Python
-- Author: Yawo T. A. NYONATO
-- Date: 2025-10-06
-- Description:
--   Database for managing flight operations, crew, cargo, revenue,
--   fuel, and allowances — with normalized lookup tables.
-- =====================================================================

-- -----------------------------------------------------
-- 1. CREATE DATABASE
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS airline_management;
USE airline_management;

-- -----------------------------------------------------
-- 2. LOOKUP TABLES
-- -----------------------------------------------------

-- 2.1 Aircraft Status Types
CREATE TABLE aircraft_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE COMMENT 'Aircraft operational state (ACTIVE, IN_MAINTENANCE, RETIRED)'
) ENGINE=InnoDB COMMENT='Lookup table for aircraft status types';

-- 2.2 Crew Role Types
CREATE TABLE crew_role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE COMMENT 'Crew role (PILOT, CO-PILOT, CABIN_CREW, etc.)'
) ENGINE=InnoDB COMMENT='Lookup table for crew professional roles';

-- 2.3 Duty Role Types for Flight Assignments
CREATE TABLE duty_role (
    duty_role_id INT AUTO_INCREMENT PRIMARY KEY,
    duty_role_name VARCHAR(50) NOT NULL UNIQUE COMMENT 'Flight duty role (CAPTAIN, FIRST_OFFICER, etc.)'
) ENGINE=InnoDB COMMENT='Lookup table for flight duty roles assigned to crew';

-- 2.4 Flight Status Types
CREATE TABLE flight_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE COMMENT 'Flight status (ON_TIME, DELAYED, CANCELLED)'
) ENGINE=InnoDB COMMENT='Lookup table for flight operational statuses';

-- 2.5 User Roles
CREATE TABLE user_role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE COMMENT 'User role (ADMIN, OPERATIONS, FINANCE, HR, etc.)'
) ENGINE=InnoDB COMMENT='Lookup table for system user roles';

-- -----------------------------------------------------
-- 3. CORE ENTITIES
-- -----------------------------------------------------

-- 3.1 Airport
CREATE TABLE airport (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(5) NOT NULL UNIQUE COMMENT 'IATA/ICAO airport code (e.g., LFW, CDG)',
    name VARCHAR(100) NOT NULL COMMENT 'Airport full name',
    city VARCHAR(100) COMMENT 'City location',
    country VARCHAR(100) COMMENT 'Country name'
) ENGINE=InnoDB COMMENT='List of all airports used in flight operations';

-- 3.2 Aircraft
CREATE TABLE aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_no VARCHAR(20) NOT NULL UNIQUE COMMENT 'Aircraft tail number (e.g., 5V-TAA)',
    model VARCHAR(50) COMMENT 'Aircraft model (e.g., Boeing 737-700)',
    manufacturer VARCHAR(50) COMMENT 'Aircraft manufacturer',
    capacity INT COMMENT 'Passenger capacity',
    status_id INT NOT NULL COMMENT 'Operational status (FK to aircraft_status)',
    FOREIGN KEY (status_id) REFERENCES aircraft_status(status_id)
) ENGINE=InnoDB COMMENT='List of aircraft and their operational status';

-- 3.3 Flight Schedule
CREATE TABLE flight_schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_no VARCHAR(10) NOT NULL COMMENT 'Flight number (e.g., KP202)',
    origin_id INT NOT NULL COMMENT 'Departure airport (FK)',
    destination_id INT NOT NULL COMMENT 'Arrival airport (FK)',
    departure_time TIME NOT NULL COMMENT 'Scheduled departure time',
    arrival_time TIME NOT NULL COMMENT 'Scheduled arrival time',
    frequency VARCHAR(20) COMMENT 'Operating days (e.g., MON-WED-FRI)',
    aircraft_id INT COMMENT 'Assigned aircraft (FK)',
    FOREIGN KEY (origin_id) REFERENCES airport(airport_id),
    FOREIGN KEY (destination_id) REFERENCES airport(airport_id),
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id)
) ENGINE=InnoDB COMMENT='Planned flight schedules with assigned aircraft and routes';

-- 3.4 Flight Movement
CREATE TABLE flight_movement (
    movement_id INT AUTO_INCREMENT PRIMARY KEY,
    schedule_id INT NOT NULL COMMENT 'Linked scheduled flight (FK)',
    flight_date DATE NOT NULL COMMENT 'Actual flight date',
    actual_departure DATETIME COMMENT 'Actual departure timestamp',
    actual_arrival DATETIME COMMENT 'Actual arrival timestamp',
    status_id INT NOT NULL COMMENT 'Operational status (FK to flight_status)',
    remarks VARCHAR(255) COMMENT 'Additional notes',
    FOREIGN KEY (schedule_id) REFERENCES flight_schedule(schedule_id),
    FOREIGN KEY (status_id) REFERENCES flight_status(status_id)
) ENGINE=InnoDB COMMENT='Daily movement tracking for flights (actuals vs schedule)';

-- -----------------------------------------------------
-- 4. CREW MANAGEMENT
-- -----------------------------------------------------

-- 4.1 Crew
CREATE TABLE crew (
    crew_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_no VARCHAR(20) NOT NULL UNIQUE COMMENT 'Unique staff identifier',
    first_name VARCHAR(50) NOT NULL COMMENT 'Crew first name',
    last_name VARCHAR(50) NOT NULL COMMENT 'Crew last name',
    role_id INT NOT NULL COMMENT 'Crew role (FK to crew_role)',
    base_airport_id INT COMMENT 'Crew home/base airport (FK)',
    FOREIGN KEY (role_id) REFERENCES crew_role(role_id),
    FOREIGN KEY (base_airport_id) REFERENCES airport(airport_id)
) ENGINE=InnoDB COMMENT='List of flight crew and technical personnel';

-- 4.2 Crew Qualification
CREATE TABLE crew_qualification (
    qualification_id INT AUTO_INCREMENT PRIMARY KEY,
    crew_id INT NOT NULL COMMENT 'Linked crew member (FK)',
    aircraft_type VARCHAR(50) NOT NULL COMMENT 'Qualified aircraft model (e.g., B737)',
    issue_date DATE NOT NULL COMMENT 'Qualification issue date',
    expiry_date DATE COMMENT 'Qualification expiry date',
    remarks VARCHAR(255) COMMENT 'Notes on qualification',
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id)
) ENGINE=InnoDB COMMENT='Crew qualifications and license validity for aircraft types';

-- 4.3 Flight Crew Assignment
CREATE TABLE flight_crew_assignment (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    movement_id INT NOT NULL COMMENT 'Linked flight movement (FK)',
    crew_id INT NOT NULL COMMENT 'Assigned crew member (FK)',
    duty_role_id INT NOT NULL COMMENT 'Assigned duty role (FK)',
    FOREIGN KEY (movement_id) REFERENCES flight_movement(movement_id),
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id),
    FOREIGN KEY (duty_role_id) REFERENCES duty_role(duty_role_id)
) ENGINE=InnoDB COMMENT='Crew assignments per actual flight movement';

-- -----------------------------------------------------
-- 5. REVENUE & EXPENSE MODULES
-- -----------------------------------------------------

-- 5.1 Cargo Revenue
CREATE TABLE cargo_revenue (
    cargo_id INT AUTO_INCREMENT PRIMARY KEY,
    movement_id INT NOT NULL COMMENT 'Linked flight movement (FK)',
    weight_kg DECIMAL(10,2) NOT NULL COMMENT 'Cargo weight (kg)',
    revenue_amount DECIMAL(10,2) NOT NULL COMMENT 'Revenue earned from cargo',
    currency CHAR(3) DEFAULT 'USD' COMMENT 'Currency code (ISO 4217)',
    FOREIGN KEY (movement_id) REFERENCES flight_movement(movement_id)
) ENGINE=InnoDB COMMENT='Cargo revenue recorded per flight movement';

-- 5.2 Excess Baggage
CREATE TABLE excess_baggage (
    baggage_id INT AUTO_INCREMENT PRIMARY KEY,
    movement_id INT NOT NULL COMMENT 'Linked flight movement (FK)',
    passenger_name VARCHAR(100) COMMENT 'Passenger paying for excess baggage',
    weight_excess DECIMAL(8,2) NOT NULL COMMENT 'Excess baggage weight (kg)',
    amount_charged DECIMAL(8,2) NOT NULL COMMENT 'Amount charged for excess baggage',
    currency CHAR(3) DEFAULT 'USD' COMMENT 'Currency code',
    FOREIGN KEY (movement_id) REFERENCES flight_movement(movement_id)
) ENGINE=InnoDB COMMENT='Excess baggage transactions recorded per flight';

-- 5.3 Fuel Bill
CREATE TABLE fuel_bill (
    fuel_id INT AUTO_INCREMENT PRIMARY KEY,
    movement_id INT NOT NULL COMMENT 'Linked flight movement (FK)',
    supplier_name VARCHAR(100) NOT NULL COMMENT 'Fuel supplier name',
    quantity_litres DECIMAL(10,2) NOT NULL COMMENT 'Quantity supplied (litres)',
    price_per_litre DECIMAL(10,2) NOT NULL COMMENT 'Unit price per litre',
    total_cost DECIMAL(12,2)
        GENERATED ALWAYS AS (quantity_litres * price_per_litre) STORED COMMENT 'Total fuel cost (calculated)',
    currency CHAR(3) DEFAULT 'USD' COMMENT 'Currency code',
    FOREIGN KEY (movement_id) REFERENCES flight_movement(movement_id)
) ENGINE=InnoDB COMMENT='Fuel purchase and consumption cost per flight movement';

-- 5.4 LTA (Leave Travel Allowance)
CREATE TABLE lta_allowance (
    lta_id INT AUTO_INCREMENT PRIMARY KEY,
    crew_id INT NOT NULL COMMENT 'Crew receiving LTA (FK)',
    allowance_date DATE NOT NULL COMMENT 'Allowance date',
    route_description VARCHAR(255) COMMENT 'Route or destination description',
    amount DECIMAL(10,2) NOT NULL COMMENT 'Allowance amount',
    currency CHAR(3) DEFAULT 'USD' COMMENT 'Currency code',
    approved_by VARCHAR(100) COMMENT 'Approver name',
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id)
) ENGINE=InnoDB COMMENT='Leave Travel Allowance records per crew member';

-- -----------------------------------------------------
-- 6. SYSTEM USERS
-- -----------------------------------------------------

CREATE TABLE user_account (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE COMMENT 'System username',
    password_hash VARCHAR(255) NOT NULL COMMENT 'Hashed password for authentication',
    role_id INT NOT NULL COMMENT 'Linked role (FK to user_role)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Account creation timestamp',
    FOREIGN KEY (role_id) REFERENCES user_role(role_id)
) ENGINE=InnoDB COMMENT='System user accounts for access control and permissions';

-- =====================================================================
-- END OF DATABASE STRUCTURE
-- =====================================================================
