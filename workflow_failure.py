from prefect import flow, task

@task
def failing_task():
    raise Exception("Simulated failure")

@flow(retries=3, retry_delay_seconds=5)
def failure_workflow():
    failing_task()
