FROM python:3.9-slim-buster

WORKDIR /app

COPY ../API_Calls/requirements.txt .

RUN pip install -r requirements.txt

COPY ../API_Calls/app.py .

EXPOSE 5000

CMD [ "python", "app.py" ]
