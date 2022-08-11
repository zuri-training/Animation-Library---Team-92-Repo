function show1() {
  const Button = document.getElementById("bounce");
  Button.addEventListener("click", function () {
    var Box = document.querySelector(".container1");
    console.log("remove");
    Box.classList.remove("bounce");
    setTimeout(() => {
      console.log("add");
      Box.classList.add("bounce");
    }, 100);
  });
}

function show2() {
  const Button = document.getElementById("blink");
  Button.addEventListener("click", function () {
    let Box = document.querySelector(".container2");
    Box.classList.add("blink").value;
  });
}

function show3() {
  const Button = document.getElementById("slideup");
  Button.addEventListener("click", function () {
    var Box = document.querySelector(".container3");
    Box.classList.toggle("slideUp");
  });
}
