from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="templates")

class Link:
    def __init__(self, name: str, url: str, description: str):
        self.name = name
        self.url = url
        self.description = description

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1')