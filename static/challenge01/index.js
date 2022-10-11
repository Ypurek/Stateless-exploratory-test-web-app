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

// todo for secret key part
// function task2() {
//     let url = '/challenge01/task2';
//     fetch(url).then((response) => response.json()).then((data) => console.log(data));
// }

function task3() {
    let url = '/challenge01/task3?value=';
    let value = document.querySelector('.secretInput').value;
    let result = document.querySelector('.secretOutput');
    result.classList.remove('ok', 'nok');
    result.textContent = '';
    let encodedValue = '';
    value = value.replace('❤️', '');
    console.log(value);
    try {

        encodedValue = btoa(value);
    } catch (error) {
        result.classList.add('nok')
        result.textContent = 'nok'
        return;
    }

    fetch(url + encodedValue).then((response) => response.json()).then((data) => {
        result.textContent = data.output;
        if (data.result) result.classList.add('ok')
        else result.classList.add('nok');
    })
}