function validateLoginForm() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    if (email === "" || password === "") {
      alert("Please fill in all fields");
      return false;
    }
    if(email.length < 5){
      alert("Email is too short");
      return false;
    }
    if (password.length < 5) {
      alert("Password is too short");
      return false;
    }
    if(!email.includes("@")){
      alert("Email is invalid");
      return false;
    }
    if(email.includes(" ")){
      alert("Email is invalid");
      return false;
    }
    if (password.includes(" ")) {
      alert("Password is invalid");
      return false;
    }
    return true;
  }