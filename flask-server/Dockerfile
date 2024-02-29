FROM python:3.11-alpine

WORKDIR /flask-server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "run:app"]