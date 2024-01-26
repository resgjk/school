from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title="artemy_plokhikh_crypto_proj")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    context = {
        "title": "Главная страница",
        "request": request,
    }
    return templates.TemplateResponse(
        name="inner.html",
        context=context,
    )
