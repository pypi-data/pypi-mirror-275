import time
from celery import shared_task

__all__ = [
    "ping",
    "echo",
    "sleep",
    "raise_error",
    "retry_n",
]


@shared_task(name="debug.ping")
def ping():
    return "pong"


@shared_task(name="debug.echo")
def echo(msg):
    return msg


@shared_task(name="debug.sleep")
def sleep(seconds):
    time.sleep(seconds)
    return True


@shared_task(name="debug.raise_error")
def raise_error():
    raise RuntimeError("always raise a RuntimeError...")


@shared_task(name="debug.retry_n", bind=True)
def retry_n(task, n, interval=0.1):
    if task.request.retries >= n:
        return True
    task.retry(
        exc=RuntimeError(f"debug.retry_n[{n}] error."),
        max_retries=9999,
        countdown=interval * task.request.retries,
    )
