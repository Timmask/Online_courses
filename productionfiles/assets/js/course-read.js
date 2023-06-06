let areaItem = document.querySelectorAll('.main-area__item')
let mainRotate = document.querySelectorAll('.main-rotate')

areaItem.forEach( (item, index) => {
    item.addEventListener('click', function() {
        mainRotate[index].classList.toggle('main-rotate__active')
        this.classList.toggle('main-area__item-show')
    })
})