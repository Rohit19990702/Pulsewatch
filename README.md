# PulseWatch
A log and mood monitoring system using Django + Celery + GPT.

## Setup
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
celery -A pulsewatch worker -l info
```