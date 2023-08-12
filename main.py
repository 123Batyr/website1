from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI()

# Подключаем статические файлы (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="templates")

class Link(BaseModel):
    name: str
    url: str
    description: str

links = [
    Link(name="Яндекс", url="https://yandex.ru/maps/org/tm_limited_by_berdi_begmenov/83646725806/reviews/?ll=37.663082%2C55.709275&z=16", description="Поиск информации и интернет-сервисы"),
    Link(name="2ГИС", url="https://2gis.ru/moscow/firm/70000001063755552/tab/reviews?m=37.663033%2C55.709309%2F16", description="Поисковая система и интернет-сервисы"),
    Link(name="zoon", url="https://zoon.ru/msk/stores/magazin_muzhskoj_odezhdy_tm_limited_by_berdi_begmenov/", description="Поисковая система и интернет-сервисы"),
    # Link(name="Google", url="https://www.google.com", description="Поисковая система и интернет-сервисы")
    # Добавьте еще ссылки и описания по аналогии
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "links": links})
