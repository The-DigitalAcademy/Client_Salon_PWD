document.getElementById("button").onclick = function() {
    goToLandingPage('Service_enchant');
  };
  
  function goToLandingPage(Service_enchant) {
    window.location.href = 'http://127.0.0.1:5000/' + Service_enchant;
  }