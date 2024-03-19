
  
  document.getElementById("hair_Salon").onclick = function() {
    // Add id from html here to handle the onclick event
    goToLandingPage(landing);
  };
  
  function goToLandingPage(landing) {
    // code here to navigate back to the landing page
    window.location.href = 'http://127.0.0.1:5000/'; // Replace 'landing.html' with the actual URL of your landing page
  }