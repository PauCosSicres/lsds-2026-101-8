FROM python:3.11-slim

WORKDIR /code

RUN pip install fastapi uvicorn python-multipart httpx

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]A