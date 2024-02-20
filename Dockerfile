FROM python:slim

WORKDIR /app

COPY . /app

RUN pip install -r req.txt

EXPOSE 5000

ENV FLASK_APP="app/__init__.py"

CMD ["flask", "run", "--host=0.0.0.0"]
