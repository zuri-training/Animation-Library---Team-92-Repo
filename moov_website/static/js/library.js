

function myFunction() {
  var showContent = document.getElementById("display");
  var element = document.getElementById("myDIV");
  element.classList.toggle("bounce");
  showContent.value="<div class='BounceIn'>  \n \n</div>"
  
}
function show2() {
  var showContent = document.getElementById("display");
  var element = document.getElementById("myDIV");
  element.classList.toggle("bounceBtm");
  showContent.value="<div class='BounceInFromBottom'>  \n \n</div>"
  
  
}
 
  function show3() {
    var showContent = document.getElementById("display");
  var element = document.getElementById("myDIV");
  element.classList.toggle("bounceOut");
  showContent.value="<div class='BounceOut'>  \n \n</div>"
    
  }
  function show4() {
    var showContent = document.getElementById("display");
  var element = document.getElementById("myDIV");
  element.classList.toggle("bounceOutFromBottom");
  showContent.value="<div class='BounceOutFromBottom'>  \n \n</div>"
  }
  function show5() {
    var showContent = document.getElementById("display");
    showContent.value="<div class='fade_In'>  \n \n</div>"
    
  }
  function show6() {
    var showContent = document.getElementById("display");
    showContent.value="<div class='fade_InDown'>  \n \n</div>"
    
  }
  function show7() {
    var showContent = document.getElementById("display");
    showContent.value="<div class='fade_Out'>  \n \n</div>"
    
  }
  function show8() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='fade_OutLeft'>  </div>";
    
  }
  function show9() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='Move_InLeft'> </div>";
    
  }
  function show10() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='Move_InUp'> </div>";
    
  }
  function show11() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='move_OutRight'> </div>";
    
  }

  function show12() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='move_OutUp'><div>";
    
  }
  function show13() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='flip_in_180'> </div>";
    
  }
  function show14() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='flip_inX'> </div>";
    
  }
  function show15() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='flip_out_180'>  </div>";
    
  }
  function show16() {
    var showContent = document.getElementById("display");
    showContent.value ="<div class='flip_outX> </div>";
    
  }

function copyText(){
document.querySelector("#display").select();
document.execCommand('copy');
}
  
document.querySelector(".copyImg").onClick = function(){
copyText(document.querySelector("#display"))
}