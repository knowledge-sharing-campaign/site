// Generated by CoffeeScript 1.10.0
(function() {
  var onlyAlphaFilter, onlyNumFilter;

  onlyAlphaFilter = function(e) {
    var charCode;
    e = window.event || e;
    charCode = e.charCode || e.keyCode;
    if (charCode >= 65 && charCode <= 122 || charCode === 8 || charCode === 32) {
      return true;
    } else {
      return false;
    }
  };

  onlyNumFilter = function(e) {
    var charCode;
    e = window.event || e;
    charCode = e.charCode || e.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
      return false;
    } else {
      return true;
    }
  };

  document.getElementById("firstname").onkeypress = onlyAlphaFilter;

  document.getElementById("lastname").onkeypress = onlyAlphaFilter;

  document.getElementById("contact").onkeypress = onlyNumFilter;

  window.validateForm = function() {
    var cpass, pass, re;
    pass = document.getElementById("password").value;
    cpass = document.getElementById("confirmpassword").value;
    if (pass !== cpass) {
      alert("Passwords don't match!");
      return false;
    }
    re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;
    if (!re.test(pass)) {
      alert("Password must have at least one number, one lowercase and one uppercase letter and at least six characters");
      return false;
    }
    if (!document.getElementById("tandc").checked) {
      alert("Please accept the terms and conditions before continuing");
      return false;
    }
    return true;
  };

}).call(this);
