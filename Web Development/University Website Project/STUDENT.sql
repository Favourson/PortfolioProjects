CREATE TABLE UNIVERSITY(
	UNI_ID INT(4) NOT NULL,
    UNI_NAME CHAR(52) NOT NULL,
    UNI_DESCR CHAR(90) DEFAULT NULL,
    UNI_LOCATION VARCHAR(32),
    UNI_ADDRESS VARCHAR(40),
    CONSTRAINT PK_UNI_ID PRIMARY KEY (UNI_ID)
);


INSERT INTO UNIVERSITY VALUES
(101,'Covenants University Lagos','Largest University in Africa', 'Lagos, Nigeria','10 osun, Lagos, Nigeria'),
(102,'Covenants University London','Highest Rated African University Branch in London', 'London, United Kingdom', '13 Camden Road, London');




CREATE TABLE FACULTY(
	FCLT_ID INT(4) NOT NULL,
    FCLT_NAME CHAR(32) DEFAULT NULL,
    FCLT_DESCR CHAR(32) DEFAULT NULL,
    UNI_ID INT(4),
    CONSTRAINT PK_FCLT_ID PRIMARY KEY (FCLT_ID),
    FOREIGN KEY (UNI_ID) REFERENCES UNIVERSITY(UNI_ID)
);

INSERT INTO FACULTY VALUES
(001, 'Faculty of History', 'All aspects of History', 102),
(002, 'Faculty of Arts', 'All types and forms of arts', 102),
(003, 'Faculty of Engineering', 'All branches of Engineering', 101),
(004, 'Faculty of Economics', 'All branches of Economics', 101),
(005, 'Faculty of Education', 'All forms of Education', 102);


CREATE TABLE ACADEMIC_CLDR(
	ACADEMIC_CLDR_ID INT(7) NOT NULL,
    ACADEMIC_CLDR_NAME CHAR(20) DEFAULT NULL,
    ACADEMIC_WEEKS VARCHAR(9) DEFAULT NULL,
    CONSTRAINT PK_ACADEMIC_CLDR_ID PRIMARY KEY (ACADEMIC_CLDR_ID)
);

INSERT INTO ACADEMIC_CLDR VALUES
(202201, 'Fall Semester', '18 Weeks'),
(202202, 'Spring Semester', '16 Weeks'),
(202203, 'Summer Semester', '8 Weeks'),
(202301, 'Fall Semester', '18 Weeks'),
(202302, 'Spring Semester', '16 Weeks');



CREATE TABLE STUDENT(
	STUDENT_NO INT(12) NOT NULL,
	STUDENT_ID VARCHAR(7),
    UNI_ID INT(4),
    FACULTY_ID INT(4),
    FCLT_NAME CHAR(32),
    FULL_NAME CHAR(32) DEFAULT NULL,
    DATE_OF_BIRTH DATE DEFAULT NULL,
    STUDENT_EMAIL VARCHAR(32),
    PHONE_NO VARCHAR(20),
    ADDRESS VARCHAR(32),
    CONSTRAINT PK_STUDENT_NO PRIMARY KEY (STUDENT_NO),
    FOREIGN KEY (FACULTY_ID) REFERENCES FACULTY(FCLT_ID),
    FOREIGN KEY (UNI_ID) REFERENCES UNIVERSITY(UNI_ID)
);


