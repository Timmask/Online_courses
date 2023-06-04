let testItemBtn = document.querySelectorAll('.test-item button'),
    testItem = document.querySelectorAll('.test-item')

testItemBtn.forEach( item => {
    item.addEventListener('click', function() {
        this.parentElement.parentElement.classList.toggle('active')
    })
})