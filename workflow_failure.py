from prefect import flow, task

@task(retries=3, retry_delay_seconds=5)
def retry_task():
    print("Task attempt")
    raise Exception("Retrying")

@flow
def failure_workflow():
    retry_task()
