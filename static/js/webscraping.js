function checkPasswordMatch() {
    var password = document.getElementById("psw").value;
    var confirmPassword = document.getElementById("psw-repeat").value;

    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return false; // Prevent form submission
    }

    return true; // Allow form submission
  }




