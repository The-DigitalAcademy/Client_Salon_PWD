document.getElementById("button").onclick = function() {
    goToLandingPage('Service_lumina');
  };
  
  function goToLandingPage(Service_lumina) {
    window.location.href = 'http://127.0.0.1:5000/'+ Service_lumina ;
  }