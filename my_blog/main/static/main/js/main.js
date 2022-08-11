const alertBtn = document.querySelector('.alert-btn')
let sqB = document.querySelector('.sq-btn')
let square = document.querySelector('.square')



if (sqB) {
  sqB.addEventListener('click', () => {
    console.log('btn clicked');
  });
}

sqB?.addEventListener('click', () => {
  console.log('btn clicked');
});



function add () {
    console.log(2 + 2)
}


sqB.addEventListener('click', add);