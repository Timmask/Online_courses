let theme = document.querySelector('.add-theme')
let test = document.querySelector('.add-test')

theme.addEventListener('click', function() {
    let div = document.createElement('div')
        div.classList.add('add-card')

    div.innerHTML = `
        <h3>Тақырып 1</h3>
        <p>Лекцияың аты:</p>
        <input type="text">
        <p>Лекцияның мәтіні:</p>
        <textarea></textarea>
        <p>Видеолекция</p>
        <input type="file">
        <button>Жою</button>
    `

    document.querySelector('.main-area__item').prepend(div)
})
test.addEventListener('click', function() {

})