from fastapi import FastAPI
from app.api import auth, records, jobs, search, health
from app.dashboard.views import router as dashboard_router
from app.core.logging import setup_logging
from app.db.base import Base
from app.db.session import engine
from app.automation.scheduler import start_scheduler

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
