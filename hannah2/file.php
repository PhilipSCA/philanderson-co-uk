<?php
    $con= mysqli_connect("localhost","root","","database_name");
?>

$query = "INSERT INTO comments(post_id,username,comment) VALUES ('$post_id','$commentorname','$comment')";
mysqli_query($con,$query);