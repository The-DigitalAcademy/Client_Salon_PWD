document.getElementById("button").onclick = function() {
    goToLandingPage('Services_sharon');
  };
  
  function goToLandingPage(Service_enchant) {
    window.location.href = 'http://127.0.0.1:5000/Services_sharon' + Services_sharon ;
  }