document.getElementById("spar").onclick = function() {
    // get an element id from html to handle the onclick event
    goToLandingPage(nails);
  };
  
  function goToLandingPage(nails) {
    //  to navigate back to the nails page
    window.location.href = 'http://127.0.0.1:5000/nails'; // Replace 'landing.html' with the actual URL of your landing page
  }