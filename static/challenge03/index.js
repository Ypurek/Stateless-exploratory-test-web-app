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

