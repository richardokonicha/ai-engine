# Pull official base image
FROM python:3.10.8-slim-buster

# Set working directory
WORKDIR /

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV OPENAI_KEY <your_openai_key_here>

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc python3-opencv \
    && apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Add the app
COPY . .

EXPOSE 5001

CMD [ "python", "main.py" ]
