<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CST2340 University Website Design</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.1/css/fontawesome.min.css">
<link rel="stylesheet" href="fontawesome-free-6.3.0-web\css\all.min.css">
</head>
<body>
<section class="sub-header">
    <nav>
        <a href="index.html"><img src="images/logo.png"></a>
        <div class="nav-links" id="navLinks">
            <i class="fa fa-times" onclick="hideMenu()"></i>
            <ul>
                <li><a href="index.html">HOME</a></li>
                <li><a href="about.html">ABOUT</a></li>
                <li><a href="course.html">COURSE</a></li>
                <li><a href="blog.html">BLOG</a></li>
                <li><a href="contact.html">CONTACT</a></li>
                <li><a href="students.php">STUDENTS</a></li>
            </ul>
        </div>
        <i class="fa fa-bars" onclick="showMenu()"></i>
    </nav>
    <h1>STUDENTS</h1>
</section>
<body>

<link rel="stylesheet" href="phpstyle.css">
<!--SEARCH AND DISPLAY ALL--->
<h1> Search with Student or Staff NO</h1>

<form action="student1.php" method="post">
    Student or Staff NO: <input type="text" name="SID"><br>
    <input type="submit" name="submit" value="submit" class="hero-btn red-btn">
</form>

</body>
<body>

<!------INSERT INTO STUDENT TABLE------>
<h1> Insert Student Details </h1>

<form action= "student2.php" method="post">

	Student No: <input type = "text" name="STUDENT_NO"><br>

    Student Id: <input type = "text" name="STUDENT_ID"><br>

    Student University ID: <input type = "text" name="UNI_ID"><br>

    Faculty ID: <input type = "text" name="FACULTY_ID"><br>

    Full Name: <input type = "text" name="FULL_NAME"><br>

    Faculty Name: <input type = "text" name="FCLT_NAME"><br>

    Date of Birth: <input type = "text" name="DATE_OF_BIRTH"><br>

	Student email: <input type = "text" name="STUDENT_EMAIL"><br>

	Phone Number: <input type = "text" name="PHONE_NO"><br>
    
    Address: <input type = "text" name="ADDRESS"><br>

	<input type="submit" name="submit" value="Submit" class="hero-btn red-btn">


</form>
</body>

<br>
<br>

<!----DELETE FROM THE STUDENT TABLE------>
<body>

<h1> Delete Student Details </h1>

<form action= "student3.php" method="post">

	Student Id: <input type = "text" name="STUDENT_NO"><br>

	<input type="submit" name="submit" value="Submit" class="hero-btn red-btn">

</form>
</body>


<!----- Footer ------>

<section class="footer">
    <h4>About Us</h4>
    <p>Covenant University is a world-class institution committed to academic excellence, leadership development, and positive societal impact. 
        We offer a wide range of undergraduate, graduate, and postgraduate programs in various fields of study, 
        with renowned faculty members and state-of-the-art facilities. <br>Contact Us today for more information or visit our <a href="FAQ.html">FAQ</a></p>
        <div class="icons">
            <i class="fa-brands fa-facebook"></i>
            <i class="fa-brands fa-twitter"></i>
            <i class="fa-brands fa-instagram"></i>
            <i class="fa-brands fa-linkedin"></i>
            <i class="fa-brands fa-youtube"></i>
        </div>
        <p>Made with <i class="fa-regular fa-heart"></i> by Group HE04</p>
</section>



<!-----JavaScript code to Toggle menu (viewing in other device mode)------>
<script>
    var navLinks = document.getElementById("navLinks");
    function showMenu(){
        navLinks.style.right = "0";
    }
    function hideMenu(){
        navLinks.style.right = "-200px";
    }
</script>
<!-----JavaScript code to Toggle menu (viewing in other device mode)------>


</body>
</html>
