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
        "title": "Введение",
        "request": request,
    }
    return templates.TemplateResponse(
        name="inner.html",
        context=context,
    )


@app.get("/blockchain", response_class=HTMLResponse)
async def blockchain_page(request: Request):
    context = {
        "title": "Блокчейн",
        "request": request,
    }
    return templates.TemplateResponse(
        name="blockchain.html",
        context=context,
    )


@app.get("/smart-contracts", response_class=HTMLResponse)
async def contracts_page(request: Request):
    context = {
        "title": "Смарт - контракты",
        "request": request,
    }
    return templates.TemplateResponse(name="contract.html", context=context)


@app.get("/mining", response_class=HTMLResponse)
async def mining_page(request: Request):
    context = {
        "title": "Майнинг",
        "request": request,
    }
    return templates.TemplateResponse(name="mining.html", context=context)
