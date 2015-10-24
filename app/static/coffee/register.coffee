onlyAlphaFilter = (e) ->
  e = window.event || e
  charCode = e.charCode || e.keyCode
  if (charCode >= 65 and charCode <= 122 or charCode is 8 or charCode is 32) then true else false

onlyNumFilter = (e) ->
  e = window.event || e
  charCode = e.charCode || e.keyCode
  if (charCode > 31 and (charCode < 48 or charCode > 57)) then false else true

document.getElementById("firstname").onkeypress = onlyAlphaFilter
document.getElementById("lastname").onkeypress = onlyAlphaFilter
document.getElementById("contact").onkeypress = onlyNumFilter

window.validateForm = ->
  pass = document.getElementById("password").value
  cpass = document.getElementById("confirmpassword").value

  if pass != cpass
    alert "Passwords don't match!"
    return false

  re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/
  if not re.test(pass)
    alert "Password must have at least one number, one lowercase and one uppercase letter and at least six characters"
    return false

  if not document.getElementById("tandc").checked
    alert "Please accept the terms and conditions before continuing"
    return false

  return true
