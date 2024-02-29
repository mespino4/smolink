# Use the official Python image
#FROM python:3.11-alpine

# Set the working directory in the container
#WORKDIR /deployment

# Copy the current directory contents into the container at /deployment
#COPY . /deployment

# Install any needed dependencies specified in requirements.txt
#RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
#EXPOSE 8000

# Run app.py when the container launches
#CMD ["gunicorn", "--bind=0.0.0.0:8000", "run:app"]
#CMD ["gunicorn", "-w", "4", "-b", "127.0.0.1:8000", "run:app"]


# syntax=docker/dockerfile:1

FROM python:3.11-alpine

WORKDIR /flask-server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "run:app"]