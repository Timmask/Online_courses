let left = document.querySelector('.open-left__sidebar')
let side_left = document.querySelector('.main-sidebar')

left.addEventListener('click', function() {
    side_left.classList.toggle('active-left__side')
    this.classList.toggle('open-left__rotate')
})