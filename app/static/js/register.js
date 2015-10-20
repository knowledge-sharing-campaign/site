var validate = function() {

    if (!/^[A-Za-z]+$/.test(document.register.firstname.value)) {
        alert("Please provide your first name.");
        document.register.firstname.focus();
    }

    if (!/^[A-Za-z]+$/.test(document.register.lastname.value)) {
        alert("Please provide your last name.");
        document.register.lastname.focus();
    }

    if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(document.register.email.value)) {
        alert("Please provide a valid e-mail address.");
        document.register.email.focus();
    }

    if (!/^[0-9]+$/.test(document.register.contactnumber.value)) {
        alert("Please provide your contact number.");
        document.register.contactnumber.focus();
    }

    if (!/^[A-Za-z]+$/.test(document.register.university.value)) {
        alert("Please provide your university.");
        document.register.university.focus();
    }

    if (!/^[A-Za-z]+$/.test(document.register.course.value)) {
        alert("Please provide your course.");
        document.register.surname.focus();
    }

    if (!/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{6,15}$/.test(document.register.password.value)) {
        alert("Please provide your password. It should contain 6-15 characters, at least 1 digit, 1 uppercase letter, 1 lowercase letter and 1 special character. Also it should not conatin any spaces.");
        document.register.password.focus();
    }

    if (!document.register.password.value == document.register.confirmpassword.value)
        alert("Password Mismatch. Please provide your password again.");
        document.register.password.focus();
    }
