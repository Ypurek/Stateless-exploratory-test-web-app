import re
import aiofiles
import base64
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(debug=False)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(response: Response):
    response.set_cookie(key='secretKeyPartEncoded', value='PDw8PDw8PDw8PDwrKysrKysrKysrKw==')
    async with aiofiles.open('index.html', 'r') as index:
        return await index.read()


@app.get("/task/1", response_class=JSONResponse)
async def task1(value: str = ''):
    # rule: string 6-14 chars
    # only latin chars, at least 1 capital
    # 2 digits, but not next to each other
    # !@# chars allowed, but not more than 2
    # spaces stripped
    if len(value) == 0:
        return JSONResponse(content={"response": False,
                                     'showHint': True})

    clear = base64.b64decode(value).decode().strip()
    pattern = '^[a-zA-Z0-9!@#]{6,14}$'
    if not re.search(pattern, clear):
        return JSONResponse(content={"response": False})
    if sum(map(str.isupper, clear)) < 1:
        return JSONResponse(content={"response": False})
    if sum(map(lambda x: x in '!@#', clear)) > 2:
        return JSONResponse(content={"response": False})
    if sum(map(lambda x: x in '0123456789', clear)) != 2:
        return JSONResponse(content={"response": False})
    ''.isnumeric()
    for index, i in enumerate(clear):
        if index < len(clear) - 2 and i.isnumeric() and clear[index + 1].isnumeric():
            return JSONResponse(content={"response": False})
    return JSONResponse(content={"response": True})


@app.get("/task/2", response_class=JSONResponse)
async def task2():
    return JSONResponse(content={"secretKeyPartEncoded": "KysrKysrKysrKys+Pj4+Pj4+Pj4+Pj4+Pj4+"})


@app.get("/task/3", response_class=JSONResponse)
async def task3(value: str = ''):
    if any(i not in '12345678' for i in value):
        return JSONResponse(content={"response": ''})

    if value.endswith('8'):
        value = value[0:-1]

    parity = ''
    if len(value) > 0 and len(value) % 2 == 0:
        parity = '8'

    if value == '':
        return JSONResponse(content={"response": '1' + parity})
    if value == '1':
        return JSONResponse(content={"response": '2' + parity})
    if value == '2':
        return JSONResponse(content={"response": '35' + parity})
    if value == '35':
        return JSONResponse(content={"response": '467' + parity})
    if value == '467':
        return JSONResponse(content={"response": '26' + parity})
    if value == '26':
        return JSONResponse(content={"response": '1' + parity})
    return JSONResponse(content={"response": '1' + parity})
