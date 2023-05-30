<!----DELETING DATA FROM THE STUDENT TABLE-------->
<link rel="stylesheet" href="phpstyle.css">
<?php
#DELETE STUFF FROM THE TABLE OR FROM THE DATA
$host= "localhost";
$user = "root";
$passwd = "";
$database = "php_practice";
$tbl_name = "Student";

$SID = $_POST["STUDENT_NO"];

// Create connection
$conn = new mysqli($host, $user, $passwd, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connection to Delete Sucsessful";
echo "<br>";


//Create SQL statement and run

$sql = "delete from $tbl_name where STUDENT_NO = '$SID' ";
$resultdelete = $conn->query($sql);

//Select all data to print to screen
$result = $conn->query("SELECT * FROM $tbl_name");

//check to see if any data has been selected

if ($result->num_rows > 0) {

    // output data of each row

    while($row = $result->fetch_assoc()) {
        echo "Student Number: " . $row["STUDENT_NO"] . "<br>";
        echo "Student ID: " . $row["STUDENT_ID"] . "<br>";
        echo "University ID: " . $row["UNI_ID"] . "<br>";
        echo "Faculty ID: " . $row["FACULTY_ID"] . "<br>";
        echo "Faculty Name: " . $row["FCLT_NAME"] . "<br>";
        echo "Student Name: " . $row["FULL_NAME"] . "<br>";
        echo "Date of Birth: " . $row["DATE_OF_BIRTH"] . "<br>";
        echo "Student Email: " . $row["STUDENT_EMAIL"] . "<br>";
        echo "Phone Number: " . $row["PHONE_NO"] . "<br>";
        echo "Address: " . $row["ADDRESS"] . "<br>";
        echo "<br>";
 }
} else {
    echo "0 results";
}
$conn->close();
?> 