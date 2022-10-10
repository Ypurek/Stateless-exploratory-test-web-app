function task1() {
    let result = document.querySelector('.result');
    result.classList.remove('ok', 'nok');
    let url = '/task1?value=';
    let value = document.getElementById('textInput').value;
    let encodedValue = '';
    try {
        encodedValue = btoa(value);
    } catch (error) {
        result.classList.add('nok')
        result.textContent = 'I speak only En!'
    }
    fetch(url + encodedValue).then((response) => response.json()).then((data) => {
        // if (data.showHint) {
        //     document.querySelector('.hint').classList.remove('hintHide')
        // }
        if (data.response === 'OK') {
            result.classList.add('ok');
            result.textContent = 'ok';
        } else {
            result.classList.add('nok');
            result.textContent = data.response;
        }
    })
}

function task1_hard() {
    let result = document.querySelector('.result');
    result.classList.remove('ok', 'nok');
    let url = '/task1-hard?value=';
    let value = document.getElementById('textInput').value;
    let encodedValue = '';
    try {
        encodedValue = btoa(value);
    } catch (error) {
        result.classList.add('nok')
        result.textContent = 'I speak only En!'
    }
    fetch(url + encodedValue).then((response) => response.json()).then((data) => {
        // if (data.showHint) {
        //     document.querySelector('.hint').classList.remove('hintHide')
        // }
        if (data.response === 'OK') {
            result.classList.add('ok');
            result.textContent = 'ok';
        } else {
            result.classList.add('nok');
            result.textContent = data.response;
        }
    })
}

function task1_help() {
    let output = document.querySelector('.helpOutput');
    let url = '/task-help?value=';
    let value = document.querySelector('#numInputHelp').value;

    fetch(url + value).then((response) => response.json()).then((data) => {
        output.textContent = data.response;
    })
}

function task1_help_hard() {
    let output = document.querySelector('.helpOutput');
    let url = '/task-help-hard?value=';
    let value = document.querySelector('#numInputHelp').value;

    fetch(url + value).then((response) => response.json()).then((data) => {
        output.textContent = data.response;
    })
}

// todo
// function test2() {
//     let url = '/task2';
//     fetch(url).then((response) => response.json()).then((data) => console.log(data));
// }

function task3() {
    let result = '';
    for (let i = 1; i <= 8; i++) {
        let checkbox = document.querySelector('#c' + i);
        if (checkbox.checked) {
            result += i
        }
        checkbox.checked = !1
    }
    let url = '/task3?value=';
    fetch(url + result).then((response) => response.json()).then((data) => {
        data.response.split('').forEach(x => {
            document.querySelector('#c' + x).checked = !0
        })
    })
}

function dis(element) {
    element.disabled = true;
}