INSERT INTO STUDENT VALUES
(100801091, 'FO191', 101, 001, 'Faculty of History', 'Favoursen Osborna', '2003-06-11', 'FO151@STDNTEML.AC.NG', '+2348043731978', '12 Lagos, Nigeria'),
(100802092, 'ABA192', 102, 002, 'Faculty of Arts', 'Abodurin Agbenarobi', '2002-02-12', 'ABA192@STDNTEML.AC.UK', '+447772897898', '27 Wembley, London'),
(100803093, 'MK193', 102, 004, 'Faculty of Economics', 'Millie Kevsha', '2001-10-19', 'MK193@STDNTEML.AC.UK', '+44899873454387', '08 colindale, London'),
(100804094, 'OM194', 102, 005, 'Faculty of Education', 'Otuto Mamona', '2002-02-14', 'OM194@STDNTEML.AC.UK', '+97189899431979', '04 Academic City, Dubai'),
(100805095, 'AK195', 101, 003, 'Faculty of Engineering', 'Atreus Kratoson', '2003-09-21', 'AK195@STDNTEML.AC.NG', '+23490481231978', '1 Abuja, Nigeria'),
(100806096, 'JO101', 102, 001, 'Faculty of History', 'Jason Obome', '2001-01-19', 'JO101@STDNTEML.AC.UK', '+4482342654387', '02 colindale, London'),
(100807097, 'LF104', 102, 002, 'Faculty of Arts', 'Layefa Farson', '2002-07-14', 'LF104@STDNTEML.AC.UK', '+9711292343979', '06 Academic City, Dubai'),
(100808098, 'SHR205', 101, 004, 'Faculty of Economics', 'Shane Rayor', '2000-09-11', 'SHR205@STDNTEML.AC.NG', '+23485765231978', '10 Abuja, Nigeria'),
(100809099, 'OG214', 102, 005, 'Faculty of Education', 'Omar Gunawardena Farson', '2000-07-10', 'OG214@STDNTEML.AC.UK', '+97188231894887', '06 Golf, Dubai'),
(100810100, 'YL345', 102, 003, 'Faculty of Engineering', 'Yabo Lateef', '2000-01-11', 'YL345@STDNTEML.AC.UK', '+449928398472', '10 Mead street, London');



CREATE TABLE MODULE(
	MDL_CODE INT(7) NOT NULL,
    MDL_NAME VARCHAR(64) DEFAULT NULL,
    FACULTY_NAME CHAR(32) DEFAULT NULL,
    FACULTY_ID INT(4),
    MDL_LEADER CHAR(32) DEFAULT NULL,
    ACADEMIC_CLDR_ID INT(7),
    CONSTRAINT PK_MDL_CODE PRIMARY KEY (MDL_CODE),
    FOREIGN KEY (ACADEMIC_CLDR_ID) REFERENCES ACADEMIC_CLDR(ACADEMIC_CLDR_ID),
    FOREIGN KEY (FACULTY_ID) REFERENCES FACULTY(FCLT_ID)
);

INSERT INTO MODULE VALUES
(11101, 'Discovering the arts and humanities', 'Faculty of History', 001, 'Kevin Bayer', 202201),
(11102, 'Early modern Europe: society and culture c.1500-1780', 'Faculty of History', 001, 'Kevin Bayer', 202202),
(11103, 'Art and visual cultures in the modern world', 'Faculty of Arts', 002, 'Mehak Maleeka', 202201),
(11104, 'Exploring art and visual culture', 'Faculty of Arts', 002, 'Mehak Malaika', 202202),
(11105, 'Engineering: mathematics, modelling, applications', 'Faculty of Engineering', 003, 'Cory Goodman', 202201),
(11106, 'Mechanical engineering: heat and flow', 'Faculty of Engineering', 003, 'Cory Goodman', 202301),
(11107, 'Essential economics: macro and micro perspectives', 'Faculty of Economics', 004, 'Valerie Desplat', 202202),
(11108, 'Doing economics: people, markets and policy', 'Faculty of Economics', 004, 'Valerie Desplat', 202302),
(11109, 'English for academic purposes online', 'Faculty of Education', 005, 'Banuje Ginika', 202201),
(11110, 'Developing subject knowledge for the primary years', 'Faculty of Education', 005, 'Banuje Ginika', 202203);



CREATE TABLE ENROLMENT(
	STUDENT_NO INT(12),
    MDL_CODE INT(7),
    ACADEMIC_CLDR_ID INT(7),
    CONSTRAINT PK_STUDENT_MDL PRIMARY KEY (STUDENT_NO, MDL_CODE),
    FOREIGN KEY (STUDENT_NO) REFERENCES STUDENT(STUDENT_NO),
    FOREIGN KEY (MDL_CODE) REFERENCES MODULE(MDL_CODE),
    FOREIGN KEY (ACADEMIC_CLDR_ID) REFERENCES ACADEMIC_CLDR(ACADEMIC_CLDR_ID)
);

