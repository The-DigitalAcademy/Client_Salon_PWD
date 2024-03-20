document.getElementById("button").onclick = function() {
    goToLandingPage('Services_sharon');
  };
  
  function goToLandingPage(Services_sharon) {
    window.location.href = 'http://127.0.0.1:5000/' + Services_sharon;
  }