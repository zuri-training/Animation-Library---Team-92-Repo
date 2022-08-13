

function show1() {
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
    var element = document.getElementById("myDIV");
    element.classList.toggle("fade_In");
    showContent.value="<div class='fade_In'>  \n \n</div>"
    
  }
  function show6() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("fade_InDown");
    showContent.value="<div class='fade_InDown'>  \n \n</div>"
    
  }
  function show7() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("fade_Out");
    showContent.value="<div class='fade_Out'>  \n \n</div>"
    
  }
  function show8() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("fade_OutLeft");
    showContent.value="<div class='fade_OutLeft'>  \n \n</div>"
  }
  function show9() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("move_InLeft");
    showContent.value="<div class='move_InLeft'>  \n \n</div>"
    
  }
  function show10() {
   
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("move_InUp");
    showContent.value="<div class='move_InUp'>  \n \n</div>"
  }
  function show11() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("move_OutRight");
    showContent.value="<div class='move_OutRight'>  \n \n</div>"
    
  }

  function show12() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("move_OutUp");
    showContent.value="<div class='move_OutUp'>  \n \n</div>"
    
  }
  function show13() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("flip_In_180");
    showContent.value="<div class='flip_In_180'>  \n \n</div>"
  }
  function show14() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("flip_InX");
    showContent.value="<div class='flip_InX'>  \n \n</div>"
    
  }
  function show15() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("flip_Out_180");
    showContent.value="<div class='flip_Out_180'>  \n \n</div>"
    
  }
  function show16() {
    var showContent = document.getElementById("display");
    var element = document.getElementById("myDIV");
    element.classList.toggle("flip_OutX");
    showContent.value="<div class='flip_OutX'>  \n \n</div>"
    
  }

  function myFunction() {
    /* Get the text field */
    var copyLink = document.querySelector(".input-field");
  
    /* Select the text field */
    copyLink.select();
    copyLink.setSelectionRange(0, 999); //The amount of characters to select
  
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyLink.value);
  
    /* Alert the copied text */
    confirm(" Copied")
  
  
  }
  