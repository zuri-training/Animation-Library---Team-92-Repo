function show(){
    var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='BounceIn'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
   }
    function show2() {

      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='BounceInFromBottom'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show3() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='BounceOut'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show4() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='BounceOutFromBottom'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show5() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='fade_In'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show6() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='fade_InDown'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show7() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='fade_Out'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show8() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='fade_OutLeft'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show9() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='Move_InLeft'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show10() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='Move_InUp'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show11() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='move_OutRight'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }

    function show12() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='move_OutUp'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show13() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='flip_in_180'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show14() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='flip_inX'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show15() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='flip_out_180'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }
    function show16() {
      var showContent = document.getElementById("display");
      showContent.innerHTML ="<p>&lt;div&gt; <br> &lt;p class='flip_outX'&gt &lt;/p&gt <br>  &lt;div&gt</p>";
      
    }

function copyText(){
  document.querySelector("#display").select();
  document.execCommand('copy');
}
    
document.querySelector(".copyImg").onClick = function(){
  copyText(document.querySelector("#display"))
}