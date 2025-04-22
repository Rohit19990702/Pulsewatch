from celery import shared_task
@shared_task
def send_alert(message):
    print(f'Alert: {message}')