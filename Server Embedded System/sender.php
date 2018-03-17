
<!DOCTYPE html>
<html class="no-js">
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Blend &mdash;</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="author" content="Youness Kafia" />



  	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
	<link rel="shortcut icon" href="favicon.ico">
    
	<link href='https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic,700' rel='stylesheet' type='text/css'>
	<link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
	
	<!-- Animate.css -->
	<link rel="stylesheet" href="css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="css/icomoon.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="css/bootstrap.css">
	<!-- Owl Carousel -->
	<link rel="stylesheet" href="css/owl.carousel.min.css">
	<link rel="stylesheet" href="css/owl.theme.default.min.css">
	<!-- Theme style  -->
	<link rel="stylesheet" href="css/style.css">

	<script src="js/modernizr-2.6.2.min.js"></script>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>

	</head>
	<body>
        
	<div id="fh5co-page">
        
		<a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle"><i></i></a>
		<aside id="fh5co-aside" role="complementary" class="border">

			<h1 id="fh5co-logo"><a href="index.html"><img src="images/logo-colored.png" ></a></h1>
			<nav id="fh5co-main-menu" role="navigation">
				<ul>
					<li><a href="index.html">Home</a></li>
					<li><a href="video.html">Videos</a></li>
					<li><a href="sender.php">Control</a></li>
					<li><a href="ImagesLog.html">Images</a></li>
				</ul>
			</nav>

			<div class="fh5co-footer">
				<ul>
					<li><a href="#"><i class="icon-facebook"></i></a></li>
					<li><a href="#"><i class="icon-twitter"></i></a></li>
					<li><a href="#"><i class="icon-instagram"></i></a></li>
					<li><a href="#"><i class="icon-linkedin"></i></a></li>
				</ul>
			</div>

		</aside>

		<div id="fh5co-main">

			

			<div class="fh5co-narrow-content animate-box fh5co-border-bottom" data-animate-effect="fadeInLeft">
				<h2 class="fh5co-heading" >Control the camera</span></h2>
            
				<p><p></p></p>

				<div class="row">
                    
                    
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">

</script>
<button>Switch On</button>
<submit>Switch Off<submit>
<script>
$("button").click(function(){
    $.get("receiver.php/?kill=0", function(data, status){
    });
});

$("submit").click(function(){
    $.get("receiver.php/?kill=1", function(data, status){
    });
});
</script>
                    
                    
                    
					
                    
                    
                    
                    
					
				
    
    
                </div>

			</div>


			

		</div>
	</div>

	<!-- jQuery -->
	<script src="js/jquery.min.js"></script>
	<!-- jQuery Easing -->
	<script src="js/jquery.easing.1.3.js"></script>
	<!-- Bootstrap -->
	<script src="js/bootstrap.min.js"></script>
	<!-- Carousel -->
	<script src="js/owl.carousel.min.js"></script>
	<!-- Stellar -->
	<script src="js/jquery.stellar.min.js"></script>
	<!-- Waypoints -->
	<script src="js/jquery.waypoints.min.js"></script>
	<!-- Counters -->
	<script src="js/jquery.countTo.js"></script>
	
	
	<!-- MAIN JS -->
	<script src="js/main.js"></script>

	</body>
</html>





