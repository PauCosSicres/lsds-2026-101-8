FROM python:3.11-slim

WORKDIR /code

COPY ./app /code/app

RUN pip install --no-cache-dir fastapi uvicorn python-multipart

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]