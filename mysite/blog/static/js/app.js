let mobilePlusListTrigger = document.getElementById('mobile-list-trigger');
let mobileListItem = document.getElementById('mobile-list-item');
mobilePlusListTrigger.addEventListener('click', () => {
    mobileListItem.classList.toggle('mobile-list-active');
})


const openSearch = document.getElementById('openSearch');
const closeSearch = document.getElementById('closeSearch');
const mobileInput = document.getElementById('mobileInput');


openSearch.addEventListener('click', () => {
    mobileInput.classList.toggle('search-input');
    // console.log('clicked')
})
closeSearch.addEventListener('click', () => {
    mobileInput.classList.toggle('search-input');
    // console.log('clicked')
})

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


let collapsebtn = document.getElementById('collapse');
let collapse_body = document.getElementById('collapse-body');

collapsebtn.addEventListener('click', () => {
    collapse_body.style.display = 'block'
})

