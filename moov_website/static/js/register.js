const firstName = document.getElementById("firstName");
const email = document.getElementById("email");
const password = document.getElementById("password");
const btn = document.getElementById("btn");

tn.addEventListener('click', function() {
    if(firstName.value == null || firstName.value == undefined || firstName.value == '' || firstName.value <= 0){
        errorFirstName.style.display = 'block';
        firstName.style.background = 'URL(images/icon-error.svg) right no-repeat'
    }
    else{
        errorFirstName.style.display = 'none';
      
    }
})
btn.addEventListener('click', function() {
    if(lastName.value == null || lastName.value == undefined || lastName.value == '' || lastName.value <= 0){
        errorLastName.style.display = 'block';
        lastName.style.border = '2px solid hsl(0, 100%, 74%)';
        lastName.style.background = 'URL(images/icon-error.svg) right no-repeat'
    }else{
        errorLastName.style.display = 'none';
       
    }
})
btn.addEventListener('click', function() {
    if(email.value == null || email.value == undefined || email.value == '' || (email.value.indexOf('@') == -1) ||(email.value.indexOf('.com') == -1) || email.value <= 0){
        errorEmail.style.display = 'block';
        email.style.border = '2px solid hsl(0, 100%, 74%)';
        email.style.background = 'URL(images/icon-error.svg) right no-repeat'
    }else{
        errorEmail.style.display = 'none';
        
    }
})
btn.addEventListener('click', function() {
    if(password.value == null || password.value == undefined || password.value == '' || password.length <= 7){
        errorPassword.style.display = 'block';
        password.style.border = '2px solid hsl(0, 100%, 74%)';
        password.style.background = 'URL(images/icon-error.svg) right no-repeat'
    }else{
        errorPassword.style.display = 'none';
        
    }
})