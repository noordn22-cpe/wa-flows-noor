from prefect import flow, task
from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

@task
def time_check():
    hour = datetime.now(IST).hour
    if not (11 <= hour <= 18):
        raise Exception("Outside allowed time window")
    return True

@task
def gated_task():
    return "Ran during allowed window"

@flow
def time_gated_workflow():
    time_check()
    gated_task()