INSERT INTO ENROLMENT VALUES
(100801091, 11101, 202201),
(100802092, 11102, 202201),
(100803093, 11103, 202202),
(100804094, 11104, 202202),
(100805095, 11105, 202203),
(100806096, 11106, 202203),
(100807097, 11107, 202301),
(100808098, 11108, 202301),
(100809099, 11109, 202302),
(100810100, 11110, 202302);


CREATE TABLE STAFF_ROLE(
	STAFF_ROLE_ID INT(5) NOT NULL,
    STAFF_ROLE_NAME CHAR(32) DEFAULT NULL,
    STAFF_ROLE_DESCR VARCHAR(120) DEFAULT NULL,
    CONSTRAINT PK_STAFF_ROLE_ID PRIMARY KEY (STAFF_ROLE_ID)
);

INSERT INTO STAFF_ROLE VALUES
(1011, 'Professor', 'teaches classes to graduate and undergraduate students'),
(1012, 'Ass. Professor', 'assists with teaching classes to undergraduate and graduate students'),
(1013, 'Senior Lecturer', 'teaching classes to students and reviewing lecture materials'),
(1014, 'Lecturer', 'research and teach subjects to students'),
(1015, 'University Cleaner', 'responsible for maintaining high standards of cleanliness throughout the school'),
(1016, 'Secretary', 'supports in ensuring the smooth functioning of the Management Committee'),
(1017, 'Security Officer', 'Provides security for all within areas of the University campus'),
(1018, 'Librarian', 'Provides students and staff with information, and skills needed for effective research'),
(1019, 'Research Manager', 'provide high level professional support to research strategies and innovation activities'),
(1020, 'IT support', 'Assists all with software downloads and updates, and technical student portal issues');



CREATE TABLE TEACHING_STAFF(
	TEACHING_STAFF_ID INT(7) NOT NULL,
    TEACHING_FULL_NAME VARCHAR(32) DEFAULT NULL,
    STAFF_ROLE_ID INT(5) DEFAULT NULL,
    STAFF_ROLE_NAME CHAR(32) DEFAULT NULL,
    TEACHING_STAFF_EMAIL VARCHAR(32),
    TEACHING_STAFF_TELEPHONE VARCHAR(32),
    OFFICE_DAYS VARCHAR (32),
    TEACHING_STAFF_OFFICE_NO VARCHAR(18),
    CONSTRAINT PK_TEACHING_STAFF_ID PRIMARY KEY (TEACHING_STAFF_ID),
    FOREIGN KEY (STAFF_ROLE_ID) REFERENCES STAFF_ROLE(STAFF_ROLE_ID)
);

INSERT INTO TEACHING_STAFF VALUES
(1001, 'Kevin Bayer', 1013, 'Senior Lecturer', 'kevinbayer46@gmail.com', '+448998734111223', 'Mon to Wed', 'Room 105'),
(1002, 'Bolu Adebisi', 1011, 'Professor', 'boluadebisi@gmail.com', '+448998789234535', 'Wed to Fri', 'Room 106'),
(1003, 'Delvin Gamman', 1012, 'Assistant Professor', 'delvingamman200@gmail.com', '+448996675536445', 'Mon to Fri', 'Room 108'),
(1004, 'Cory Goodman', 1014, 'Lecturer', 'corygoodman@gmail.com', '+448998737777787', 'Mon to Fri', 'Room 104'),
(1005, 'Mehak Maleeka', 1012, 'Assistant Professor', 'mehakmaleeka@gmail.com', '+44899873454387', 'Mon to Wed', 'Room 102'),
(1006, 'Afreen Hussain', 1011, 'Professor', 'afreenhussain@gmail.com', '+44899845324548', 'Tue to Fri', 'Room 101'),
(1007, 'Valerie Desplat', 1014, 'Lecturer', 'valeriedesplat@gmail.com', '+44765584854747', 'Tue to Thur', 'Room 103'),
(1008, 'Banuje Ginika', 1013, 'Senior Lecturer', 'banujeginika@gmail.com', '+4489987348853', 'Mon to Fri', 'Room 107'),
(1009, 'Oluwa Lekan', 1012, 'Assistant Professor', 'oluwalekan@gmail.com', '+4423237348880', 'Mon to Fri', 'Room 108'),
(1010, 'Happy Galviana', 1013, 'Senior Lecturer', 'happygalviana@gmail.com', '+4478987873487898', 'Mon to Wed', 'Room 105');



