<?php
	session_start();

	$_SESSION['views'] = $_SESSION['views'] + 1;

	echo $_SESSION['views'];
?>

<!DOCTYPE html>
<html>
<head>
	<title>Philip - Homepage</title>
	<link rel="stylesheet" href="../style.css" type="text/css">
	

</head>

<body>
	<!-- <button class="btn btn-primary">Default</button> -->
	<div class="navigation">
	<header>
		<nav>
			<ul>
				<li><a href="../index.html">Home</a></li>
				<li><a href="../about.html">About</a></li>
				<li><a href="../login.html">Login</a></li>
			</ul>
		</nav>
	</header>
</div>
	<section>
		<div id="titlediv">
		<h2 class="title">Dashboard</h2>

		</div>
		<hr>

	</section>
</body>
</html>