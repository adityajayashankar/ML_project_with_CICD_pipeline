FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

# Use archived Debian Buster repositories
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/|http://archive.debian.org/|g' /etc/apt/sources.list && \
    apt-get update -y && apt-get install awscli -y

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
