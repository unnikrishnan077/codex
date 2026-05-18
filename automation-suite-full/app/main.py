from fastapi import FastAPI

from app.api import auth, health, jobs, records, search
from app.automation.scheduler import start_scheduler
from app.core.logging import setup_logging
from app.dashboard.views import router as dashboard_router
from app.db.base import Base
from app.db.session import engine

setup_logging()
Base.metadata.create_all(bind=engine)
start_scheduler()

app = FastAPI(title="automation-suite-full")
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(records.router)
app.include_router(jobs.router)
app.include_router(search.router)
app.include_router(dashboard_router)
