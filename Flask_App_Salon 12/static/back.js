 
  document.getElementById("forgot_password").onclick = function() {
    // Add id from html here to handle the onclick event
    goToLandingPage(login);
  };
  
  function goToLandingPage(login) {
    // code here to navigate back to the landing page
    window.location.href = 'http://127.0.0.1:5000/login'; // Replace 'landing.html' with the actual URL of your landing page
  }