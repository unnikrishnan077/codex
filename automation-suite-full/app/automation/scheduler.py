from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(job_defaults={"misfire_grace_time": 30, "coalesce": True})


def start_scheduler() -> None:
    if not scheduler.running:
        scheduler.start()
