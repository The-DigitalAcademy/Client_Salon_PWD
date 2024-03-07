document.getElementById("signupForm").addEventListener<"click">("click", submit)
    event.preventDefault(); // Prevent form submission
  
    // Get input values
    var name_surname = document.getElementById("name&surname").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
  
    // Perform form validation
    if (name&surname === "" || email === "" ||password === ""  ||confirm_password === ""){
      alert("Please fill in all fields");
      return;
     
    }
  
    // Perform signup process (you can replace this with your own logic)
    alert("Signup successful!");
    // Additional code for sending data to a server or performing other actions
  ;