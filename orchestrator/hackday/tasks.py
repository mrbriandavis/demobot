from celery import task
from time import sleep

@task()
def add(x, y):
    # sleep(400)
    return x + y

