# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:53:24 2020

@author: Suraj
"""



<!DOCTYPE html>
<html >
<!--From https://codepen.io/frytyler/pen/EGdtg-->
<head>
  <meta charset="UTF-8">
  <title>ML API</title>
 

<style>
	body
	{
		background-repeat: no-repeat;background-size: cover;background-image: url('https://cdn1.vectorstock.com/i/1000x1000/24/95/digital-3d-printing-concept-background-vector-7362495.jpg');
		font-color:white;
		
	}

}
</style>
</head>

<body>
 <div class="login">
 	<center>
	<h1>3 D PRINTERS</h1>

     <!-- Main Input For Receiving Query to our ML -->
    <form action="{{ url_for('y_predict')}}"method="post">
    	
        <input type="text" name="Roughness" placeholder="roughness" required="required" /><br><br>
        <input type="text" name="Tension Strength" placeholder="tension_strength" required="required" /><br><br>
        <input type="text" name="Elongation" placeholder="elongation" required="required" /><br><br>
        <button type="submit" class="btn btn-primary btn-block btn-large">Predict</button>
    
    </form>

   <br>
   <br>
   {{ prediction_text }}
</center>
 </div>



</body>
</html>

