<?php
    $con=mysqli_connect("localhost","root","","database1");
    // Check connection
    if (mysqli_connect_errno())
      {
      echo "Failed to connect to MySQL: " . mysqli_connect_error();
      }

    $result = mysqli_query($con,"SELECT * FROM latest");

    echo "<center><header style='color: red; font-size:40px; font-family:monospace'> Latest Movies <header></center>";
    echo "<main style='border: 5px solid gray; border-radius:10px;'>";
    while($row = mysqli_fetch_array($result))
      {
      echo "<br><center><v style='color:red; font-size:20px;'>".$row['names'] . "<a href='" . $row['links']."' target='blank'> <br>".$row['links']."</a></v></center>"; 
        //these are the fields that you have stored in your database table employee
      }
    echo "</main>";

    mysqli_close($con);
?>