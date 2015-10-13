//function allnumeric(inputtxt)  
//   {  
//      var numbers = /^[0-9]+$/;  
//      if(inputtxt.value.match(numbers))  
//      {     
//      return true;  
//     }  
//     else  
//      {  
//      alert('Please input numeric characters only');  
//      document.form1.text1.focus();  
//      return false;  
//      }  
//   }

(function() {
  var validate;

  validate = function() {
    if (/^[A-Za-z]+$/.test(document.register.firstname.value))
        return true;
    alert("Please provide your first name.");
    document.register.firstname.focus();
    return false;

    if (/^[A-Za-z]+$/.test(document.register.lastname.value))
        return true;
    alert("Please provide your first name.");
    document.register.lastname.focus();
    return false;

    if (/^[A-Za-z]+$/.test(document.register.surname.value))
        return true;
    alert("Please provide your surname.");
    document.register.surname.focus();
    return false;

    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.register.email.value))
        return true;
    alert("Please provide a valid e-mail address.");
    document.register.email.focus();
    return false;

    if (/^[0-9]+$/.test(document.register.contactnumber.value))
        return true;
    alert("Please provide your contact number.");
    document.register.contactnumber.focus();
    return false;

    if (/^[A-Za-z]+$/.test(document.register.university.value))
        return true;
    alert("Please provide your university.");
    document.register.university.focus();
    return false;

    if (/^[A-Za-z]+$/.test(document.register.course.value))
        return true;
    alert("Please provide your course.");
    document.register.surname.focus();
    return false;

    if (/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{6,15}$/.test(document.register.password.value))
        return true;
    alert("Please provide your password. It should contain 6-15 characters, at least 1 digit, 1 uppercase letter, 1 lowercase letter and 1 special character. Also it should not conatin any spaces.");
    document.register.password.focus();
    return false;

    if (/^[A-Za-z]+$/.test(document.register.City.value))
        return true;
    alert("Please provide your city.");
    document.register.City.focus();
    return false;
};
}).call(this);