FROM python:3.11-slim

WORKDIR /code

RUN pip install fastapi uvicorn

COPY app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
