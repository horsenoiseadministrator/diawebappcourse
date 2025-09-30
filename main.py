from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/", response_class=HTMLResponse)
def inputform():
    with open("input.html", "r") as file:
        html_content = file.read()
    return html_content


@app.get("/result/q={num1}&{num2}", response_class=HTMLResponse)
def result(num1: int, num2: int):
    sum_result = num1 + num2
    with open("result.html", "r") as file:
        html_content = file.read()
        html_content = html_content.replace("{num1}", str(num1))
        html_content = html_content.replace("{num2}", str(num2))
        html_content = html_content.replace("{result}", str(sum_result))
        
    return html_content


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

