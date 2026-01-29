FROM python:3.11-slim

WORKDIR /code

RUN pip install --no-cache-dir fastapi uvicorn

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]