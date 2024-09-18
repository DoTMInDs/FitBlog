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