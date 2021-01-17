<?php



session_start();
$quantity = $_SESSION['quantity'];
if(!$quantity){
    exit;
}



?>

<html>
    <h1 style="color:white">After the that you payed...</h1>
    <p style="color: white">You can now Send me your files of your pictures.</p>
    <style>
        .file{
            color: magenta;
        }

        body {
          font-family: Verdana, Geneva, Tahoma, sans-serif;
          background-image: url("https://www.teahub.io/photos/full/35-351063_amoled-wallpaper-black-compass-wallpaper-hd.jpg");
          background-color: #ffffff;
          background-position: center;
          background-repeat: repeat;
          background-size: cover;
          
        }
        </style>
 
<body>

<?php
for($i = 0; $i < $quantity; $i++){
    echo '
    <input class="file" type="file"><br><br> ';
}
?>


</body>

<br><br>
<style>
      .loginbox input[type="submit"]{
                border: none;
                outline:none;
                height:40px;
                width: 1900px;
                background:#fb2525;
                color: #fff;
                font-size:18px;
                border-radius:20px;
                }
      .loginbox input[type="submit"]:hover{
                cursor:pointer;
                background:#ffc107;
                color:#000;
                }
      .active{
            color:#fff;
            background:#e02626;
              border-radius:4px;
                }
    </style>
  </head>
<body>
  <div class="loginbox">
<form>
  <input type="submit" name="" value="Submit">
</form>
</div>
</body>
</html> 