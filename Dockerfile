# FROM python:slim

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . /app
# EXPOSE 5000

# ENV FLASK_APP="app/__init__.py"

# CMD ["flask", "run", "--host=0.0.0.0"]


FROM python:slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000

ENV FLASK_APP="app/__init__.py"

CMD ["flask", "run", "--host=0.0.0.0"]