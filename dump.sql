DROP DATABASE IF EXISTS COMPANY;
CREATE SCHEMA COMPANY;
USE COMPANY;

DROP TABLE IF EXISTS Spares;
CREATE TABLE Spares (
    typeid varchar(20) NOT NULL,
    name varchar(20) NOT NULL,
    cost_per_piece decimal NOT NULL,
    PRIMARY KEY (typeid)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Spares WRITE;
/*!40000 ALTER TABLE Spares DISABLE KEYS */;
INSERT INTO Spares VALUES ('AEP1', 'Field Coils', '250.50'), ('AEP2', 'Rotors', '150.50'), ('AEP3', 'Stators', '250.50'), ('AEP4', 'Housings', '500.50'), ('AEP5', 'Carbon Brushes', '200.50'), ('NB1', 'Hub Bolts', '14.5'), ('NB2', 'T Bolts', '14.5'), ('NB3', 'U Bolts', '14.5');
/*!40000 ALTER TABLE Spares ENABLE KEYS */;
UNLOCK TABLES;



DROP TABLE IF EXISTS Task;
CREATE TABLE Task (
    cost decimal NOT NULL,
    typeid varchar(20) NOT NULL,
    PRIMARY KEY (typeid)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Task WRITE;
/*!40000 ALTER TABLE Task DISABLE KEYS */;
INSERT INTO Task VALUES ('200.00', 'E123'), ('500.00', 'E129'), ('125.00', 'W12'), ('519.12', 'R134'), ('1000.00', 'OW12');
/*!40000 ALTER TABLE Task ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Garage;
CREATE TABLE Garage (
    number int NOT NULL,
    maintainence_cost decimal NOT NULL,
    PRIMARY KEY (number)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Garage WRITE;
/*!40000 ALTER TABLE Garage DISABLE KEYS */;
INSERT INTO Garage VALUES ('1', '1200.05'), ('2', '1230.05'), ('3', '1500.05'), ('4', '1900.05'), ('5', '1000.05');
/*!40000 ALTER TABLE Garage ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Customers;
CREATE TABLE Customers (
    name varchar(20) NOT NULL,
    contact bigint NOT NULL,
    membership_id varchar(20) NOT NULL,
    location varchar(20) NOT NULL,
    PRIMARY KEY (membership_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Customers WRITE;
/*!40000 ALTER TABLE Customers DISABLE KEYS */;
INSERT INTO Customers VALUES ('Jack', '9837124668', 'seo1234', 'London'), ('Dan', '9824592876', 'seo4234', 'Burmingham'), ('Dorry', '9873049765', 'seo1245', 'Beijing'), ('Dora', '9512843690', 'seo1534', 'Delhi'), ('Benny', '9543217688', 'seo1264', 'Delhi'), ('Nell', '9543267801', 'seo12334', 'London');
/*!40000 ALTER TABLE Customers ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Storage_Sections;
CREATE TABLE Storage_Sections (
    location varchar(20) NOT NULL,
    warehouse_no int NOT NULL,
    spare_types varchar(20) NOT NULL,
    number int NOT NULL,
    PRIMARY KEY (warehouse_no, location, number)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Storage_Sections WRITE;
/*!40000 ALTER TABLE Storage_Sections DISABLE KEYS */;
INSERT INTO Storage_Sections VALUES ('London', '1', 'AEP1', '1'), ('London', '1', 'NB2', '2'), ('London', '1', 'AEP3', '3'), ('London', '1', 'AEP4', '4'), ('Burmingham', '2', 'NB2', '1'), ('Burmingham', '2', 'NB1', '2'), ('Burmingham', '2', 'AEB5', '3'), ('Beijing', '3', 'NB3', '1'), ('Beijing', '3', 'AEB2', '2'), ('Beijing', '3', 'AEB3', '3'), ('Delhi', '4', 'NB4', '1'), ('Delhi', '4', 'NB5', '2'), ('Delhi', '4', 'AEB1', '3'), ('Delhi', '4', 'AEB3', '4'), ('Hong Kong', '5', 'AEB3', '1');
/*!40000 ALTER TABLE Storage_Sections ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Warehouse;
CREATE TABLE Warehouse (
    type varchar(20) NOT NULL,
    warehouse_no int NOT NULL,
    no_of_employees int NOT NULL,
    PRIMARY KEY (warehouse_no),
    CONSTRAINT Warehouse_ibfk_1 FOREIGN KEY (type) REFERENCES Task (typeid)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Warehouse WRITE;
/*!40000 ALTER TABLE Warehouse DISABLE KEYS */;
INSERT INTO Warehouse VALUES ('E123', '1', '20'), ('W12', '2', '20'), ('E129', '3', '20'), ('R134', '4', '20'), ('OW12', '5', '20');
/*!40000 ALTER TABLE Warehouse ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Cars;
CREATE TABLE Cars (
    reg_id varchar(20) NOT NULL,
    due_date date NOT NULL,
    g_num int NOT NULL,
    task varchar(20) NOT NULL,
    total_cost decimal NOT NULL,
    customer_id varchar(20) NOT NULL,
    PRIMARY KEY (reg_id),
    CONSTRAINT Cars_ibfk_1 FOREIGN KEY (customer_id) REFERENCES Customers (membership_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Cars WRITE;
/*!40000 ALTER TABLE Cars DISABLE KEYS */;
INSERT INTO Cars VALUES ('AE19OS1234', '2020-09-14', '3', 'E123', '15000.00', 'seo1234');
/*!40000 ALTER TABLE Cars ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Service_History;
CREATE TABLE Service_History (
    registeration_no varchar(20) NOT NULL,
    task_id varchar(20) NOT NULL,
    cost decimal NOT NULL,
    task_status varchar(20) NOT NULL,
    PRIMARY KEY (registeration_no, task_id, cost),
    CONSTRAINT Service_History_ibfk_2 FOREIGN KEY (registeration_no) REFERENCES Cars (reg_id),
    CONSTRAINT Service_History_ibfk_3 FOREIGN KEY (task_id) REFERENCES Task (typeid)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Service_History WRITE;
/*!40000 ALTER TABLE Service_History DISABLE KEYS */;
INSERT INTO Service_History VALUES ('AE19OS1234', 'E123', '15000.00','Completed');
/*!40000 ALTER TABLE Service_History ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
    ssn int NOT NULL,
    full_name varchar(20) NOT NULL,
    contact bigint(10) NOT NULL,
    join_date date NOT NULL,
    birth_date date NOT NULL,
    age int DEFAULT NULL,
    warehouse_no int,
    -- assigned_car varchar(20),
    -- typeid varchar(20) NOT NULL,
    PRIMARY KEY (ssn),
    CONSTRAINT Employee_ibfk_1 FOREIGN KEY (warehouse_no) REFERENCES Warehouse (warehouse_no)
    -- CONSTRAINT Employee_ibfk_2 FOREIGN KEY (assigned_car) REFERENCES Cars (reg_id),
    -- CONSTRAINT Employee_ibfk_3 FOREIGN KEY (typeid) REFERENCES Task (typeid)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES Employee WRITE;
/*!40000 ALTER TABLE Employee DISABLE KEYS */;
INSERT INTO Employee VALUES ('430', 'Jahir Bana', '9823495823', '2020-09-12', '1972-03-14', '48', '5');
/*!40000 ALTER TABLE Employee ENABLE KEYS */;
UNLOCK TABLES;