CREATE TABLE OPERATIONAL_STAFF(
	OPERATIONAL_STAFF_ID INT(7) NOT NULL,
    OPERATIONAL_FULL_NAME VARCHAR(32) DEFAULT NULL,
    STAFF_ROLE_ID INT(5) DEFAULT NULL,
    STAFF_ROLE_NAME CHAR(32) DEFAULT NULL,
    OPERATIONAL_STAFF_EMAIL VARCHAR(32),
    OPERATIONAL_STAFF_TELEPHONE VARCHAR(32),
    OPERATIONAL_STAFF_OFFICE_NO VARCHAR(18),
    CONSTRAINT PK_OPERATIONAL_STAFF_ID PRIMARY KEY (OPERATIONAL_STAFF_ID),
    FOREIGN KEY (STAFF_ROLE_ID) REFERENCES STAFF_ROLE(STAFF_ROLE_ID)
);

INSERT INTO OPERATIONAL_STAFF VALUES
(1010, 'Bay Roqe', 1015, 'University Cleaner', 'bayroqe@gmail.com', '+44098765235890', 'Room 21'),
(1020, 'Otuto Nwoguna', 1016, 'Secretary', 'otutonwoguna@gmail.com', '+44009867413456', 'Room 01'),
(1030, 'Raechel Afolabi', 1017, 'Security Officer', 'raechelafolabi@gmail.com', '+4412343546987', 'Room 07'),
(1040, 'Babunde Alo', 1018, 'Librarian', 'babundealo@gmail.com', '+44807652134356', 'Room 64'),
(1050, 'Akpan Louis', 1015, 'University Cleaner', 'akpanlouis@gmail.com', '+44342543231654', 'Room 21'),
(1060, 'Amaka Nwokedi', 1017, 'Security Officer', 'amakanwokedi@gmail.com', '+44867765533298', 'Room 07'),
(1070, 'Kelvin Mayo', 1016, 'Secretary', 'kelvinmayo@gmail.com', '+4443354768688', 'Room 02'),
(1080, 'Clarissa Contreras', 1018, 'Librarian', 'clarissacontreras@gmail.com', '+4467879800990', 'Room 64'),
(1090, 'Kimena Olivera', 1019, 'Research Manager', 'kimenaolivera@gmail.com', '+4443879801230', 'Room 34'),
(1100, 'Freya Terra', 1020, 'IT support', 'freyaterra@gmail.com', '+44778798768100', 'Room 24');




CREATE TABLE ROOM_TYPE(
	ROOM_TYPE_ID INT(5) NOT NULL,
    ROOM_TYPE_DESCR VARCHAR(16) DEFAULT NULL,
    CONSTRAINT PK_ROOM_TYPE_ID PRIMARY KEY (ROOM_TYPE_ID)
);

INSERT INTO ROOM_TYPE VALUES
(1111, 'Lecture Room'),
(1222, 'Laboratory Room'),
(1333, 'Meeting Room'),
(1444, 'Workshop Room');



CREATE TABLE ROOM(
	ROOM_ID INT(4) NOT NULL,
    ROOM_TYPE_ID INT(5) DEFAULT NULL,
    BUILDING CHAR(40) DEFAULT NULL,
    CAPACITY VARCHAR(12),
    BUILDING_FLOOR VARCHAR(12),
    CONSTRAINT PK_ROOM_ID PRIMARY KEY (ROOM_ID),
    FOREIGN KEY (ROOM_TYPE_ID) REFERENCES ROOM_TYPE(ROOM_TYPE_ID)
);

INSERT INTO ROOM VALUES
(112, 1111, 'Freeman Building', '60 seats', '1st Floor'),
(511, 1222, 'Kuvuki Building', '200 seats', '5th Floor'),
(405, 1333, 'Meta Matters Building', '300 seats', '4th Floor'),
(120, 1444, 'Emmet Justice Building', '150 seats', '1st Floor'),
(240, 1222, 'Campus Central Building', '30 seats', '2nd Floor'),
(160, 1333, 'Kuvuki Building', '250 seats', '1st Floor'),
(370, 1111, 'Meta Matters Building', '500 seats', '3rd Floor'),
(200, 1444, 'Freeman Building', '100 seats', '2nd Floor'),
(306, 1333, 'Emmet Justice Building', '150 seats', '3rd Floor'),
(330, 1111, 'Freeman Building', '200 seats', '2nd Floor');




