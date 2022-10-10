function task1() {
    let url = '/challenge01/task1?value=';
    let result = document.querySelector('.result');
    let resultOut = document.querySelector('.resultOutput');
    result.classList.remove('ok', 'nok');
    resultOut.textContent = '';

    let value = document.getElementById('textInput').value;
    let encodedValue = '';
    try {
        encodedValue = btoa(value);
    } catch (error) {
        result.classList.add('nok')
        result.textContent = 'nok'
        resultOut.textContent = 'only eng';
        return;
    }
    fetch(url + encodedValue).then((response) => response.json()).then((data) => {
        if (data.showHint) {
            document.querySelector('.hint').classList.remove('hintHide')
        }
        if (data.response) {
            result.classList.add('ok')
            result.textContent = 'ok'
        } else {
            result.classList.add('nok')
            result.textContent = 'nok'
            resultOut.textContent = data.hint;
        }
    })
}

function task2() {
    let url = '/challenge01/task2?value=';
    let result = '';
    for (let i = 1; i <= 8; i++) {
        let checkbox = document.querySelector('#c' + i);
        if (checkbox.checked) {
            result += i
        }
        checkbox.checked = !1
    }

    fetch(url + result).then((response) => response.json()).then((data) => {
        data.response.split('').forEach(x => {
            document.querySelector('#c' + x).checked = !0
        })
    })
}

// todo for secret key part
// function task3() {
//     let url = '/challenge01/task3';
//     fetch(url).then((response) => response.json()).then((data) => console.log(data));
// }