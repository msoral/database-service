FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./database_service /app
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt