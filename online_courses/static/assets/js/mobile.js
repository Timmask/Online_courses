let left = document.querySelector('.open-left__sidebar')
let right = document.querySelector('.open-right__sidebar')
let side_left = document.querySelector('.sidebar-left')
let side_right = document.querySelector('.sidebar-right')
left.addEventListener('click', function() {
    side_left.classList.toggle('active-left__side')
    this.classList.toggle('open-left__rotate')
})
right.addEventListener('click', function() {
    side_right.classList.toggle('active-right__side')
    this.classList.toggle('open-right__rotate')
})