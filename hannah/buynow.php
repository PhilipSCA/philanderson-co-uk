<html>
<head>

<link rel="icon" href="images/icon5.png">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<title>DTD - Pay Now!</title>

<style>
        body {
          font-family: Verdana, Geneva, Tahoma, sans-serif;
          background-color: white;
          background-color: #ffffff;
          background-position: center;
          background-repeat: repeat;
          background-size: cover;
        }


        
        /* Navbar links */
        .navbar a {
            float: left;
            text-align: center;
            padding: 12px;
            color: white;
            text-decoration: none;
            font-size: 17px;
        }
        
        /* Navbar links on mouse-over */
        .navbar a:hover {
            background-color: #000;
        }
        
        
        /* Add responsiveness - will automatically display the navbar vertically instead of horizontally on screens less than 500 pixels */
        @media screen and (max-width: 500px) {
            .navbar a {
            float: none;
            display: block;
            }
        }

        .bg-img {
  /* The image used */
  background-image: url("https://i.pinimg.com/originals/60/e9/3d/60e93de6c2475b184f5aca595fa53237.jpg");

  min-height: 380px;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

  /* Needed to position the navbar */
  position: relative;
}

/* Position the navbar container inside the image */
.container {
  position: absolute;
  margin: 20px;
  width: auto;
}

/* The navbar */
.topnav {
  overflow: hidden;
  background-color: #333;
}

/* Navbar links */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}
</style>

<body>

<div class="navbar">
<div class="bg-img">
  <div class="container">
    <div class="topnav">
 
  <a href="index.html"><i class="fa fa-fw fa-home"></i> Home</a> 
  <a href="#"><i class="fa fa-fw fa-search"></i>Watch</a> 
  <a href="#"><i class="fa fa-fw fa-envelope"></i>My Work</a> 
  <a href="#"><i class="fa fa-fw fa-user"></i> Find Out More</a>
  </div>
  </div>
</div>

</body>

<form action="purchase.php" method="POST">
<label for="email">Your Email Address</label>
<input id="email" name="email" type="text" placeholder="Enter your email here"></input>
<br><br>
<label for="cardcode">Gift Card Code</label>
<input id="cardcode" name="cardcode" type="text" placeholder="Enter your gift card code here"></input>
<br>
<input type="submit"></input>
</form>

<script src="https://shoppy.gg/api/embed.js"></script>
<button data-shoppy-product="Jlxcu8K" style="background-color: red;">Pay</button>

</head>
</html>