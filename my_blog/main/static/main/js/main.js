const alertBtn = document.querySelector('.alert-btn')
let sqB = document.querySelector('.sq-btn')
let square = document.querySelector('.square')


function someClass () {
    square.classList.toggle('red')
}

sqB.addEventListener('click', someClass);
