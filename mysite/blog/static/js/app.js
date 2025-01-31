// Mobile menu
const mobileMenu = document.getElementById('mobile_menu');
const navLinks = document.getElementById('nav-links');

mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.toggle('change');
    navLinks.classList.toggle('showing');
    // console.log('clicked');
});

function goBack() {
    window.history.back();
}


let time = document.getElementById('current-time');
setInterval(() => {
    let d = new Date();
    time.innerHTML = d.toLocaleTimeString();
}, 1000)


let collapsebtn = document.getElementById('collapse');
let collapse_body = document.getElementById('collapse-body');

collapsebtn.addEventListener('click', () => {
    collapse_body.style.display = 'block'
})



