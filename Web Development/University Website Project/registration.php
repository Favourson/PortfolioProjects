<html>
<head>
<link rel="stylesheet" href="regstyle.css">
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
                <li><a href="InputStudentID.php">STUDENTS</a></li>
            </ul>
        </div>
        <i class="fa fa-bars" onclick="showMenu()"></i>
    </nav>
    <h1>Register With Us Today!</h1>
</section>



<!---------- Registration Page --------->
<?php
// Define variables and set to empty values
$nameErr = $emailErr = $genderErr = $dobErr = $courseErr = "";
$name = $email = $gender = $dob = $course = $query = "";

// Function to test input data for data type validation
function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

// Function to test input data for format validation
function test_format($data) {
  if (!preg_match("/^[a-zA-Z ]*$/",$data)) {
    return false;
  } else {
    return true;
  }
}

// Function to test input data for comparison validation
function test_comparison($data1, $data2) {
  if ($data1 == $data2) {
    return true;
  } else {
    return false;
  }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Validate name input
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
    if (!test_format($name)) {
      $nameErr = "Only letters and white space allowed";
    }
  }

  // Validate email input
  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = test_input($_POST["email"]);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $emailErr = "Invalid email format";
    }
  }

  // Validate gender input
  if (empty($_POST["gender"])) {
    $genderErr = "Gender is required";
  } else {
    $gender = test_input($_POST["gender"]);
  }

  // Validate date of birth input
  if (empty($_POST["dob"])) {
    $dobErr = "Date of Birth is required";
  } else {
    $dob = test_input($_POST["dob"]);
    $today = date("Y-m-d");
    $diff = date_diff(date_create($dob), date_create($today));
    if ($diff->y < 18) {
      $dobErr = "You must be at least 18 years old to apply";
    }
  }

  // Validate course selection
  if ($_POST["course"] == "") {
    $courseErr = "Course selection is required";
  } else {
    $course = test_input($_POST["course"]);
  }

  // Validate query input
  $query = test_input($_POST["query"]);
}

?>


<p><span class="error">* required field</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  <label for="name">Full Name:</label>
  <input type="text" id="name" name="name" value="<?php echo $name;?>">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  <label for="email">Email:</label>
  <input type="text" id="email" name="email" value="<?php echo $email;?>">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>
  <label for="gender">Gender:</label>
  <input type="radio" id="male" name="gender" value="male"<?php if($gender == "male"){echo " checked";}?>>
  <label for="male">Male</label>
  <input type="radio" id="female" name="gender" value="female"<?php if($gender == "female"){echo " checked";}?>>
  <label for="female">Female</label>
  <span class="error">* <?php echo $genderErr;?></span>
  <br><br>
  <label for="dob">Date of Birth:</label>
  <input type="date" id="dob" name="dob" value="<?php echo $dob;?>">
  <span class="error">* <?php echo $dobErr;?></span>
  <br><br>
  <label for="course">Course:</label>
  <select id="course" name="course">
    <option value=""<?php if($course == ""){echo " selected";}?>>--Select--</option>
    <option value="Discovering the arts and humanities"<?php if($course == "Discovering the arts and humanities"){echo " selected";}?>>Discovering the arts and humanities</option>
    <option value="Early modern Europe: society and culture c.1500-1780"<?php if($course == "Early modern Europe: society and culture c.1500-1780"){echo " selected";}?>>Early modern Europe: society and culture c.1500-1780</option>
    <option value="Art and visual cultures in the modern world"<?php if($course == "Art and visual cultures in the modern world"){echo " selected";}?>>Art and visual cultures in the modern world</option>
    <option value="Exploring art and visual culture"<?php if($course == "Exploring art and visual culture"){echo " selected";}?>>Exploring art and visual culture</option>
    <option value="Engineering: mathematics, modelling, applications"<?php if($course == "Engineering: mathematics, modelling, applications"){echo " selected";}?>>Engineering: mathematics, modelling, applications</option>
    <option value="Mechanical engineering: heat and flow"<?php if($course == "Mechanical engineering: heat and flow"){echo " selected";}?>>Mechanical engineering: heat and flow</option>
    <option value="Essential economics: macro and micro perspectives"<?php if($course == "Essential economics: macro and micro perspectives"){echo " selected";}?>>Essential economics: macro and micro perspectives</option>
    <option value="Doing economics: people, markets and policy"<?php if($course == "Doing economics: people, markets and policy"){echo " selected";}?>>Doing economics: people, markets and policy</option>
    <option value="English for academic purposes online"<?php if($course == "English for academic purposes online"){echo " selected";}?>>English for academic purposes online</option>
    <option value="Developing subject knowledge for the primary years"<?php if($course == "Developing subject knowledge for the primary years"){echo " selected";}?>>Developing subject knowledge for the primary years</option>
  </select>
  <span class="error">* <?php echo $courseErr;?></span>
  <br><br>
  <label for="query">Query:</label>
  <textarea id="query" name="query" rows="5" cols="40"><?php echo $query;?></textarea>
  <br><br>
  <input type="submit" name="submit" value="Submit">
</form>

<?php
// Output the form data after successful validation
if ($nameErr == "" && $emailErr == "" && $genderErr == "" && $dobErr == "" && $courseErr == "" && isset($_POST['submit'])) {
  echo "<h2>Your Input:</h2>";
  echo "Name: " . $name . "<br>";
  echo "Email: " . $email . "<br>";
  echo "Gender: " . $gender . "<br>";
  echo "Date of Birth: " . $dob . "<br>";
  echo "Course: " . $course . "<br>";
  echo "Query: " . $query . "<br>";
}

?>

<!----- Footer from other html pages ------>

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