CREATE TABLE ROOM_BOOKING(
	ROOM_BOOKING_ID INT(7) NOT NULL,
    ROOM_ID INT(4) DEFAULT NULL,
    BOOKING_STAFF_ID INT(7),
    PROCESSING_STAFF_ID INT(7),
    BOOKING_START_DATE DATE,
    BOOKING_END_DATE DATE,
    CONSTRAINT PK_ROOM_BOOKING_ID PRIMARY KEY (ROOM_BOOKING_ID),
    FOREIGN KEY (BOOKING_STAFF_ID) REFERENCES TEACHING_STAFF(TEACHING_STAFF_ID),
    FOREIGN KEY (ROOM_ID) REFERENCES ROOM(ROOM_ID),
    FOREIGN KEY (PROCESSING_STAFF_ID) REFERENCES OPERATIONAL_STAFF(OPERATIONAL_STAFF_ID)
);

INSERT INTO ROOM_BOOKING VALUES
(123401, 112, 1001, 1020, '2021-09-19', '2021-09-25'),
(123402, 511, 1003, 1040, '2021-09-25', '2021-10-30'),
(123403, 405, 1005, 1070, '2022-01-15', '2022-01-30'),
(123404, 120, 1007, 1080, '2022-02-15', '2022-03-30'),
(123405, 240, 1004, 1040, '2022-04-25', '2022-05-30'),
(123406, 160, 1008, 1070, '2022-09-19', '2022-09-30'),
(123407, 370, 1002, 1070, '2023-01-05', '2023-01-19'),
(123408, 200, 1006, 1020, '2023-06-20', '2023-06-22'),
(123409, 306, 1006, 1020, '2023-07-22', '2023-07-25'),
(123410, 330, 1006, 1020, '2023-06-12', '2023-06-15');





CREATE TABLE REGISTRATION(
	REGISTRATION_ID INT(7) NOT NULL,
    STUDENT_NO INT(12),
    MDL_CODE INT(7),
    REG_DATE DATE,
    REG_DESCR VARCHAR(52),
    CONSTRAINT PK_REGISTRATION_ID PRIMARY KEY (REGISTRATION_ID),
    FOREIGN KEY (STUDENT_NO) REFERENCES STUDENT(STUDENT_NO),
    FOREIGN KEY (MDL_CODE) REFERENCES MODULE(MDL_CODE)
);

INSERT INTO REGISTRATION VALUES
(110011, 100801091, 11101, '2020-06-15', 'UG registration for Fall Semester'),
(110012, 100802092, 11103, '2020-07-25', 'UG registration for Fall Semester'),
(110013, 100803093, 11107, '2020-09-28', 'UG registration for Spring Semester'),
(110014, 100804094, 11109, '2021-01-18', 'UG registration for Summer Semester'),
(110015, 100805095, 11105, '2021-03-05', 'UG registration for Summer Semester'),
(110016, 100806096, 11102, '2021-07-20', 'UG registration for Fall Semester'),
(110017, 100807097, 11104, '2022-08-15', 'UG registration for Fall Semester'),
(110018, 100808098, 11108, '2022-08-19', 'UG registration for Fall Semester'),
(110019, 100809099, 11110, '2022-08-19', 'UG registration for Fall Semester'),
(110020, 100810100, 11106, '2022-08-19', 'UG registration for Fall Semester');



select * from student;





drop table registration;
drop table room_booking;
drop table room;
drop table room_type;
drop table operational_staff;
drop table teaching_staff;
drop table staff_role;
drop table enrolment;
drop table module;
drop table student;
drop table academic_cldr;
drop table faculty;
drop table university;

create database practice;

Select * from room_booking;
Select * from room;
Select * from room_type;
Select * from operational_staff;
Select * from teaching_staff;
Select * from staff_role;
Select * from enrolment;
Select * from module;
Select * from student;
Select * from academic_cldr;
Select * from faculty;
Select * from university;
