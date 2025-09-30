FROM python:3.12-slim

WORKDIR /.

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY='django-insecure-&*2-bs@*-c3&!$$5=oi$3bz16#^gsf7ci+6)er(ie3c7c&*7l7'
ENV CELERY_BROKER_URL="redis://redis:6379/0"
ENV CELERY_BACKEND="redis://redis:6379/0"

RUN mkdir -p /media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]