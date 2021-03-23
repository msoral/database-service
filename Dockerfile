FROM python:3.7.9-buster
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .
RUN apt update
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python -m", "database_service" ]