function show1() {
    let Button = document.getElementById('bounce');
    Button.addEventListener('click', function () {
        let Box = document.querySelector('.container1');  
        Box.classList.toggle('bounce');

      
    })
}

function show2() {
    let Button = document.getElementById('blink');
    Button.addEventListener('click', function () {
        let Box = document.querySelector('.container2');  
        Box.classList.toggle('blink');
    })
}

function show3() {
    Button.addEventListener('click', function () {
      let Box = document.querySelector(".container3");
      Box.classList.toggle("slideUp");
        
    })

    
}   

