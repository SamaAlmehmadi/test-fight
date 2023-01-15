
function ValidForm() {
	 
    var pw = document.forms['myForm']['password'].value;
    var pwc = document.forms['myForm']['confirm_password'].value;
    var email= document.forms['myForm']['email'].value;
    var firstName= document.forms['myForm']['first_name'].value;
    var lastName= document.forms['myForm']['last_name'].value;
    var phone= document.forms['myForm']['phone'].value;
 
    var regexEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
 
   if (firstName == "") { //check if firstname is empty, then alert the user the error text
       alert("check the First Name")
       return false
   }
 
   if (lastName.value == "") {//check if lastname is empty, then alert the user the error text
       alert("check the Last Name")
       return false
   }
 
   if(!regexEmail.test(email)){
         alert("EMAIL FORMAT IS NOT VALID !");
         return false;
     }
 
   if (!/05\d{7,15}/.test(phone)) { // use regex to valid user phone
       alert("check the Phone Number")
       return false
   }
   
   
   if ( pw != pwc) { //check if the age does not belong to the required intervale, then display the error message
       alert("check the password")
       return false
   }
 
 
 }
 

 window.onscroll = () => {
    var nav  = document.querySelector('nav');
    
    if (window.pageYOffset > 0) {
        nav.classList.add("sticky")
    } 
    else {
        nav.classList.remove("sticky");
    }
}

