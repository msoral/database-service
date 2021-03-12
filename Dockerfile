FROM python:3.7.9-buster
COPY . .
RUN apt update
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "flask", "run" ]