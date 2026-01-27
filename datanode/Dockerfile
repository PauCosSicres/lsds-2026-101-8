FROM python:3.11-slim

WORKDIR /code

COPY app /code/app

RUN pip install fastapi uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
