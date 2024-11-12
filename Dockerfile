FROM python:3.11-slim

COPY ./app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD python main.py
