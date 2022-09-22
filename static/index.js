function task1() {
    let result = document.querySelector('.result');
    result.classList.remove('ok', 'nok');
    let url = '/task/1?value=';
    let value = document.getElementById('textInput').value;
    let encodedValue = '';
    try {
        encodedValue = btoa(value);
    } catch (error) {
        result.classList.add('nok')
        result.textContent = 'nok'
    }
    fetch(url + encodedValue).then((response) => response.json()).then((data) => {
        console.log(data);
        if (data.showHint) {
            document.querySelector('.hint').classList.remove('hintHide')
        }
        let result = document.querySelector('.result');
        if (data.response) {
            result.classList.add('ok')
            result.textContent = 'ok'
        } else {
            result.classList.add('nok')
            result.textContent = 'nok'
        }
    })
}

function task3() {
    let result = '';
    for (let i = 1; i <= 8; i++) {
        let checkbox = document.querySelector('#c' + i);
        if (checkbox.checked) {
            result += i
        }
        checkbox.checked = !1
    }
    let url = '/task/3?value=';
    fetch(url + result).then((response) => response.json()).then((data) => {
        console.log(data);
        data.response.split('').forEach(x => {
            document.querySelector('#c' + x).checked = !0
        })
    })
}