document.addEventListener('DOMContentLoaded', function() {
    var checkButton = document.getElementById('clickThis');
    checkButton.addEventListener('click', function() {
    var inputVal = document.getElementById("myInput").value;
     alert(inputVal);

    }, false);
  }, false);
