  
 document.getElementById("landing").onclick = function() {
    goToLandingPage('landing');
  };
  
  function goToLandingPage(landing) {
    window.location.href = 'http://127.0.0.1:5000/'+ landing ;
  }