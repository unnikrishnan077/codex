from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["dashboard"])
templates = Jinja2Templates(directory="app/dashboard/templates")


@router.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Automation Suite"})
