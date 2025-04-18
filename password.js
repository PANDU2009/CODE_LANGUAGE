{/* <script language="JavaScript"> */ }
// <!--hide
var password;
var pass1 = "CODE";
var pass2 = "LENOVO"

password = prompt('Enter Password To Open Page', '');
if (password == pass1)
    alert('Correct Password, Click OK to Enter.');

else if (password == pass2)

    alert('Correct Password, Click OK to Enter.');

else {

    alert('Wrong password.');
    window.location = "https://google.com"
}
