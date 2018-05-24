FROM python:alpine

WORKDIR /app

RUN python -m pip install flask

ADD app.py .

CMD ["python", "app.py"]
