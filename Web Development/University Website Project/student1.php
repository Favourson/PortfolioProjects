<!----DISPLAYING ALL FROM THE STUDENT OR STAFF-------->
<link rel="stylesheet" href="phpstyle.css">
<?php
// Set up database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "php_practice";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Get ID search parameter
$id = $_POST['SID'] ?? '';

// Check if the input is 'all'
if ($id == 'all') {
    // Query both tables
    $sql_student = "SELECT * FROM STUDENT";
    $result_student = mysqli_query($conn, $sql_student);

    $sql_teacher = "SELECT * FROM TEACHING_STAFF";
    $result_teacher = mysqli_query($conn, $sql_teacher);

    // Output the student information
    echo "<h2>Students:</h2>";
    while($row = mysqli_fetch_assoc($result_student)) {
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

    // Output the teacher information
    echo "<h2>Teachers:</h2>";
    while($row = mysqli_fetch_assoc($result_teacher)) {
        echo "Teacher Name: " . $row["TEACHING_FULL_NAME"] . "<br>";
        echo "Teacher Email: " . $row["TEACHING_STAFF_EMAIL"] . "<br>";
        echo "Phone Number: " . $row["TEACHING_STAFF_TELEPHONE"] . "<br>";
        echo "Role: " . $row["STAFF_ROLE_NAME"] . "<br>";
        echo "<br>";
    }
}
// If the input is not 'all', then search for the student or teacher with the given ID
else {
    // Query the database for the student with the given ID
    $sql_student = "SELECT * FROM STUDENT WHERE STUDENT_NO = '$id'";
    $result_student = mysqli_query($conn, $sql_student);

    // Query the database for the teacher with the given ID
    $sql_teacher = "SELECT * FROM TEACHING_STAFF WHERE TEACHING_STAFF_ID = '$id'";
    $result_teacher = mysqli_query($conn, $sql_teacher);

    // Check if the student was found
    if (mysqli_num_rows($result_student) > 0) {
        // Output the student information
        while($row = mysqli_fetch_assoc($result_student)) {
            echo "Student Name: " . $row["FULL_NAME"] . "<br>";
            echo "Student Email: " . $row["STUDENT_EMAIL"] . "<br>";
            echo "Phone Number: " . $row["PHONE_NO"] . "<br>";
            echo "Address: " . $row["ADDRESS"] . "<br>";
        }
    }
    // Check if the teacher was found
    // Check if the teacher was found
    else if (mysqli_num_rows($result_teacher) > 0) {
        // Output the teacher information
        while($row = mysqli_fetch_assoc($result_teacher)) {
            echo "<h2>Teacher Information:</h2>";
            echo "Teacher Name: " . $row["TEACHING_FULL_NAME"] . "<br>";
            echo "Teacher Email: " . $row["TEACHING_STAFF_EMAIL"] . "<br>";
            echo "Phone Number: " . $row["TEACHING_STAFF_TELEPHONE"] . "<br>";
            echo "Role: " . $row["STAFF_ROLE_NAME"] . "<br>";
        }
    }
}