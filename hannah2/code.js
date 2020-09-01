

$query = "INSERT INTO comments(post_id,username,comment) VALUES ('$post_id','$commentorname','$comment')";
mysqli_query($con,$query);

$query = "SELECT * FROM comments WHERE post_id='{$id}'";
$result = mysqli_query($con,$query);
$row = mysqli_fetch_array($result);