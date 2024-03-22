document.getElementById("").onclick = function() {
    goToLandingPage('Enchant_spar');
  };
  
  function goToLandingPage(Enchant_spar) {
    window.location.href = 'http://127.0.0.1:5000/' + Enchant_spar ;
  }