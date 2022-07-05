const u_name = /^[a-zA-Z]([a-z\SA-Z0-9]){4,9}$/;
const email = /^([_\.\-0-9\Sa-zA-Z]+)@([\_\.\-0-9a-z\SA-Z]+)\.([\Sa-zA-Z]){2,7}$/;
const f_name = /^[A-Z]([\Sa-z]){3,10}$/;
const l_name = /^[A-Z]([\Sa-z]){3,10}$/;
const password = /^[a-zA-Z]([a-zA-Z0-9]){6}[0-9]$/;
const btn = document.getElementById('btn');


let user_name = document.getElementById('u_name');
user_name.addEventListener('blur', () => {
    if (u_name.test(user_name.value)) {
        user_name.classList.remove('is-invalid');
        user_name.classList.add('is-valid');
        btn.removeAttribute('disabled');
    }
    else{
        user_name.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});

let u_email = document.getElementById('email');
u_email.addEventListener('blur', () => {
    if (email.test(u_email.value)) {
        u_email.classList.remove('is-invalid');
        u_email.classList.add('is-valid');
        btn.removeAttribute('disabled');
    }
    else{
        u_email.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});

let fname = document.getElementById('fname');
fname.addEventListener('blur', () => {
    if (f_name.test(fname.value)) {
        fname.classList.remove('is-invalid');
        fname.classList.add('is-valid');
        btn.removeAttribute('disabled');
    }
    else{
        fname.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});

let lname = document.getElementById('lname');
lname.addEventListener('blur', () => {
    if (l_name.test(lname.value)) {
        lname.classList.remove('is-invalid');
        lname.classList.add('is-valid');
        btn.removeAttribute('disabled');
    }
    else{
        lname.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});

let u_password = document.getElementById('pass');
u_password.addEventListener('blur', () => {
    if (password.test(u_password.value)) {
        u_password.classList.remove('is-invalid');
        u_password.classList.add('is-valid');
        btn.removeAttribute('disabled');
    }
    else{
        u_password.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});

let cpassword = document.getElementById('c_pass');
cpassword.addEventListener('blur', () => {
    if (u_password.value == cpassword.value) {
        cpassword.classList.remove('is-invalid');
        cpassword.classList.add('is-valid');
        btn.removeAttribute('disabled');
    }
    else{
        cpassword.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});