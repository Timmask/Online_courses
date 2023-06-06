let ts = document.querySelectorAll('.sidebar-right__courses')
ts.forEach(item => {
    item.addEventListener('click', function (){
        this.classList.toggle('sidebar-right__courses-show')
    })
})